// linalg_kernels.cpp
// cppimport
/*

*/

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <vector>
#include <cmath>

namespace py = pybind11;

// -------- core kernels on double* (row-major) --------
// Row-major: element (i,j) stored at base[i*cols + j].

inline void cholesky_upper(double *A, double *U, std::size_t n)
{
    for (std::size_t i = 0; i < n; ++i)
    {
        U[i * n + i] = std::sqrt(A[i * n + i]);
        for (std::size_t k = i + 1; k < n; ++k)
            U[i * n + k] = A[i * n + k] / U[i * n + i];

        // update A: A[j,k] -= U[i,k] * U[i,j]
        for (std::size_t j = i + 1; j < n; ++j)
        {
            for (std::size_t k = i + 1; k < n; ++k)
            {
                A[j * n + k] -= U[i * n + k] * U[i * n + j];
            }
        }
    }
}

inline void transpose_rm(const double *M, double *MT, std::size_t rows, std::size_t cols)
{
    for (std::size_t i = 0; i < rows; ++i)
        for (std::size_t j = 0; j < cols; ++j)
            MT[j * rows + i] = M[i * cols + j];
}

inline void matmul_rm(const double *A, const double *B, double *C,
                      std::size_t n, std::size_t p, std::size_t m)
{
    // C = A(n x p) * B(p x m) -> (n x m)
    for (std::size_t i = 0; i < n; ++i)
    {
        for (std::size_t j = 0; j < m; ++j)
        {
            double s = 0.0;
            for (std::size_t k = 0; k < p; ++k)
            {
                s += A[i * p + k] * B[k * m + j];
            }
            C[i * m + j] = s;
        }
    }
}

// -------- pybind11 wrappers (NumPy arrays) --------

py::array_t<double> cholesky_upper_np(py::array_t<double, py::array::c_style | py::array::forcecast> A_in)
{
    auto buf = A_in.request();
    std::size_t n = static_cast<std::size_t>(buf.shape[0]); // assume square
    const double *Ain = static_cast<const double *>(buf.ptr);

    std::vector<double> A(Ain, Ain + n * n); // algo updates in-place

    py::array_t<double> U_out({n, n});
    auto Ubuf = U_out.request();
    double *U = static_cast<double *>(Ubuf.ptr);

    cholesky_upper(A.data(), U, n);
    return U_out;
}

py::array_t<double> transpose_np(py::array_t<double, py::array::c_style | py::array::forcecast> M_in)
{
    auto buf = M_in.request();
    std::size_t rows = static_cast<std::size_t>(buf.shape[0]);
    std::size_t cols = static_cast<std::size_t>(buf.shape[1]);
    const double *M = static_cast<const double *>(buf.ptr);

    py::array_t<double> MT_out({cols, rows});
    auto tbuf = MT_out.request();
    double *MT = static_cast<double *>(tbuf.ptr);

    transpose_rm(M, MT, rows, cols);
    return MT_out;
}

py::array_t<double> matmul_np(py::array_t<double, py::array::c_style | py::array::forcecast> A_in,
                              py::array_t<double, py::array::c_style | py::array::forcecast> B_in)
{
    auto Ab = A_in.request();
    auto Bb = B_in.request();
    std::size_t n = static_cast<std::size_t>(Ab.shape[0]);
    std::size_t p = static_cast<std::size_t>(Ab.shape[1]);
    std::size_t m = static_cast<std::size_t>(Bb.shape[1]);

    const double *A = static_cast<const double *>(Ab.ptr);
    const double *B = static_cast<const double *>(Bb.ptr);

    py::array_t<double> C_out({n, m});
    auto Cb = C_out.request();
    double *C = static_cast<double *>(Cb.ptr);

    matmul_rm(A, B, C, n, p, m);
    return C_out;
}

PYBIND11_MODULE(linalg_kernels, m)
{
    m.doc() = "Row-major double* kernels: cholesky_upper, transpose, matmul (pybind11)";
    m.def("cholesky_upper", &cholesky_upper_np, "Compute U (upper) using the provided algorithm");
    m.def("transpose", &transpose_np, "Transpose (row-major)");
    m.def("matmul", &matmul_np, "Matrix multiply C = A*B");
}
