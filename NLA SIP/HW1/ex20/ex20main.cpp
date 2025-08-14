// cholesky_cli.cpp
// Build:  g++ -O2 -std=c++17 cholesky_cli.cpp -o cholesky_cli
// Usage:  ./cholesky_cli [-A path/to/A.csv] [-U path/to/U.csv] [-L path/to/L.csv]
//
// Behavior:
// - Computes the Cholesky-like factor U from A using the user-specified routine below (kept verbatim).
// - Writes U to -U (default "U.csv").
// - Optionally writes L = U^T to -L if provided (otherwise skipped).
// - If a flag is omitted, you’ll be prompted. Empty input uses defaults A.csv and U.csv.
//
// Notes:
// - Per request, matrix operations avoid shape/value checks.
// - The Cholesky algorithm below is **exactly** the one you supplied; not altered.

/**
 * @file cholesky_cli.cpp
 * @brief CLI tool to compute (your) Cholesky factor U from a CSV matrix A.
 * @details
 *  - Input:  A (CSV), n×n.
 *  - Output: U (CSV), same size as A.
 *  - Optional: L = U^T (CSV) if -L given.
 *  - Matrix helpers avoid dimension/shape checks as requested.
 */

#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>

using Matrix = std::vector<std::vector<double>>;

/**
 * @brief Split a CSV line by ',' (no quote handling).
 */
std::vector<std::string> split_csv_line(const std::string &line)
{
    std::vector<std::string> parts;
    std::string cur;
    std::stringstream ss(line);
    while (std::getline(ss, cur, ','))
        parts.push_back(cur);
    if (!line.empty() && line.back() == ',')
        parts.push_back("");
    return parts;
}

/**
 * @brief Read a CSV file into a Matrix (rows × cols).
 * @throws std::runtime_error on file I/O error or non-numeric cells.
 * @note Keeps basic CSV consistency checks (file-level), but no matrix-shape guards elsewhere.
 */
Matrix read_csv_matrix(const std::string &path)
{
    std::ifstream fin(path);
    if (!fin)
        throw std::runtime_error("Failed to open file: " + path);

    Matrix M;
    std::string line;
    size_t cols = 0;
    size_t line_no = 0;
    while (std::getline(fin, line))
    {
        ++line_no;
        if (line.empty())
            continue;
        auto tokens = split_csv_line(line);
        if (cols == 0)
            cols = tokens.size();
        else if (tokens.size() != cols)
        {
            std::ostringstream err;
            err << "Inconsistent column count at line " << line_no
                << " (got " << tokens.size() << ", expected " << cols << ")";
            throw std::runtime_error(err.str());
        }

        std::vector<double> row;
        row.reserve(tokens.size());
        for (const auto &t : tokens)
        {
            if (t.empty())
            {
                row.push_back(0.0);
            }
            else
            {
                char *end = nullptr;
                double v = std::strtod(t.c_str(), &end);
                if (end == t.c_str() || *end != '\0')
                {
                    std::ostringstream err;
                    err << "Non-numeric entry '" << t << "' at line " << line_no;
                    throw std::runtime_error(err.str());
                }
                row.push_back(v);
            }
        }
        M.push_back(std::move(row));
    }
    if (M.empty())
        throw std::runtime_error("File is empty: " + path);
    return M;
}

/**
 * @brief Write a Matrix to CSV.
 */
void write_csv_matrix(const std::string &path, const Matrix &M)
{
    std::ofstream fout(path);
    if (!fout)
        throw std::runtime_error("Failed to open output file: " + path);
    fout.setf(std::ios::fixed);
    fout << std::setprecision(12);
    for (size_t i = 0; i < M.size(); ++i)
    {
        for (size_t j = 0; j < M[i].size(); ++j)
        {
            if (j)
                fout << ',';
            fout << M[i][j];
        }
        fout << '\n';
    }
}

/**
 * @brief (Your) Cholesky routine — kept EXACTLY as provided.
 * @param A (in/out): working copy updated in-place
 * @param U (out): result factor
 * @note No modifications to the algorithm/body.
 */
void Cholesky_decomp(Matrix &A, Matrix &U)
{
    const size_t n = A.size();

    for (size_t i = 0; i < n; ++i)
    {
        U[i][i] = sqrt(A[i][i]);
        for (size_t k = i + 1; k < n; ++k)
            U[i][k] = A[i][k] / U[i][i];

        // update A
        for (size_t j = i + 1; j < n; ++j)
        {
            for (size_t k = i + 1; k < n; ++k)
                A[j][k] -= U[i][k] * U[i][j];
        }
    }
}

/**
 * @brief Transpose of a matrix (no shape checks).
 */
Matrix transpose(const Matrix &M)
{
    if (M.empty())
        return {};
    const size_t rows = M.size();
    const size_t cols = M[0].size();
    Matrix MT(cols, std::vector<double>(rows, 0.0));
    for (size_t i = 0; i < rows; ++i)
        for (size_t j = 0; j < cols; ++j)
            MT[j][i] = M[i][j];
    return MT;
}

/**
 * @brief Matrix product C = A * B (no dimension checks).
 * @note Assumes A[0].size() == B.size() by convention; trusts caller.
 */
Matrix matmul(const Matrix &A, const Matrix &B)
{
    Matrix C(A.size(), std::vector<double>(B[0].size(), 0.0));
    for (size_t i = 0; i < A.size(); ++i)
        for (size_t j = 0; j < B[0].size(); ++j)
            for (size_t k = 0; k < A[0].size(); ++k)
                C[i][j] += A[i][k] * B[k][j];
    return C;
}

/**
 * @brief Prompt for a path with default fallback.
 */
std::string prompt_path(const std::string &label, const std::string &deflt)
{
    std::cout << label << " [" << deflt << "]: " << std::flush;
    std::string line;
    if (!std::getline(std::cin, line))
        return deflt;
    if (line.empty())
        return deflt;
    return line;
}

int main(int argc, char *argv[])
{

    std::string pathA, pathU, pathL;

    // Flags: -A input A.csv, -U output U.csv, -L optional output L.csv
    for (int i = 1; i < argc; ++i)
    {
        std::string arg = argv[i];
        auto need_next = [&](const char *flag)
        {
            if (i + 1 >= argc)
            {
                std::ostringstream err;
                err << "Missing value after " << flag;
                throw std::runtime_error(err.str());
            }
            return std::string(argv[++i]);
        };
        if (arg == "-A")
            pathA = need_next("-A");
        else if (arg == "-U")
            pathU = need_next("-U");
        else if (arg == "-L")
            pathL = need_next("-L");
        else if (arg == "-h" || arg == "--help")
        {
            std::cout
                << "Usage: " << argv[0] << " [-A path/to/A.csv] [-U path/to/U.csv] [-L path/to/L.csv]\n"
                << "If a flag is omitted, you'll be prompted. Empty input uses defaults A.csv and U.csv.\n";
            return 0;
        }
        else
        {
            std::ostringstream err;
            err << "Unknown argument: " << arg;
            throw std::runtime_error(err.str());
        }
    }

    if (pathA.empty())
        pathA = prompt_path("Path to matrix A (CSV)", "A.csv");
    if (pathU.empty())
        pathU = prompt_path("Path to output U (CSV)", "U.csv");
    // L is optional; only prompted if user wants it quickly.
    if (pathL.empty())
    {
        std::string wantL = prompt_path("Also write L = U^T? (enter path or leave empty to skip)", "");
        pathL = wantL;
    }

    Matrix A = read_csv_matrix(pathA);

    // Compute U using your routine (kept intact)
    Matrix Acopy = A;
    Matrix U(A.size(), std::vector<double>(A.size(), 0.0));
    Cholesky_decomp(Acopy, U);

    // Always write U
    write_csv_matrix(pathU, U);

    // Optionally write L = U^T
    if (!pathL.empty())
    {
        Matrix L = transpose(U);
        write_csv_matrix(pathL, L);
    }

    // Optional quick check (no throwing): form L*U and compare visually if you wish
    Matrix L = transpose(U);
    Matrix A_recon = matmul(L, U);
    write_csv_matrix("A_reconstructed.csv", A_recon);

    std::cout << "U written to: " << pathU << (pathL.empty() ? "" : (", L written to: " + pathL)) << "\n";
    std::cout << "Reconstructed A written to: A_reconstructed.csv\n";
    return 0;
}
