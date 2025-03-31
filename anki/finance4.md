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

## What is lagrange multiplier?

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

- For symmetric matrices, eigenvectors for different eigenvalues are orthogonal.
- The algebraic multiplicity equals the geometric multiplicity so we can always find a complete set of orthogonal eigenvectors.
- Thus, every symmetric matrix can be diagonalized by an orthogonal matrix.

## A robot performs fair coin tossing. Scientist A has 80% chance of successfully predicting the outcome, while the scientist B is successful 60% of the time. Scientist A predicts the coin will land tails, scientist B predicts the coin will land heads. What is the probability that the coin will land heads?

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

