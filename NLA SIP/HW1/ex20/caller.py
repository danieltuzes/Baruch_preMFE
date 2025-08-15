# run_cholesky.py
# Usage:
#   python run_cholesky.py -A A.csv -U U.csv --verify --L L.csv
# Install once:
#   pip install numpy pybind11 cppimport

import argparse
import numpy as np
import cppimport  # compiles linalg_kernels.cpp on first import

kern = cppimport.imp("linalg_kernels")  # builds a binary extension, then imports it


def main():
    ap = argparse.ArgumentParser(description="Run Cholesky (upper) via C++ kernels")
    ap.add_argument(
        "-A", default="A.csv", help="input matrix file (CSV) [default: A.csv]"
    )
    ap.add_argument("-U", default="U.csv", help="output U file (CSV) [default: U.csv]")
    ap.add_argument("--L", default="", help="optional output L=U^T file (CSV)")
    ap.add_argument(
        "--verify", action="store_true", help="check A ≈ (U^T) * U and print error"
    )
    args = ap.parse_args()

    # Load A
    A = np.loadtxt(args.A, delimiter=",", dtype=np.float64)

    # Compute U using C++ (no checks)
    U = kern.cholesky_upper(A)

    # Save U
    np.savetxt(args.U, U, delimiter=",", fmt="%.12f")

    # Optionally save L = U^T
    if args.L:
        L = kern.transpose(U)
        np.savetxt(args.L, L, delimiter=",", fmt="%.12f")

    # Optional verification (helpful for sanity)
    if args.verify:
        L = kern.transpose(U)
        Arec = kern.matmul(L, U)
        err = np.linalg.norm(A - Arec, ord="fro")
        print(f"‣ Frobenius error ||A - L*U||_F = {err:.6e}")


if __name__ == "__main__":
    main()
