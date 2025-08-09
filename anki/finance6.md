# Finance

## What is a gamma function, show its property

<!-- notecardId: 1751754951549 -->

By definition:
$$
\Gamma(n) = \int_0^\infty x^{n-1} e^{-x} \, dx
$$

$\Gamma(1) = \int_0^\infty e^{-x} \, dx = 1$

Using integration by parts, we can show the property of the gamma function:

$$
\begin{aligned}
\Gamma(n+1) &= \int_0^\infty x^n e^{-x} \, dx \\
           &= \left[ x^n \cdot (-e^{-x}) \right]_0^\infty - \int_0^\infty n x^{n-1} \cdot (-e^{-x}) \, dx \quad \\
           &= 0 + n \int_0^\infty x^{n-1} e^{-x} \, dx \\
           &= n \Gamma(n)
\end{aligned}
$$

## What is a gamma distribution

<!-- notecardId: 1751758252259 -->

$$
\Gamma(k) = \int_0^\infty t^{k-1} e^{-t} dt
$$

Turn this into a probability density by normalizing:

$$
f(x) = \frac{1}{\Gamma(k)} x^{k-1} e^{-x} \quad x > 0
$$

Now introduce a rate parameter $\lambda$ via change of variables:

Let $y = \lambda x \Rightarrow dy = \lambda dx$

Then:
$$
\begin{aligned}
f(x; k, \lambda)\,dx
&= f(y) \, dy \\
&= \frac{1}{\Gamma(k)} y^{k-1} e^{-y} \cdot dy \\
&= \frac{1}{\Gamma(k)} (\lambda x)^{k-1} e^{-\lambda x} \cdot \lambda  dx \\
&= \frac{\lambda^k}{\Gamma(k)} x^{k-1} e^{-\lambda x}  dx
\end{aligned}
$$

So the Gamma distribution is:

$$
f(x; k, \lambda) = \frac{\lambda^k}{\Gamma(k)} x^{k-1} e^{-\lambda x} \quad x > 0
$$

## What is the distribution of $Z^2$, where $Z \sim N(0, 1)$

<!-- notecardId: 1751758252265 -->

Let $Z \sim N(0,1)$ and $X = Z^2$. We compute the CDF:

$$
F_X(x) = \mathbb{P}(Z^2 \leq x) = \mathbb{P}(-\sqrt{x} \leq Z \leq \sqrt{x})
= \int_{-\sqrt{x}}^{\sqrt{x}} \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \, dz
$$

Differentiate using Leibniz's rule:

$$
\begin{aligned}
f_X(x) &= \frac{d}{dx} F_X(x) = f(\sqrt{x}) \cdot \frac{d}{dx} \sqrt{x} + f(-\sqrt{x}) \cdot \frac{d}{dx} \sqrt{x} \\
&= \frac{1}{\sqrt{2\pi}} e^{-x/2} \cdot \frac{1}{2\sqrt{x}} + \frac{1}{\sqrt{2\pi}} e^{-x/2} \cdot \frac{1}{2\sqrt{x}} \\
&= \frac{1}{\sqrt{2\pi x}} e^{-x/2}
\end{aligned}
$$

Rewrite as a Gamma PDF:

$$
f_X(x) = \frac{2^{1/2}}{\Gamma(1/2)} x^{-1/2} e^{-x/2}
= \frac{(1/2)^{1/2}}{\Gamma(1/2)} x^{(1/2)-1} e^{-x \cdot (1/2)}
$$

This matches the Gamma distribution with:
$$
k = \frac{1}{2}, \quad \lambda = \frac{1}{2}
$$

So:
$$
Z^2 \sim \text{Gamma}\left(\frac{1}{2}, \frac{1}{2}\right)
$$

## If $X_i \sim \text{Gamma}(\alpha_i, \lambda)$, what is $\sum_{i=1}^n X_i$

<!-- notecardId: 1751758506676 -->

The sum $S = \sum_{i=1}^n X_i$ has distribution:
$$
S \sim \text{Gamma}\left( \sum_{i=1}^n \alpha_i,\; \lambda \right)
$$

---

Step 1: MGF of Gamma distribution

For $X \sim \text{Gamma}(\alpha, \lambda)$, the moment-generating function is:

$$
\begin{aligned}
M_X(t) &= \mathbb{E}[e^{tX}] \\
&= \int_0^\infty e^{tx} \cdot \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x} dx \\
&= \frac{\lambda^\alpha}{\Gamma(\alpha)} \int_0^\infty x^{\alpha - 1} e^{-(\lambda - t)x} dx \\
&= \frac{\lambda^\alpha}{(\lambda - t)^\alpha} \cdot \frac{\Gamma(\alpha)}{\Gamma(\alpha)} \\
&= \left( \frac{\lambda}{\lambda - t} \right)^\alpha, \quad t < \lambda
\end{aligned}
$$

$$
\begin{aligned}
M_X(t) &= \mathbb{E}[e^{tX}] \\
&= \int_0^\infty e^{tx} \cdot \frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\lambda x}  dx \\
&= \frac{\lambda^\alpha}{\Gamma(\alpha)} \int_0^\infty x^{\alpha - 1} e^{-(\lambda - t)x} dx \qquad \text{Gamma}(\alpha, \lambda - t) = \int_0^{\infty}\frac{(\lambda - t)^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-(\lambda - t)x} dx \\
&= \frac{\lambda^\alpha}{\Gamma(\alpha)} \cdot \frac{\Gamma(\alpha)}{(\lambda - t)^\alpha} \\
&= \left( \frac{\lambda}{\lambda - t} \right)^\alpha, \quad t < \lambda
\end{aligned}
$$

---

Step 2: MGF of the sum

Let $X_i \sim \text{Gamma}(\alpha_i, \lambda)$, independent. Then:

$$
\begin{aligned}
M_S(t)
&= \mathbb{E}[e^{tS}] = \mathbb{E}\left[ e^{t(X_1 + \cdots + X_n)} \right] \\
&= \prod_{i=1}^n \mathbb{E}[e^{t X_i}] = \prod_{i=1}^n M_{X_i}(t) \\
&= \prod_{i=1}^n \left( \frac{\lambda}{\lambda - t} \right)^{\alpha_i} \\
&= \left( \frac{\lambda}{\lambda - t} \right)^{\sum_{i=1}^n \alpha_i}
\end{aligned}
$$

## How is the Fisher distribution defined

<!-- notecardId: 1751759482912 -->

The Fisher distribution, also known as the F-distribution, is defined as the ratio of two independent chi-squared variables divided by their respective degrees of freedom:

$$
Z\sim {{F}_{m,k}}\Leftrightarrow Z=\frac{X/k}{Y/m}\qquad X\sim \chi _{k}^{2}\quad Y\sim \chi _{m}^{2}
$$

## biased coin flip, expected length till we get $n$ consecutive T, give recursive formula

<!-- notecardId: 1751856198464 -->

Let $E_n$ be the expected number of flips to get $n$ consecutive tails. We can derive a recursive formula.

After having flipped $n-1$ tails, we have two cases:

1. We flip a tail (probability $p$): we have $n$ consecutive tails, so we stop.
2. We flip a head (probability $1-p$): we reset to 0, and need to get $n$ consecutive tails again.

$$
\begin{aligned}
E_n =& p \left(E_{n-1} + 1\right) + (1-p)\left(E_{n-1} + E_n + 1\right) \\
=&  \frac{E_{n-1}+1} p
\end{aligned}
$$

Note that $E_0 = 0$, $E_1 = \frac{1}{p}$, and $E_2 = \frac 1 p + \frac 1 {p^2}$. The general formula is:

$$
E_n = \frac{E_{n-1} + 1}{p} = \frac{1}{p^n} + \frac{1}{p^{n-1}} + \cdots + \frac{1}{p} = \frac{1 - p^{-(n+1)}}{1 - p^{-1}} = \frac{p^n - 1}{p^n (p - 1)}
$$

## People with index starting from 0 are sitting at a table and every $k$th person is eliminated, what is the index of the last person remaining? Give recursive formula and closed form for $k=2$

<!-- notecardId: 1751856198469 -->

Let $J(n)$ be the index of the last person remaining when there are $n$ people and every $k$th person is eliminated. The recursive formula is:

$$
J(n) = (J(n-1) + k) \mod n
$$

For $k=2$, we can see that if $n = 2^m$ for some integer $m$, then the last person remaining is at index 0. If $n$ is not a power of 2, we can express it as $n = 2^m + l$ where $l < 2^m$. The closed form for $k=2$ is:
$$
J(n) = 2l
$$

where $l = n - 2^m$ and $2^m$ is the largest power of 2 less than or equal to $n$.

## The probability that 2 players meet in the knockout match with $2^n$ participants

<!-- notecardId: 1751856198472 -->

Total number of matches:

- 1st round: $2^n / 2 = 2^{n-1}$
- 2nd round: $2^{n-1} / 2 = 2^{n-2}$
- $k$th round: $2^{n-k}$
- Final round: 1 match $= 2^0$
- Total matches: $2^{n-1} + 2^{n-2} + \ldots + 2^0 = 2^n - 1$

Number of ways to choose 2 players from $2^n$ participants is $\binom{2^n}{2} = \frac{2^n(2^n - 1)}{2}$.

The probability that 2 players meet in the knockout match is the same for every pair.

$$
P = \frac{2^n-1}{\binom{2^n}{2}} = \frac{2(2^n-1)}{2^n(2^n-1)} = \frac{2}{2^n}
$$

## binomial model with 1 step, $u=2$, $d=0.75$, $r=0.1$, $S_0=100$, $K=100$, price the call option

<!-- notecardId: 1751856198473 -->

Buy $\Delta$ shares of the stock and borrow $B$ at the risk-free rate $r$ to replicate the call option.

$$
\begin{aligned}
&\Delta \cdot 200 + B \cdot 1.1 = 100 \\
&\Delta \cdot 75 + B \cdot 1.1 = 0 \\
\Rightarrow &125 \Delta = 100 \Rightarrow \Delta = \frac{4}{5} \\
\Rightarrow &75 \cdot \frac{4}{5} + 1.1 B = 0 \Rightarrow B = -\frac{60}{1.1} \\
\Rightarrow &C_0 = \Delta S_0 + B = \frac{4}{5} \cdot 100 - \frac{60}{1.1} = \frac{280}{11}
\end{aligned}
$$

## 5 pirates with 100 coins distributing them, the oldest makes the proposal: if at least half of them agrees, they are distributed, otherwise the oldest is thrown overboard, restart. What is the distribution of coins?

<!-- notecardId: 1751856198475 -->

| # Pirates | A (1) | B (2) | C (3) | D (4) | E (5) |
| --------- | ----- | ----- | ----- | ----- | ----- |
| 1         | 100   |       |       |       |       |
| 2         | 100   | 0     |       |       |       |
| 3         | 99    | 0     | 1     |       |       |
| 4         | 98    | 0     | 1     | 0     |       |
| 5         | 97    | 0     | 1     | 0     | 1     |

## maximum number of regions formed by $n$ lines in the plane

<!-- notecardId: 1751856198477 -->

The 1st line divides the plane into 2 regions. Each subsequent line can intersect all previous lines, adding new regions. The intersections are in a finite range of the plane, zoom out, so all the intersections are in a single point. If we have $n$ lines and adding a new one, it can intersect all previous $n$ lines, creating $n+1$ new regions. In a table:

| Lines | Regions | new regions |
| ----- | ------- | ----------- |
| 0     | 1       | 1           |
| 1     | 2       | 1           |
| 2     | 4       | 2           |
| 3     | 7       | 3           |
| 4     | 11      | 4           |
| 5     | 16      | 5           |
| 6     | 22      | 6           |
| 7     | 29      | 7           |

## You have two eggs, and 100 storey building, you want to find the maximum storey from which they break, using minimum number of steps

<!-- notecardId: 1751945627060 -->

At each step $i$, we drop egg 1 from floor $n_i$. Let $d_i = n_i - n_{i-1}$ be the interval between drops (with $n_0 = 0$). If the egg breaks at step $i$, we must linearly check $d_i - 1$ floors with the second egg.

So the total number of drops in the worst case if egg 1 breaks at step $i$ is:

$$
\text{Worst-case drops} = i + d_i - 1
$$

To minimize the maximum number of drops, we equalize this expression for all $i$:

$$
i + d_i - 1 = T \quad \text{(constant)} \Rightarrow d_i = T - i + 1
$$

So the drop intervals are: $T, T - 1, T - 2, \dots, 1$

This covers:

$$
\sum_{i=1}^T d_i = \sum_{i=1}^T i = \frac{T(T+1)}{2} \geq 100 \Rightarrow T=14
$$

Thus, the minimal worst-case number of drops is **14**, with egg 1 dropped from floors:  
$14, 27, 39, 50, 60, 69, 77, 84, 90, 95, 99, 100$

| Drop #, $i$ | Floor $n_i$ | Step $d_i$ | Worst-case drops = $i + d_i - 1$ |
| ----------- | ----------- | ---------- | -------------------------------- |
| 1           | 14          | 14         | 14                               |
| 2           | 27          | 13         | 14                               |
| 3           | 39          | 12         | 14                               |
| 4           | 50          | 11         | 14                               |
| 5           | 60          | 10         | 14                               |
| 6           | 69          | 9          | 14                               |
| 7           | 77          | 8          | 14                               |
| 8           | 84          | 7          | 14                               |
| 9           | 90          | 6          | 14                               |
| 10          | 95          | 5          | 14                               |
| 11          | 99          | 4          | 14                               |
| 12          | 100         | 3          | 14                               |
| 13          | -           | 2          | 14 (unused)                      |
| 14          | -           | 1          | 14 (unused)                      |

## Which is bigger, $e^\pi$ or $\pi^e$?

<!-- notecardId: 1751945627064 -->

$$
\begin{aligned}
e^\pi >=<& \pi^e \\
\ln{e^\pi} >=<& \ln{\pi^e} \\
\frac {\ln e} e  >=<& \frac {\ln \pi} \pi
\end{aligned}
$$

Check the properties of $f(x) = \ln {\left(x\right)} /x$, is it increasing?

$$
\begin{aligned}
f'(x) = 1/x^2 -\ln\left(x\right)/x^2 >?& 0\\
1-\ln\left(x\right) >?& 0\\
1 >?& \ln\left(x\right) \\
\end{aligned}
$$

This holds if $x<e$, so $f(x)$ is increasing if $x<e$, and decreasing otherwise. $\pi > e$, so $f(x)$ is decreasing,

$$
\begin{aligned}
\frac {\ln e} e  > & \frac {\ln \pi} \pi \\
e^\pi >& \pi^e \\
\end{aligned}
$$

## How many ways can we tile a $2 \times n$ rectangle with $1 \times 2$ dominoes?

<!-- notecardId: 1751945627066 -->

Find the recursive formula for $T(n)$:

$$
T(n) = T(n-1) + T(n-2)
$$

Because we can place a domino vertically (leaving a $2 \times (n-1)$ rectangle) or horizontally (leaving a $2 \times (n-2)$ rectangle).

This is the Fibonacci sequence, with initial conditions $T(1) = 1$ and $T(2) = 2$.

## The value $v$ of a car is between 0 and 1000, uniformly distributed. We can make 1 bid $B$, and if $B>v$, we buy the car. We can sell that car at $1.5v$. What $B$ maximizes the profit? And if the $v$ is between 100 and 1000?

<!-- notecardId: 1751945627068 -->

The law of total probability:

$$
E_{\text{profit}} = P(B \leq v) \cdot E(\text{profit} | B \leq v) + P(\text{offer} > v) \cdot E(\text{profit} | B > v)
$$

$E(\text{profit} | B \leq v) = 0$ because we don't buy the car.

$$
\begin{aligned}
E(\text{profit} | B > v) =& E(1.5v - B| B > v) \\
=& 1.5E(v | B > v) - B \\
=& 1.5 \cdot 0.5 B - B = -0.25 B < 0
\end{aligned}
$$

So the expected profit is negative for any $B > 0$. The optimal bid is $B = 0$.

If $v \in [100, 1000]$, we can compute the expected profit:

$$
\begin{aligned}
E(\text{profit} | B > v)=& 1.5E(v | B > v) - B \\
=& 1.5 \cdot \frac{B + 100}{2} - B \\
=& 0.75B + 75 - B \\
=& -0.25B + 75
\end{aligned}
$$

The expected profit, if we get the car, is maximized when $B$ is as small as possible, but for the total profit, we need to consider the probability of getting the car, $P(B > v) = \frac{B - 100}{900}$:

$$
\begin{aligned}
E(\text{profit}) =& P(B > v) \cdot E(\text{profit} | B > v) \\
=& \frac{B - 100}{900} \cdot (-0.25B + 75) \\
=& \frac{-0.25B^2 + 100B -7500}{900} \\
\end{aligned}
$$

This is a 2nd degree polynomial, which is maximized at $-b / 2a$:
$$
B = \frac{100}{2 \cdot 0.25} = 200
$$

## When is an estimator asymptotically normal, and what is the standard error of the estimator?

<!-- notecardId: 1753676139902 -->

If

$$
\sqrt{n}(\hat{\theta} - \theta) \xrightarrow{d} N(0, \sigma_{\theta_0}^2)
$$

for some $\sigma_{\theta_0}^2 > 0$, then $\hat{\theta}$ is asymptotically normal, and $\sigma_{\theta_0}^2$ is the asymptotic variance of $\hat{\theta}$.

The **standard error** of the estimator $\hat{\theta}$ is $\sigma_{\theta_0}$.

## What does it mean that the MLE is consistent? Prove it!

<!-- notecardId: 1753676139911 -->

The MLE $\hat{\theta}$ is **consistent** if $\hat{\theta} \xrightarrow{p} \theta_0$.

Below, we show step 1, 2 and 3 are true, so step 4 follows.

$$
    \begin{array}{*{20}{c}}
  {{l}\left( \theta  \right)}&{\mathop {2 \to }\limits^p }&{\mathcal L\left( \theta  \right)} \\ 
  {1 \downarrow \max }&{}&{3 \downarrow \max } \\ 
  {\hat \theta }&{4\mathop  \to \limits^p }&{{\theta _0}} 
\end{array}
$$

1. The likelihood function $L(\theta) = \prod_{i=1}^n f(x_i | \theta)$ is maximized at $\hat{\theta}$. Then the log-likelihood function $l(\theta) = \ln L(\theta) = \sum_{i=1}^n \ln f(x_i | \theta)$ is also maximized at $\hat{\theta}$. We use the notation $f(x | \theta) = f_\theta(x)$ for the PDF of $X$ given $\theta$.
   The MLE $\hat{\theta}$ is defined as:
   $$\hat{\theta} = \arg\max_{\theta} l(\theta) = \arg\max_{\theta} \sum_{i=1}^n \ln f(x_i | \theta)$$
2. $\hat{\theta}$ also maximizes the normalized log-likelihood function $l_n(\theta) = \frac{l(\theta)}{n}$. By the LLN, $l_n(\theta) \xrightarrow{p} \mathbb{E}_{\theta_0}[\ln f(X | \theta)] = \int \ln f(x | \theta) f(x | \theta_0) dx := \mathcal{L}(\theta)$.
3. We show that $$\mathcal{L}(\theta) \le \mathcal{L}(\theta_0) \quad \forall \theta$$ i.e. so $\hat{\theta}$ maximizes $\mathcal{L}(\theta)$. By the Jensen's inequality, we have:
    $$
    \begin{aligned}
    {\mathbb{E}_{{\theta _0}}}\left( {\ln \left( {\frac{{{f_\theta }\left( x \right)}}{{{f_{{\theta _0}}}\left( x \right)}}} \right)} \right) \leqslant  & \ln \left( {{\mathbb{E}_{{\theta _0}}}\left( {\frac{{{f_\theta }\left( x \right)}}{{{f_{{\theta _0}}}\left( x \right)}}} \right)} \right) \\
    {\mathbb{E}_{{\theta _0}}}\left( {\ln \left( {{f_\theta }\left( x \right)} \right)} \right) - {\mathbb{E}_{{\theta _0}}}\left( {\ln \left( {{f_{{\theta _0}}}\left( x \right)} \right)} \right) \leqslant  & \ln \left( {\int {\frac{{{f_\theta }\left( x \right)}}{{{f_{{\theta _0}}}\left( x \right)}}{f_{{\theta_0}}}\left( x \right)dx} } \right) \\
    \mathcal{L}\left( \theta  \right) - \mathcal{L}\left( {{\theta _0}} \right) \leqslant  & \ln \left( {\int {{f_\theta }\left( x \right)dx} } \right) = \ln \left( 1 \right) = 0 \\
    \mathcal{L}\left( \theta  \right) \leqslant  & \mathcal{L}\left( {{\theta _0}} \right) \\
    \end{aligned}
    $$

## The def of the Fisher information and a practical formula calculating it

<!-- notecardId: 1753676139913 -->

Definition:
$$I(\theta_0) = \mathbb{E}_{\theta_0} \left[ \left(\frac{\partial}{\partial \theta} \ln f(X | \theta) \right)^2 \right]$$

A practical formula for calculating the Fisher information is:

$$
I({\theta _0}) =  - {\mathbb{E}_{{\theta _0}}}\left[ {{{\left. {\left( {\frac{{{\partial ^2}}}{{\partial {\theta ^2}}}\ln f\left( {X|\theta } \right)} \right)} \right|}_{\theta  = {\theta _0}}}} \right]
$$

$$
\begin{aligned}
  {\mathbb{E}_{{\theta _0}}}\left[ {{{\left. {\left( {\frac{{{\partial ^2}}}{{\partial {\theta ^2}}}\ln f\left( {X|\theta } \right)} \right)} \right|}_{\theta  = {\theta _0}}}} \right] =  & {\mathbb{E}_{{\theta _0}}}\left[ {{{\left. {\left( {\frac{\partial }{{\partial \theta }}\frac{{\frac{\partial }{{\partial \theta }}f\left( {X|\theta } \right)}}{{f\left( {X|\theta } \right)}}} \right)} \right|}_{\theta  = {\theta _0}}}} \right] \\
   =  & {\mathbb{E}_{{\theta _0}}}\left[ {{{\left. {\left( {\frac{{{{\left. {\left( {\frac{{{\partial ^2}}}{{\partial {\theta ^2}}}f\left( {X|\theta } \right)} \right)} \right|}_{\theta  = {\theta _0}}}}}{{{f_{{\theta _0}}}\left( {X|\theta } \right)}} - \frac{{{{\left( {\frac{\partial }{{\partial \theta }}f\left( {X|\theta } \right)} \right)}^2}}}{{{f^2}\left( {X|\theta } \right)}}} \right)} \right|}_{\theta  = {\theta _0}}}} \right] \\
   =  & \int {\frac{{{{\left. {\left( {\frac{{{\partial ^2}}}{{\partial {\theta ^2}}}f\left( {X|\theta } \right)} \right)} \right|}_{\theta  = {\theta _0}}}}}{{{f_{{\theta _0}}}\left( {X|\theta } \right)}}{f_{{\theta _0}}}\left( {X|\theta } \right)dx}  - {\mathbb{E}_{{\theta _0}}}\left[ {{{\left. {\left( {{{\left( {\frac{{\frac{\partial }{{\partial \theta }}f\left( {X|\theta } \right)}}{{f\left( {X|\theta } \right)}}} \right)}^2}} \right)} \right|}_{\theta  = {\theta _0}}}} \right] \\ 
   =  & \frac{{{\partial ^2}}}{{\partial {\theta ^2}}}\int {{{\left. {\left( {f\left( {X|\theta } \right)} \right)} \right|}_{\theta  = {\theta _0}}}dx}  - {\mathbb{E}_{{\theta _0}}}\left[ {{{\left. {{{\left( {\frac{\partial }{{\partial \theta }}\left( {\ln f\left( {X|\theta } \right)} \right)} \right)}^2}} \right|}_{\theta  = {\theta _0}}}} \right] \\
   =  & 0 - I\left( {{\theta _0}} \right) \\
\end{aligned}
$$

## Fubini on integers and its proof

<!-- notecardId: 1753676139916 -->
$$E\left( M \right) = \sum\limits_{i = 0}^\infty  {P\left( {M > i} \right)} \quad M \ge 0$$
Continuous case:
$$ E\left( M \right) = \int\limits_0^\infty  {P\left( {M \geqslant x} \right)dx}\quad M>0$$

Proof:
$$
\begin{array}{*{20}{c}}
  \begin{aligned}
  E\left( M \right) =  & 1 \cdot P\left( {M = 1} \right) +  \\
   & 2 \cdot P\left( {M = 2} \right) +  \\
   &  \vdots  \\
   & n \cdot P\left( {M = n} \right) +  \\
   \vdots  \\
   \\
\end{aligned} &\begin{aligned}
  \qquad E\left( M \right) =  & P\left( {M = 1} \right) +  \\
   & P\left( {M = 2} \right) + P\left( {M = 2} \right) +\\
   &  \vdots  \\
   & P\left( {M = n} \right) + P\left( {M = n} \right) +  \ldots  + P\left( {M = n} \right) +\\
   &  \vdots  \\
   = & P\left( {M > 0} \right) + P\left( {M > 1} \right) +  \ldots  + P\left( {M > n - 1} \right) +  \ldots  \\
\end{aligned}  
\end{array}
$$

## Tower property of expectation and its proof

<!-- notecardId: 1753676139919 -->

$$E\left( {E\left( {X|\mathcal{G}} \right)|\mathcal{F}} \right) = E\left( {X|\mathcal{F}} \right)$$
where $\mathcal{F} \subseteq \mathcal{G}$. Proof:
$E\left( {E\left( {X|\mathcal{G}} \right)|\mathcal{F}} \right): = E\left( {Z|\mathcal{F}} \right)$ so we want to prove that $E\left( {Z|\mathcal{F}} \right) = E\left( {X|\mathcal{F}} \right)$.

Prove it by contradiction:

1. $E\left( {Z|\mathcal{F}} \right) \neq E\left( {X|\mathcal{F}} \right) \Leftrightarrow \exists A \in \mathcal{F}$ such that $E\left( {Z \cdot I_A} \right) \neq E\left( {X \cdot I_A} \right)$. We show that such $A$ cannot exist.
2. $\mathcal{F} \subseteq \mathcal{G}$, so $A \in \mathcal{G}$ too.
3. $Z = E\left( {X|\mathcal{G}} \right)$, we must have $E\left( {Z \cdot I_B} \right) = E\left( {X \cdot I_B} \right)$ for all $B \in \mathcal{G}$.
4. but we have found a set $A \in \mathcal{F} \subseteq \mathcal{G}$ such that $E\left( {Z \cdot I_A} \right) \neq E\left( {X \cdot I_A} \right)$, which is a contradiction to point 3.

## Prove that $E\left( {X|{\mathcal{F}}} \right) = X$ if $\sigma(X) \subseteq \mathcal{F}$

Recall the definition of conditional expectation:
$$E\left( {X|\mathcal{F}} \right) = Y \Leftrightarrow E\left( {{I_A}X} \right) = E\left( {{I_A}Y} \right){\text{ and }}\sigma \left( Y \right) \subseteq \mathcal{F}$$

So when does $X=Y$ hold?
$$E\left( {X|\mathcal{F}} \right) = X \Leftrightarrow E\left( {{I_A}X} \right) = E\left( {{I_A}X} \right){\text{ and }}\sigma \left( X \right) \subseteq \mathcal{F}$$

On the LHS,

1. the first condition always holds
2. the second condition holds if $\sigma(X) \subseteq \mathcal{F}$, which is true by assumption.

## Prove that $E\left( {X|{\mathcal{F}}} \right) = E\left( {X} \right)$ if $\sigma(X)$ and $\mathcal{F}$ are independent

The definition of conditional expectation is:

$$E\left( {X|\mathcal{F}} \right) = Y \Leftrightarrow E\left( {{I_A}X} \right) = E\left( {{I_A}Y} \right){\text{ and }}\sigma \left( Y \right) \subseteq \mathcal{F}$$

Can we prove then that
$$E\left( {X|\mathcal{F}} \right) = E\left( X \right) \Leftrightarrow E\left( {{I_A}X} \right) = E\left( {{I_A}E\left( X \right)} \right){\text{ and }}\sigma \left( {E\left( X \right)} \right) \subseteq \mathcal{F}$$

On the LHS,

1. $$E\left( {{I_A}X} \right)\mathop  = \limits^? E\left( {{I_A}E\left( X \right)} \right) = \int_A {E\left( X \right)d\omega }  = E\left( X \right)P\left( A \right)$$ $$E\left( {{I_A}X} \right) = E\left( {{I_A}} \right)E\left( X \right) = P\left( A \right)E\left( X \right)$$
2. $\sigma \left( {E\left( X \right)} \right) \subseteq \mathcal{F}$ is true because $E\left( X \right)$ is a constant, so $\sigma(E(X))$ is trivial and contained in any $\sigma$-algebra.

## What is a quadratic martingale and its properties?

If $M_n$ is a martingale, then

$$Q_n := M_n^2 - \left[ M \right]_n$$ is a martingale, where $\left[ M \right]_n$ is the quadratic variation of $M_n$, $[M]_n := \sum_{k=1}^n \mathbb{E}[(\Delta M_k)^2 \mid \mathcal{F}_{k-1}]$.

$$\begin{aligned}
  {Q_n}\mathop  = \limits^?  & E\left( {{Q_{n + 1}}|{\mathcal{F}}_n} \right) \\ 
   =  & E\left( {{M_{n + 1}}^2 - \left[ M \right]_{n + 1}|{\mathcal{F}}_n} \right) \qquad  \text{use} \begin{array}{*{20}{c}}
  {{M_{n + 1}} = {M_n} + \Delta {M_{n + 1}}} \\ 
  \qquad{\left[ {{M_{n + 1}}} \right] = \left[ {{M_n}} \right] + \mathbb{E}[{{(\Delta {M_{n + 1}})}^2}|{\mathcal{F}}_n]} 
\end{array}\\
    = & E\left( {{M_n}^2 + 2{M_n}\Delta M_{n + 1} + \Delta M_{n + 1}^2 - \left[ M \right]_n - \Delta M_{n + 1}^2|{\mathcal{F}}_n} \right) \\
    = & M_n^2 + 2M_n E(\Delta M_{n + 1} | \mathcal{F}_n) - \left[ M \right]_n \\
    = & M_n^2 - \left[ M \right]_n
\end{aligned}$$

So yes, it is true that $Q_n$ is a martingale.

## What is a stopping time?

A random variable $T$ is a stopping time if 
$$\left\{ {T \leqslant t} \right\} \in {\mathcal{F}}_t\quad \forall t \geqslant 0$$
where $(\Omega, \mathcal{F}, P)$ is a probability space, and $\mathcal{F}_t$ is a filtration, i.e. a family of $\sigma$-algebras such that $\mathcal{F}_s \subseteq \mathcal{F}_t$ for $s \leq t$.

## What is a martingale?

$M_n$ is a martingale if:

1. $E[M_{n+1} | \mathcal{F}_n] = M_n$.
2. $M_n$ is adapted to the filtration $\mathcal{F}_n$ (a filtration is a family of $\sigma$-algebras that is increasing over time, i.e. $\mathcal{F}_s \subseteq \mathcal{F}_t$ for $s \leq t$).
3. $E[|M_n|] < \infty$,

## What is optional stopping theorem and in what cases it holds?

$$E\left( {{M_T}} \right) = {M_0}$$
holds if either of the following conditions is satisfied:

1. $P(T < C) = 1$ holds for some $C \in \mathbb{R}$.
2. $E(T) < \infty$ and $\exists C \in \mathbb{R}$ such that $E\left[ | M_{n+1} - M_n | \mathcal{F}_n \right] \leq C$ on the event $\{T > n\}$.
3. $\exists C \in \mathbb{R}$ such that $\left|M_{\min\left\{T,n\right\}} \right| \leq C$.

## 6 dice are rolled 6 times. Each time, we record the minimum of the 6 dice. What is the expected value of the maximum of these 6 minimums?

$${M_i} = \min \left\{ {{R_{i,1}},{R_{i,2}}, \ldots ,{R_{i,6}}} \right\}\quad i \in \left[ {0,6} \right],$$
where the minimum in the $i$th roll is $M_i$. The maximum of these minima is

$$M = \max \left\{ {M_1,M_2, \ldots ,M_6} \right\}$$

Using Fubini:

$$\begin{aligned}
  E\left( M \right) &  = P\left( {M > 0} \right) + P\left( {M > 1} \right) +  \ldots  + P\left( {M > 5} \right) + P\left( {M > 6} \right) +  \ldots  \\ 
   &  = \qquad 1\qquad  + P\left( {M > 1} \right) +  \ldots  + P\left( {M > 5} \right) + 0 +  \ldots  \\ 
\end{aligned}$$

$$\begin{aligned}
  P\left( {M > i} \right) =  & P\left( {\max \left\{ {{M_1},{M_2}, \ldots ,{M_6}} \right\} > i} \right) \\
   =  & 1 - P\left( {\max \left\{ {{M_1},{M_2}, \ldots ,{M_6}} \right\} \leqslant i} \right) \\
   =  & 1 - P\left( {{M_1} \leqslant i,{M_2} \leqslant i, \ldots ,{M_6} \leqslant i} \right) \\
   =  & 1 - P\left( {{M_1} \leqslant i} \right)P\left( {{M_2} \leqslant i} \right) \cdot  \ldots  \cdot \left( {{M_6} \leqslant i} \right) \\
   =  & 1 - P{\left( {{M_1} \leqslant i} \right)^6} \\
   =  & 1 - P{\left( {\min \left\{ {{R_{1,1}},{R_{1,2}}, \ldots ,{R_{1,6}}} \right\} \leqslant i} \right)^6} \\
   =  & 1 - {\left( {1 - P\left( {\min \left\{ {{R_{1,1}},{R_{1,2}}, \ldots ,{R_{1,6}}} \right\} > i} \right)} \right)^6} \\
   =  & 1 - {\left( {1 - P\left( {{R_{1,1}} > i} \right)P\left( {{R_{1,2}} > i} \right) \cdot  \ldots  \cdot P\left( {{R_{1,6}} > i} \right)} \right)^6} \\
   =  & 1 - {\left( {1 - {{\left( {1 - \frac{i}{6}} \right)}^6}} \right)^6} \\
\end{aligned}$$

So we have:
$$E\left( M \right) = 1 + \sum\limits_{i = 1}^5 {P\left( {M > i} \right)}  = 1 + \sum\limits_{i = 1}^5 {1 - {{\left( {1 - {{\left( {1 - \frac{i}{6}} \right)}^6}} \right)}^6}}  = 6 - \sum\limits_{j = 1}^5 {{{\left( {1 - {{\left( {\frac{j}{6}} \right)}^6}} \right)}^6}}$$