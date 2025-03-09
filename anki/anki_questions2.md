# finance

## What is a Poisson distribution? Show that it is a distribution, and what its mean and variance are.

<!-- notecardId: 1741404376410 -->

A Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space, given that these events occur with a known constant mean rate and independently of the time since the last event.

The probability mass function (PMF) of a Poisson distribution is given by:
$$ P_\lambda(X = k) = e^{-\lambda} \frac{\lambda^k }{k!} $$

For each of the $k$ it is non-negative, and the sum of all probabilities is 1:
$$ \sum_{k=0}^{\infty} P_\lambda(X = k) = \sum_{k=0}^{\infty} e^{-\lambda} \frac{\lambda^k }{k!} = e^{-\lambda} \sum_{k=0}^{\infty} \frac{\lambda^k }{k!} = e^{-\lambda} e^{\lambda} = 1 $$

The mean:
$$ E(X) = \sum_{k=0}^{\infty} k P_\lambda(X = k) = \sum_{k=0}^{\infty} k e^{-\lambda} \frac{\lambda^k }{k!} = e^{-\lambda} \lambda \sum_{k=0}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} = e^{-\lambda} \lambda e^{\lambda} = \lambda $$
The variance:
$$ E(X(X-1)) = \sum_{k=0}^{\infty} k(k-1) P_\lambda(X = k) = \sum_{k=0}^{\infty} k(k-1) e^{-\lambda} \frac{\lambda^k }{k!} = e^{-\lambda} \lambda^2 \sum_{k=0}^{\infty} \frac{\lambda^{k-2}}{(k-2)!} = e^{-\lambda} \lambda^2 e^{\lambda} = \lambda^2 $$
$$ E(X(X-1)) = E(X^2) - E(X) = \lambda^2 \Rightarrow E(X^2) = \lambda^2 + \lambda $$
$$ Var(X) = E(X^2) - E(X)^2 = \lambda^2 + \lambda - \lambda^2 = \lambda $$

## What is a binomial distribution? Given parameters $n$ and $p$, show that it is a distribution, and what its mean and variance are.

A binomial distribution is a discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials, each with the same probability of success.
The probability mass function (PMF) of a binomial distribution is given by:
$$ P_{n,p}(X = k) = \binom{n}{k} p^k (1-p)^{n-k} $$
It is a distribution because for each of the $k$ it is non-negative, and the sum of all probabilities is 1:
$$ \sum_{k=0}^{n} P_{n,p}(X = k) = \sum_{k=0}^{n} \binom{n}{k} p^k (1-p)^{n-k} = (p + (1-p))^n = 1 $$
The mean:
$$ E(X) = E\left(\sum_{i=1}^{n} X_i\right) = \sum_{i=1}^{n} E(X_i) = \sum_{i=1}^{n} p = np $$
The variance:
$$ Var(X) = Var\left(\sum_{i=1}^{n} X_i\right) = \sum_{i=1}^{n} Var(X_i) = \sum_{i=1}^{n} p(1-p) = np(1-p)$$

## What is a geometric distribution? Given parameter $p$, show that it is a distribution, and what its mean and variance are.

A geometric distribution is a discrete probability distribution that models the number of Bernoulli trials needed to get the first success. The probability mass function (PMF) of a geometric distribution is given by:
$$ P_p(X = k) = p(1-p)^{k-1} $$
It is a distribution because for each of the $k$ it is non-negative, and the sum of all probabilities is 1:
$$ \sum_{k=1}^{\infty} P_p(X = k) = \sum_{k=1}^{\infty} p(1-p)^{k-1} = p \sum_{k=0}^{\infty} (1-p)^k = p \frac{1}{p} = 1 $$
The mean:
$$ E(X) = \sum_{k=1}^{\infty} k P_p(X = k) = \sum_{k=1}^{\infty} k p(1-p)^{k-1} = p \sum_{k=0}^{\infty} (k+1)(1-p)^k = p \frac{1}{p^2} = \frac{1}{p} $$

## What is a chi-square distribution? How is it used for testing? What is its mean and variance?

$$ X_k=\chi_k^2 = \sum_{i=1}^{k} Z_i^2 $$
where $Z_i$ are independent standard normal variables.

$$ E\left(X_k\right) = \sum_{i=1}^{k} \underbrace{E\left(Z_i^2\right)}_{\underbrace{Var(Z_i)}_1 + \underbrace{E(Z_i)^2}_0} = k $$
$$ Var\left(X_k\right) = \sum_{i=1}^{k} \underbrace{Var\left(Z_i^2\right)}_{\underbrace{E\left(Z_i^4\right)}_{3} - \underbrace{E\left(Z_i^2\right)^2}_1} = 2k $$

The chi-square distribution is used for testing the independence of two categorical variables in a contingency table, and for goodness-of-fit tests to see if a sample comes from a population with a specific distribution.
The chi-square test statistic is calculated as:
$$ \chi^2 = \sum_{i=1}^{k} \frac{(O_i - E_i)^2}{E_i} $$
where $O_i$ is the observed frequency and $E_i$ is the expected frequency,
and $i$ is the index of the category.

## What is a t-distribution? How is it used for testing? What is its mean and variance?

It is defined as the distribution of the ratio of a standard normal variable and the square root of a chi-square variable divided by its degrees of freedom:
$$ T_k = \frac{Z}{\sqrt{\frac{X_k}{k}}} $$
where $Z$ is a standard normal variable and $X_k$ is a chi-square variable with $k$ degrees of freedom.

This is the same as:
$$ T_{k-1} = \frac{\sum_{i=1}^{k} Z_i}{ \sigma\sqrt{k}} $$
where $Z_i$ are independent standard normal variables, and $\sigma$ is the unbiased standard deviation of the population, $\sigma^2 = \frac{1}{k-1} \sum_{i=1}^{k} (Z_i)^2$.

## When is a probability-measure?

A function $P$ is a probability measure if

- $P(\Omega)= 1$ 
- $P(A_i) \ge 0$
- $P\left( \biguplus_{i=1}^{\infty} A_i \right) = \sum_{i=1}^{\infty} P(A_i).$
 
## What is the characteristic function, what is it good for, and how to get the PDF?

$$\varphi_X(t) = \mathbb{E}[e^{itX}] = \int_{-\infty}^{\infty} e^{itx} f_X(x) \,dx$$
Useful to calculate the sum of independent vars:
$$\varphi_{X+Y}(t) = \varphi_X(t) \varphi_Y(t)$$
$$f_X(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} e^{-itx} \varphi_X(t) dt$$

## What is Cauchy-distribution

A Cauchy-distribution centered at 0 has a PDF:
$${f_X} \propto \frac{1}{{{c_1} + {x^2}}}$$

Its mean and variance are undefined.

## What is the conditional expected value and its properties?

A random variable $Y$ is called a **conditional expectation** of $X$ given $\mathcal{F}$, symbolically $\mathbb{E}[X \mid \mathcal{F}] := Y$, if:

1. $Y$ is $\mathcal{F}$-measurable.
2. For any $A \in \mathcal{F}$, we have  
   $$ \mathbb{E}[X \mathbf{1}_A] = \mathbb{E}[Y \mathbf{1}_A]. $$

Let $(\Omega, \mathcal{A}, \mathbb{P})$ be a probability space, and let $X$ be an integrable random variable. Let $\mathcal{G} \subseteq \mathcal{F} \subseteq \mathcal{A}$ be $\sigma$-algebras, and let $Y \in L^1(\Omega, \mathcal{A}, \mathbb{P})$. Then:

1. **(Linearity)**  
   $$ \mathbb{E}[\lambda X + Y \mid \mathcal{F}] = \lambda \mathbb{E}[X \mid \mathcal{F}] + \mathbb{E}[Y \mid \mathcal{F}]. $$

2. **(Monotonicity)** If $X \geq Y$ almost surely, then  
   $$ \mathbb{E}[X \mid \mathcal{F}] \geq \mathbb{E}[Y \mid \mathcal{F}]. $$

3. If $\mathbb{E}[|XY|] < \infty$ and $Y$ is measurable with respect to $\mathcal{F}$, then  
   $$ \mathbb{E}[XY \mid \mathcal{F}] = Y \mathbb{E}[X \mid \mathcal{F}], \quad \text{and} \quad \mathbb{E}[Y \mid \mathcal{F}] = \mathbb{E}[Y \mid Y] = Y. $$

4. **(Tower Property)**  
   $$ \mathbb{E}[\mathbb{E}[X \mid \mathcal{F}] \mid \mathcal{G}] = \mathbb{E}[X \mid \mathcal{G}]. $$

5. **(Triangle Inequality)**  
   $$ \mathbb{E}[|X| \mid \mathcal{F}] \geq |\mathbb{E}[X \mid \mathcal{F}]|. $$

6. **(Independence)** If $X$ is independent of $\mathcal{F}$, then  
   $$ \mathbb{E}[X \mid \mathcal{F}] = \mathbb{E}[X]. $$

7. If $\mathbb{P}[A] \in \{0,1\}$ for any $A \in \mathcal{F}$, then  
   $$ \mathbb{E}[X \mid \mathcal{F}] = \mathbb{E}[X]. $$

8. **(Dominated Convergence Theorem)** Assume $Y \in L^1(\mathbb{P})$, $Y \geq 0$, and let $(X_n)_{n \in \mathbb{N}}$ be a sequence of random variables such that $|X_n| \leq Y$ for all $n \in \mathbb{N}$ and  
   $$ X_n \xrightarrow{n \to \infty} X \quad \text{a.s.} $$  
   Then,  
   $$ \lim_{n \to \infty} \mathbb{E}[X_n \mid \mathcal{F}] = \mathbb{E}[X \mid \mathcal{F}] $$  
   almost surely and in $L^1(\mathbb{P})$.

## Why is the conditional expectation the best estimator?

We consider the candidate estimator $ Z = \mathbb{E}[X \mid \mathcal{G}] + W $, where $W $ is some $\mathcal{G}$-measurable adjustment term. Substituting this into the MSE:

$$\mathbb{E}[(X - Z)^2] = \mathbb{E}[(X - (\mathbb{E}[X \mid \mathcal{G}] + W))^2]$$
$$\mathbb{E}[(X - \mathbb{E}[X \mid \mathcal{G}])^2 - 2 W (X - \mathbb{E}[X \mid \mathcal{G}]) + W^2]$$

Using the **orthogonality property** of conditional expectation:

$$\mathbb{E}[(X - \mathbb{E}[X \mid \mathcal{G}]) W] = 0 \quad \text{for any } W \text{ that is } \mathcal{G}\text{-measurable}$$

$$\mathbb{E}[(X - Z)^2] = \mathbb{E}[(X - \mathbb{E}[X \mid \mathcal{G}])^2] + \mathbb{E}[W^2]$$

## Why is a random walk a martingale?

A random walk is a martingale because its expected future value, given the past, is equal to its current value. Mathematically, if we define a simple symmetric random walk as:

$$
X_n = X_{n-1} + Z_n
$$

where $Z_n$ are independent and identically distributed (i.i.d.) random variables with mean zero, then we have:

$$
E[X_n \mid X_{n-1}, X_{n-2}, \dots, X_0] = X_{n-1} + E[Z_n] = X_{n-1}
$$

Since $E[Z_n] = 0$, it follows that:

$$
E[X_n \mid \mathcal{F}_{n-1}] = X_{n-1}
$$

where $\mathcal{F}_{n-1}$ is the filtration representing all information up to time $n-1 $. This satisfies the martingale property:

$$
E[X_n \mid \mathcal{F}_{n-1}] = X_{n-1}
$$

Thus, a random walk is a martingale.

## What is a filtration in probability theory? How is it related to adaptation?

A **filtration** is a sequence of $\sigma$-algebras $\{\mathcal{F}_t\}_{t \geq 0}$ that represents the information available over time. It satisfies:

1. **Increasing property**: If $s \leq t$, then $\mathcal{F}_s \subseteq \mathcal{F}_t$, meaning that as time progresses, more information is available.
2. **Adaptation**: A stochastic process $\{X_t\}$ is said to be adapted to a filtration $\{\mathcal{F}_t\}$ if $X_t$ is $\mathcal{F}_t$-measurable for each $t$.

Filtrations are used to formalize the concept of evolving information in probability and finance.
