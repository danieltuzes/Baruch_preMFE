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

## What does the continuity of probability mean?

$$
{A_1} \subseteq {A_2} \subseteq  \ldots  \Rightarrow P\left( {{A_1} \cup {A_2} \cup  \ldots } \right) = \mathop {\lim }\limits_{n \to \infty } P\left( {{A_n}} \right)
$$

$$
{A_1} \supseteq {A_2} \supseteq  \ldots  \Rightarrow P\left( {{A_1} \cap {A_2} \cap  \ldots } \right) = \mathop {\lim }\limits_{n \to \infty } P\left( {{A_n}} \right)
$$

## Show that $\sqrt N {\hat \mu _N} = \sqrt N \bar X = \frac{{{X_1} + {X_2} +  \ldots  + {X_N}}}{{\sqrt N }} \sim {\mathcal{N}}\left( {0,1} \right)$ and $N\left( {\overline {{X^2}}  - {{\bar X}^2}} \right) = N\widehat {{\sigma ^2}} \sim \chi _{n - 1}^2$ are independent

Let $\left( {\begin{array}{*{20}{c}}
  {{X_1}} \\ 
  {{X_2}} \\ 
   \vdots  \\ 
  {{X_N}} 
\end{array}} \right) = X$, $X_i, i\in \left\{1,2,\ldots,N\right\}$ be iid std normal random vars. Then $Y=QX$ is also std normal if $Q$ is an orthogonal matrix. Let

\[Q = \left( {\begin{array}{*{20}{c}}
  {\frac{1}{{\sqrt N }}}& \ldots &{\frac{1}{{\sqrt N }}} \\ 
  ?&?&? \\ 
  ?&?&? 
\end{array}} \right)\]

There are multiple ways to fill the matrix.
$$Y_1 = \frac{1}{{\sqrt N }}\sum_{i=1}^{N} X_i = \sqrt N \bar X \Rightarrow \bar X = Y_1/\sqrt N$$
Due to CLT, this is clearly std normal.
\[\begin{gathered}
  N\widehat {{\sigma ^2}}  = N\left( {\overline {{X^2}}  - {{\bar X}^2}} \right) = N\left( {\frac{{X_1^2 + X_2^2 +  \ldots X_N^2}}{N} - {{\left( {\frac{{{X_1} + {X_2} +  \ldots  + {X_N}}}{N}} \right)}^2}} \right) \hfill \\
  N\left( {\overline {{X^2}}  - {{\bar X}^2}} \right) = X_1^2 + X_2^2 +  \ldots X_N^2 - {\left[ {\frac{1}{{\sqrt N }}\left( {{X_1} + {X_2} +  \ldots  + {X_N}} \right)} \right]^2} \hfill \\
  N\left( {\overline {{X^2}}  - {{\bar X}^2}} \right) = Y_1^2 + Y_2^2 +  \ldots Y_N^2 - Y_1^2 = Y_2^2 + Y_3^2 +  \ldots Y_N^2 \hfill \\ 
\end{gathered} \]

$Y_i$ are all independent, $\bar X(Y_1)$ and $N\widehat {{\sigma ^2}}(Y_2,\ldots Y_N)$ are independent.

## What is the MFG of the normal distribution?

$$
M_X(t) = e^{\mu t + \frac{1}{2} \sigma^2 t^2}
$$

 