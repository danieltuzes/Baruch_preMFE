# Finance

## What is bagging in terms of decision trees? What is random forest?

<!-- notecardId: 1742768765244 -->

**Bagging** (short for *bootstrap aggregating*) is an ensemble technique used to improve the performance and stability of machine learning models, especially **decision trees**.

---

### Concept

The idea is to reduce **variance** by training multiple models on different random subsets of the data and then averaging their outputs (for regression) or using majority voting (for classification).

---

### Steps

1. Given a training set with $n$ samples:  
   $$D = \{(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)\}$$

2. For $B$ iterations (e.g., $B = 100$):
   - Sample $n$ points *with replacement* from $D$ to create a **bootstrap sample** $D_b$
   - Train a decision tree $T_b$ on $D_b$

3. Aggregate the predictions:
   - **Regression**: average the outputs
     $$\hat{y}(x) = \frac{1}{B} \sum_{b=1}^B T_b(x)$$
   - **Classification**: majority vote
     $$\hat{y}(x) = \text{mode} \left( T_1(x), T_2(x), \ldots, T_B(x) \right)$$

---

### Why It Works

- Each tree is trained on a slightly different dataset, so it sees different patterns and makes different errors.
- Averaging reduces the variance compared to a single decision tree, which is prone to overfitting.
- Bagging **does not** reduce bias but significantly **reduces variance**.

---

### Bagging vs. Random Forest

- Bagging uses **entire feature space** for splits.
- Random Forest adds another layer of randomness by selecting a **random subset of features** at each split.

## What is Lagrange multiplier?

<!-- notecardId: 1743474280046 -->

For the optimization problem:

$$
\text{maximize/minimize} \quad f(x) \quad \text{subject to} \quad g_i(x) = 0 \quad (i = 1, \dots, m)
$$

The **Lagrangian** is:

$$
\mathcal{L}(x, \lambda) = f(x) - \sum_{i=1}^m \lambda_i g_i(x)
$$

**First-order necessary conditions:**

$$
\nabla_x \mathcal{L}(x, \lambda) = 0
$$
$$
g_i(x) = 0 \quad (i = 1, \dots, m)
$$

## Can every symmetric matrix be diagonalized?

<!-- notecardId: 1743474280054 -->

- For symmetric matrices, eigenvectors for different eigenvalues are orthogonal.
- The algebraic multiplicity equals the geometric multiplicity so we can always find a complete set of orthogonal eigenvectors.
- Thus, every symmetric matrix can be diagonalized by an orthogonal matrix.

## A robot performs fair coin tossing. Scientist A has 80% chance of successfully predicting the outcome, while the scientist B is successful 60% of the time. Scientist A predicts the coin will land tails, scientist B predicts the coin will land heads. What is the probability that the coin will land heads?

<!-- notecardId: 1743474280056 -->

$$
\begin{aligned}
\Pr(H \mid A=T, B=H) &= \frac{\Pr(A=T, B=H \mid H)\Pr(H)}{\Pr(A=T, B=H \mid H)\Pr(H) + \Pr(A=T, B=H \mid T)\Pr(T)} \\\\
&= \frac{(0.2)(0.6)(0.5)}{(0.2)(0.6)(0.5) + (0.8)(0.4)(0.5)} \\\\
&= \frac{0.06}{0.06 + 0.16} = \frac{3}{11} \approx 0.2727
\end{aligned}
$$

## There are $n$ passengers waiting to board the airplane. Each passenger has an assigned seat. However, the first passenger lost the ticket and forgot the seat number. The first passenger then decides to take a random seat.  Each subsequent passenger tries to sit in their assigned seat if it is available, otherwise chooses a random unoccupied seat. What is the probability that the last, $n$th passenger, will be able to sit in his/her assigned seat? For $k \in \{2, 3, \dots, n\}$, what is the probability that the $k$th passenger will be able to sit in his/her assigned seat?

The first passenger chooses their own seat and the last seat with equal probability. If they don't choose their own seat, but the $k$th passanger's seat, then all passanger till $k$ can sit in their assigned seats. When the $n$th passenger tries to sit down, they choose between the $1$st and $n$th seats with equal probability again, etc. When the $n$th comes, the probability that his seat is taken is $1/2$.

Before the last passenger, $k=n-1$: the last 2 seats and the 1st seats are taken with equal probability, so the chance that his seat has been taken is $1/3$ so he can sit in his assigned seat with probability $2/3 = \frac{n-k}{n-k+1}$ with $k=n-2$.

## When is a function measurable?

<!-- notecardId: 1743474280061 -->

a function $f: X \to Y$ is called *measurable* if for every set $B$ in the $\sigma$-algebra $\mathcal{N}$ on $Y$,

$$
f^{-1}(B) \in \mathcal{M}.
$$

Equivalently, if $Y = \mathbb{R}$ with the Borel $\sigma$-algebra, it suffices to check that

$$
\{\, x \in X : f(x) \le \alpha \} \in \mathcal{M}
\quad \text{for all } \alpha \in \mathbb{R}.
$$

## What is the expected number of runs in a deck of 2 colored cards? (A run is a maximal sequence of consecutive cards of the same color, e.g. RRBBR has 3 runs: RR, BB, R)

<!-- notecardId: 1743474280064 -->

Let $X$ be the number of runs in a deck of $52$ cards. We can express $X$ as the sum of indicator random variables:
$$
X = \sum_{i=2}^{52} I_i + 1
$$
where $I_i$ is an indicator variable that is 1 if the $i$-th card is different from the $(i+1)$-th card, and 0 otherwise. This means that a new run starts at position $i$ if the color of the $i$-th card is different from the $(i+1)$-th card.
The expected value of $X$ can be computed using the linearity of expectation:
$$
E[X] = E\left[\sum_{i=2}^{52} I_i\right] +1= \sum_{i=2}^{52} E[I_i]+1
$$
Now, we need to calculate $E[I_i]$. For each $i$, the probability that the $i$-th card is different from the $(i+1)$-th card is $\frac{1}{2}$, assuming there are only 2 colors (say Red and Blue). Therefore, we have:
$$
E[I_i] = P(I_i = 1) = P(\text{the } i\text{-th card is different from the } (i+1)\text{-th card}) = \frac{26}{51}
$$
Thus, we can substitute this back into our equation for $E[X]$:
$$
E[X] =  51\cdot\frac{26}{51} + 1 = 27
$$

## How to use PCA?

<!-- notecardId: 1743474280073 -->

We want to lower the dimensionality of the data while preserving as much variance as possible. The steps are:

1. **Standardize the data**: Center the data by subtracting the mean: $\tilde x_i = x_i - \sum_{j=1}^n x_j$.
2. **Compute the covariance matrix** on the centered data: $\Sigma = \sum_{i=1}^n \tilde x_i \tilde x_i^T / (n-1)$.
3. **Compute the eigenvalues and eigenvectors**: Find the eigenvalues and eigenvectors of the covariance matrix. It is because we want to find the directions of maximum variance after projecting the data onto a 1D space, which can be calculated by a scalar product with a direction vector $w$:
   $$ Var_{1\text D}(w) = w^T \Sigma w $$
   We want to maximize this with respect to $w$ given the constraint $||w||^2 = 1$. This is a Lagrange multiplier problem, we are looking for the maximum of the Lagrangian:
   $$ \mathcal{L}(w, \lambda) = w^T \Sigma w - \lambda (w^T w - 1) $$
   We need to use the operator $\nabla_w$ to find the stationary point of the Lagrangian:
   $$ \nabla_w \mathcal{L}(w, \lambda) = 2\Sigma w - 2\lambda w = 0 $$
   This gives us the eigenvalue equation $\Sigma w = \lambda w$. The eigenvalues are the variances of the projections onto the corresponding eigenvectors. The larger the eigenvalue, the more variance is explained by that direction.
4. **Sort the eigenvalues**: Sort the eigenvalues in descending order and select the top $k$ eigenvectors corresponding to the largest $k$ eigenvalues. This gives us the principal components.

## What are the properties of a covariance matrix and why?

<!-- notecardId: 1743474280076 -->

- **Symmetric**: $\Sigma = \Sigma^T$, as per definition.
- **Positive semi-definite**: For any vector $x$, $x^T \Sigma x \geq 0$:
Let $X-E(X) = \bar X$ be the centered data matrix. Then,

$$
x^T \Sigma x = x^T E[\bar X \bar X^T] x = E[x^T \bar X \bar X^T x] = E[(\bar X^T x)^2] \geq 0
$$

## Why does a matrix must be positive definite if it has a Cholesky decomposition?

<!-- notecardId: 1743474280078 -->

A matrix $A$ has a **Cholesky decomposition** if it can be expressed as $A = LL^T$, where $L$ is a lower triangular matrix with real and positive diagonal entries. This implies that $A$ is:

1. **Symmetric**: Since $A = LL^T$, it follows that $A^T = (LL^T)^T = L^TL = A$.
2. **Positive definite**: To show this, consider any non-zero vector $x \in \mathbb{R}^n$. We can express $x^T A x$ as follows:

   $$
   x^T A x = x^T (LL^T) x = (L^T x)^T (L^T x) = ||L^T x||^2 \geq 0
   $$

   The expression $||L^T x||^2$ is zero if and only if $L^T x = 0$, which implies $x = 0$ since $L$ has positive diagonal entries. Thus, $A$ is positive definite.

## What is a negative binomial distribution?

$P(\text{head}) = p$, and we toss a coin till we get $n$ heads. Let $X$ the number of tails.
$$f_X(k) = \underbrace{\binom{k+n-1}{k}}_{\substack{\text{\# ways to have }\\n{\text{ head, ending with head}}}}\cdot \underbrace{p^n(1-p)^k}_{\substack{\text{probability of getting }\\ n\text{ heads and }k\text{ tails}}}$$

## In the 1 time binomial model, price a European call option with strike $K$ and maturity $T$ on a stock with current price $S_0$. The stock can go up by a factor of $u$ or down by a factor of $d$ in the next time step. The risk-free interest rate is $r$. How about 2 periods?

$$C_0 \cdot (1+r) =  \left( p C_u + q C_d \right)$$


- $C_u = \max(S_0 u - K, 0)$
- $C_d = \max(S_0 d - K, 0)$
- $p = \frac{(1+r) - d}{u - d}$
- $q = 1 - p = \frac{u - (1+r)}{u - d}$

![binomial european graph](binomial_european_graph.png)

For 2 periods:
$$C\left( 0 \right)\cdot{{\left( 1+r \right)}^{2}}={{p}^{2}}C\left( {{u}^{2}} \right)+2pqC\left( u\cdot d \right)+{{q}^{2}}C\left( {{d}^{2}} \right)$$