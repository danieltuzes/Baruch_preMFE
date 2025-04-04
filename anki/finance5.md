# Finance

## What is a negative binomial distribution?

<!-- notecardId: 1743806008203 -->

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

## What is the Jensen's inequality?

<!-- notecardId: 1743806008208 -->

Let $f$ a convex function and $p_i \geq 0$ with $\sum_{i=1}^{n} p_i = 1$. Then:
$$f\left( \sum_{i=1}^{n} p_i x_i \right) 
\leq 
\sum_{i=1}^{n} p_i f(x_i)$$
$$f\left( \mathbb{E}[X] \right) \leq \mathbb{E}[f(X)]$$
and equality holds if and only if $x_1 = x_2 = \ldots = x_n$ or $f$ is linear. If $f$ is concave, the inequality is reversed.
