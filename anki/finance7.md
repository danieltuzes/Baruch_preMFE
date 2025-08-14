# Finance

## What is the expected number of random numbers generated from a continuous or discrete distribution till the generated number is not the maximum?

<!-- notecardId: 1754446392381 -->

Discrete case:
Let the random numbers 0 and 1. The squence ends when we get 0, prepended by any number of 1s, and optionally preprended by any number of 0s. So the order:

1. some 0s till we get the first 1 -> geometric distribution with the argument of probability of the 1s, $p_1$.
2. some 1s till we get the first 0 -> geometric distribution with the argument of probability of the 0s, $p_0$, which is $1 - p_1$.

$$
E = \frac{1}{p_1} + \frac{1}{p_0} = \frac{1}{p_1} + \frac{1}{1 - p_1}
$$

Continuous case:
Only the order of numbers matters. Only 1 ordering is accepted, the monotonic increasing order, and we can order $n$ numbers in $n!$ number of ways. Use Fubini on discrete case for expected value:

$$
\begin{aligned}
E(N) & = \sum_{n=0}^{\infty} P(N > n) \\
& = P(N > 0) + P(N > 1) + P(N > 2) + ... \\
&= 1 + \frac{1}{1!} + \frac{1}{2!} + ... = e
\end{aligned}
$$

## Show that the convolution is the product in the Fourier space

## Prove that the sum of 2 independent normal random vars is normal

## Let $X$, $Y$ and $Z$ be independent standard normal random vars. What is the distribuion of $\frac{X+YZ}{1+Z^2}$?

## What is a Jordan-block? What is its eigenvalue and eigenvector?

## Why a matrix and its transpose has the same eigenvalues?

## Why is the determinant and the trace of the matrix can be calculated from the eigenvalues only?
