import numpy as np
import math
from typing import List
import pandas as pd


def matrix_multiply(A: List[List[float]], B: List[List[float]]) -> List[List[float]]:
    """
    Multiplies two matrices A and B.

    Parameters
    ----------
    A : List[List[float]]
        The first matrix with dimensions (m, n).
    B : List[List[float]]
        The second matrix with dimensions (n, p).

    Returns
    -------
    List[List[float]]
        The result of matrix multiplication with dimensions (m, p).

    Raises
    ------
    ValueError
        If the number of columns in A is not equal to the number of rows in B.

    Notes
    -----
    This function assumes that A and B are two-dimensional matrices represented
    as lists of lists, with float values.

    Examples
    --------
    >>> A = [[1, 2, 3], [4, 5, 6]]
    >>> B = [[7, 8], [9, 10], [11, 12]]
    >>> matrix_multiply(A, B)
    [[58.0, 64.0], [139.0, 154.0]]
    """
    # Check if multiplication is possible
    if len(A[0]) != len(B):
        raise ValueError(
            "Number of columns in A must be equal to number of rows in B")

    # Dimensions of the result matrix
    m, n, p = len(A), len(A[0]), len(B[0])

    # Initialize the result matrix with zeros
    result = [[0.0 for _ in range(p)] for _ in range(m)]

    # Perform matrix multiplication
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]

    return result


def std_from_covariance_matrix(cov_matrix: List[List[float]]) -> List[float]:
    """
    Calculates the standard deviation vector from a covariance matrix.

    Parameters
    ----------
    cov_matrix : List[List[float]]
        A square covariance matrix (n x n).

    Returns
    -------
    List[float]
        The vector of standard deviations for each variable.

    Raises
    ------
    ValueError
        If the covariance matrix is not square.
    """
    n = len(cov_matrix)

    # Check if the covariance matrix is square
    if any(len(row) != n for row in cov_matrix):
        raise ValueError("Covariance matrix must be square (n x n).")

    # Calculate the standard deviation for each variable from the diagonal elements (variances)
    return [math.sqrt(cov_matrix[i][i]) for i in range(n)]


def inverse_diagonal(diag_vector: List[float]) -> List[float]:
    """
    Calculates the inverse of a diagonal matrix represented as a vector.

    Parameters
    ----------
    diag_vector : List[float]
        A list of non-zero values representing the diagonal elements of the matrix.

    Returns
    -------
    List[float]
        A list representing the inverse of the diagonal matrix.

    Raises
    ------
    ValueError
        If any element in the diag_vector is zero, as the inverse would be undefined.

    Examples
    --------
    >>> diag_vector = [4.0, 9.0, 16.0]
    >>> inverse_diagonal(diag_vector)
    [0.25, 0.1111111111111111, 0.0625]
    """
    # Check for zeros in the diagonal vector
    if any(value == 0 for value in diag_vector):
        raise ValueError(
            "All elements in the diagonal vector must be non-zero.")

    # Calculate the inverse of each diagonal element
    inverse_vector = [1.0 / value for value in diag_vector]

    return inverse_vector


def diagonal_matrix_from_vector(diag_vector: List[float]) -> List[List[float]]:
    """
    Converts a vector into a diagonal matrix.

    Parameters
    ----------
    diag_vector : List[float]
        A list of values representing the diagonal elements of the matrix.

    Returns
    -------
    List[List[float]]
        A diagonal matrix where the elements of diag_vector form the diagonal.

    Examples
    --------
    >>> diagonal_matrix_from_vector([2.0, 3.0, 4.0])
    [[2.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 4.0]]
    """
    n = len(diag_vector)
    return [[0.0 if i != j else diag_vector[i] for j in range(n)] for i in range(n)]


def covariance_to_correlation(cov_matrix: List[List[float]]) -> List[List[float]]:
    """
    Calculates the correlation matrix given a covariance matrix.

    Parameters
    ----------
    cov_matrix : List[List[float]]
        A square covariance matrix (n x n).

    Returns
    -------
    List[List[float]]
        The corresponding correlation matrix (n x n).

    Raises
    ------
    ValueError
        If the covariance matrix is not square.

    Examples
    --------
    >>> cov_matrix = [
    ...     [4.0, 2.0, 1.0],
    ...     [2.0, 9.0, 3.0],
    ...     [1.0, 3.0, 16.0]
    ... ]
    >>> covariance_to_correlation(cov_matrix)
    [
        [1.0, 0.3333333333333333, 0.125],
        [0.3333333333333333, 1.0, 0.1875],
        [0.125, 0.1875, 1.0]
    ]
    """
    # Calculate the standard deviation vector from the covariance matrix
    std_vector = std_from_covariance_matrix(cov_matrix)

    # Get the inverse of the standard deviation vector
    inverse_std_vector = inverse_diagonal(std_vector)

    # Convert the inverse standard deviation vector into a diagonal matrix form
    inverse_std_matrix = diagonal_matrix_from_vector(inverse_std_vector)

    # Multiply inverse_std_matrix with the covariance matrix
    intermediate_result = matrix_multiply(inverse_std_matrix, cov_matrix)

    # Multiply the intermediate result with the inverse_std_matrix again to get the final correlation matrix
    corr_matrix = matrix_multiply(intermediate_result, inverse_std_matrix)

    return corr_matrix


def correlation_to_covariance(corr_matrix: List[List[float]], std_vector: List[float]) -> List[List[float]]:
    """
    Calculates the covariance matrix given a correlation matrix and a standard deviation vector.

    Parameters
    ----------
    corr_matrix : List[List[float]]
        A square correlation matrix (n x n).
    std_vector : List[float]
        A list of standard deviations for each variable.

    Returns
    -------
    List[List[float]]
        The corresponding covariance matrix (n x n).

    Raises
    ------
    ValueError
        If the correlation matrix is not square or if the dimensions of the std_vector
        do not match the dimensions of the correlation matrix.

    Examples
    --------
    >>> corr_matrix = [
    ...     [1.0, 0.5, 0.2],
    ...     [0.5, 1.0, 0.3],
    ...     [0.2, 0.3, 1.0]
    ... ]
    >>> std_vector = [2.0, 3.0, 4.0]
    >>> correlation_to_covariance(corr_matrix, std_vector)
    [[4.0, 3.0, 1.6], [3.0, 9.0, 3.6], [1.6, 3.6, 16.0]]
    """
    n = len(corr_matrix)

    # Check if the correlation matrix is square
    if any(len(row) != n for row in corr_matrix):
        raise ValueError("Correlation matrix must be square (n x n).")

    # Check if the length of the standard deviation vector matches the dimensions of the correlation matrix
    if len(std_vector) != n:
        raise ValueError(
            "Length of the standard deviation vector must match the dimensions of the correlation matrix.")

    # Create the diagonal matrix from the standard deviation vector
    std_matrix = diagonal_matrix_from_vector(std_vector)

    # Multiply std_matrix with the correlation matrix and then again with std_matrix
    intermediate_result = matrix_multiply(std_matrix, corr_matrix)
    cov_matrix = matrix_multiply(intermediate_result, std_matrix)

    return cov_matrix


def calculate_log_returns_df(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the daily log returns for each column in a given DataFrame.

    Parameters
    ----------
    input_df : pd.DataFrame
        A DataFrame containing end-of-day values for stock indices.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the daily log returns for each stock index.
    """
    # Calculate daily log returns
    log_returns = np.log(input_df / input_df.shift(1))

    return log_returns


def df_to_list_of_lists(df: pd.DataFrame) -> List[List[float]]:
    """
    Converts a pandas DataFrame into a list of lists.

    Parameters
    ----------
    df : pd.DataFrame
        The input DataFrame.

    Returns
    -------
    List[List[float]]
        A list of lists where each inner list corresponds to a column of the DataFrame.
    """
    return df.values.tolist()


def compute_covariance_matrix(data: List[List[float]]) -> List[List[float]]:
    """
    Computes the sample covariance matrix of the given data without using numpy.

    Parameters
    ----------
    data : List[List[float]]
        A list of lists where each inner list represents a time series (column) of data.

    Returns
    -------
    List[List[float]]
        The covariance matrix computed with degrees of freedom equal to len(data[0]) - 1.
    """
    # Number of observations (rows) and number of variables (columns)
    n = len(data)
    m = len(data[0]) if n > 0 else 0

    # Calculate the mean for each column
    means = [sum(data[i][j] for i in range(n)) / n for j in range(m)]

    # Center the data by subtracting the mean from each element
    centered_data = [[data[i][j] - means[j]
                      for j in range(m)] for i in range(n)]

    # Initialize the covariance matrix
    covariance_matrix = [[0.0 for _ in range(m)] for _ in range(m)]

    # Calculate the covariance matrix using the formula
    for i in range(m):
        for j in range(m):
            covariance_sum = sum(
                centered_data[k][i] * centered_data[k][j] for k in range(n))
            covariance_matrix[i][j] = covariance_sum / (n - 1)

    return covariance_matrix


def calculate_percentage_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates the daily percentage returns for each column in the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        A DataFrame containing end-of-day values for stock indices.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the daily percentage returns for each stock index.
    """
    # Calculate daily percentage returns using the formula (current - previous) / previous * 100
    percentage_returns = (df / df.shift(1) - 1) * 100

    return percentage_returns


def exc8_9():
    """Do exercise 8 and 9 from 1st home assignment."""
    cov_matrix = [
        [1, -0.525, 1.375, -0.075, -0.75],
        [-0.525, 4, 0.1875, 0.1875, -0.675],
        [1.375, 0.1875, 12.25, 0.4375, -1.875],
        [-0.075, 0.1875, 0.4375, 6.25, 0.3],
        [-0.75, -0.675, -1.875, 0.3, 4.41]
    ]

    print(std_from_covariance_matrix(cov_matrix))
    print(inverse_diagonal(std_from_covariance_matrix(cov_matrix)))

    corr_matrix = covariance_to_correlation(cov_matrix)

    print(pd.DataFrame(corr_matrix))

    corr_matrix_input = [
        [1.0, -0.25, 0.15, -0.05, -0.30],
        [-0.25, 1.0, -0.10, -0.25, 0.10],
        [0.15, -0.10, 1.0, 0.20, 0.05],
        [-0.05, -0.25, 0.20, 1.0, 0.10],
        [-0.30, 0.10, 0.05, 0.10, 1.0]
    ]
    std_vector_input = [0.1, 0.2, 0.5, 1.0, 2.0]
    cov_matrix_result = correlation_to_covariance(
        corr_matrix_input, std_vector_input)

    print(pd.DataFrame(cov_matrix_result))

    std_vector_input = [2.0, 1.0, 0.5, 0.2, 0.1]
    cov_matrix_result = correlation_to_covariance(
        corr_matrix_input, std_vector_input)

    print(pd.DataFrame(cov_matrix_result))


def exc10():
    """Do exercise 10 from home assignment 1."""

    # Assuming the Excel file is uploaded and we have the path to it
    file_path = "NLA homework/indeces-close-jan3-jan31-2017.xlsx"
    # Calculate daily log returns using the function
    end_of_day_values_df = end_of_day_values_df = pd.read_excel(
        file_path, index_col=0, parse_dates=True)
    daily_log_returns_df = calculate_log_returns_df(end_of_day_values_df)
    log_returns_list = df_to_list_of_lists(
        daily_log_returns_df.dropna())

    print(pd.DataFrame(daily_log_returns_df))

    # Compute the covariance matrix using the function without numpy
    computed_covariance_matrix = compute_covariance_matrix(
        log_returns_list)
    print(pd.DataFrame(computed_covariance_matrix))

    # Calculate the daily percentage returns correctly
    daily_percentage_returns_df = calculate_percentage_returns(
        end_of_day_values_df)
    print(daily_percentage_returns_df)

    computed_covariance_matrix = compute_covariance_matrix(
        df_to_list_of_lists(daily_percentage_returns_df.dropna()))
    print(pd.DataFrame(computed_covariance_matrix))


def exc11():
    # Assuming the Excel file is uploaded and we have the path to it
    file_path = "NLA homework/indices-july2016.csv"
    # Calculate daily log returns using the function
    end_of_day_values = pd.read_csv(file_path, index_col=0, parse_dates=True)

    datas = {"daily": end_of_day_values,
             "weekly": end_of_day_values.resample("W").apply("first"),
             "monthly": end_of_day_values.resample("ME").apply("first")}

    for frequency, end_of_period in datas.items():
        print(frequency)
        # Calculate the daily percentage returns correctly
        perc_returns_df = calculate_percentage_returns(end_of_period)
        perc_returns_list = df_to_list_of_lists(perc_returns_df.dropna())

        covariance_matrix = compute_covariance_matrix(perc_returns_list)
        print("from perc returns")
        print("covariance matrix")
        print(pd.DataFrame(covariance_matrix))
        correlation_matrix = covariance_to_correlation(covariance_matrix)
        print("correlation matrix")
        print(pd.DataFrame(correlation_matrix))

        log_returns_df = calculate_log_returns_df(end_of_period)
        log_returns_list = df_to_list_of_lists(log_returns_df.dropna())
        # Compute the covariance matrix using the function without numpy
        covariance_matrix = compute_covariance_matrix(log_returns_list)
        print("from log returns")
        print("covariance matrix")
        print(pd.DataFrame(covariance_matrix))
        correlation_matrix = covariance_to_correlation(covariance_matrix)
        print("correlation matrix")
        print(pd.DataFrame(correlation_matrix))


if __name__ == "__main__":
    exc11()
