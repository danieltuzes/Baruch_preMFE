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
