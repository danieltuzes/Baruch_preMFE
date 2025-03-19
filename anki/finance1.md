# finance

## What is a zero rate curve, instantanous rate, and forward rate?

<!-- notecardId: 1740882963117 -->

A **zero coupon rate** (aka spot rate), is the interest rate for a zero-coupon bond, which pays no coupons and only pays the face value at maturity.
$$B\left( t \right) = B\left( 0 \right){e^{r\left( {0,t} \right)t}}$$
The function $r(0,t)$ is the zero rate curve.

An **instantaneous rate** (aka short rate) is the interest rate at a specific point in time:
$$r\left( t \right) := \lim_{h \to 0} \frac{1}{h}\frac{B\left( t+h \right) - B\left( {t } \right)}{B\left( t \right)} = \frac{B'(t)}{B(t)}$$
Which is the same as:
$$r\left( t \right) := \lim_{\tau \to 0} \frac{r(0,t+\tau)(t+\tau) - r(0,t)t}{\tau} = \frac{d}{{dt}}\left( {r\left( {0,t} \right)t} \right)$$
Alternatively,
$$B(t) = B(0){e^{\int_0^t r (\tau )d\tau }} \Leftrightarrow r\left( {0,t} \right) = \frac{1}{t}\int\limits_0^t {r\left( \tau  \right)d\tau }$$

**Forward rate** $r(0; t_1, t_2)$ is the interest rate for a zero-coupon bond that matures at $t_2$ and is purchased at $t_1$.
$$r(0; t_1, t_2) = \frac{r(0, t_2)t_2 - r(0, t_1)t_1}{t_2 - t_1} = \int_{t_1}^{t_2} r(t) dt$$
It is the average of the instantaneous rate over the interval $[t_1, t_2]$.

## What is the present value of a bond that has a cash flow $c_i$ at time $t_i$?

<!-- notecardId: 1740882963119 -->

$$B\left( 0 \right) = \sum\limits_{i = 1}^n {c_i {e^{ - r\left( {0,t_i } \right)t_i }}}$$
Where $c_i$ is the cash flow at time $t_i$ and $r(0, t_i)$ is the zero rate curve.

## What is the yield of a bond, how does the value of a bond change with yield, and how do you calculate the yield of a bond?

<!-- notecardId: 1740882963121 -->

The yield of a bond $y$ is the constant interest rate $y$ for which the bond's market price $B$ is:
$$B = \sum\limits_{i = 1}^n {c_i {e^{ - y{t_i}}}}$$

The value of a bond is inversely related to its yield. As the yield increases, the value of the bond decreases, and vice versa:
$$\frac{{dB}}{{dy}} = -\sum\limits_{i = 1}^n {c_i t_i {e^{ - y{t_i}}}} < 0$$
The yield of a bond can be calculated using the Newton-Raphson method:
$$y_{n+1} = y_n - \frac{{B\left( {y_n } \right)}}{{B'\left( {y_n } \right)}}$$

## What is the coupon rate of a bond for an annually compounding and for a semi-annual compounding bond?

<!-- notecardId: 1740882963123 -->

The coupon rate $c$:
$$c = \frac{\text{annual coupon payment}}{\text{face value}}$$

## What is the par yield of a bond?

<!-- notecardId: 1740882963124 -->

The par yield $c_p$ is the coupon rate that makes the bond's present value equal to its face value:
$$F = F{e^{ - r\left( {0,T} \right)T}} + \sum\limits_i {F{c_p} \cdot {e^{ - r\left( {0,{t_i}} \right){t_i}}}} $$

## When is a bond on a par, premium, or discount?

<!-- notecardId: 1740882963126 -->

- a bond is on par if its price is equal to its face value
- a bond is on premium if its price is greater than its face value
- a bond is on discount if its price is less than its face value

## What is the adjusted duration of a bond, how it is related to the time to each cash flow?

<!-- notecardId: 1740882963128 -->

It is the sensitivity of the bond's value to changes in yield:

$$D = -\frac{1}{B}\frac{dB}{dy} = \frac{1}{B}\sum\limits_{i = 1}^n {c_i t_i {e^{ - y{t_i}}}}$$
Here, $B = \sum\limits_{i = 1}^n {c_i {e^{ - y{t_i}}}}$, so
$$D = \sum\limits_{i = 1}^n {{t_i}\frac{{{c_i}{e^{ - y{t_i}}}}}{B}}  = \sum\limits_{i = 1}^n {{t_i}{w_i}}$$
is a weighted average of the time to each cash flow.

## What is the convexity of a bond?

<!-- notecardId: 1740882963131 -->

It is the sensitivity of the bond's duration to changes in yield.
$$C = \frac{1}{B}\frac{d^2 B}{dy^2} = \frac{1}{B}\sum\limits_{i = 1}^n {c_i t_i^2 {e^{ - y{t_i}}}}$$

## Proof that the harmonic mean is less or equal to the arithmetic mean

<!-- notecardId: 1740882963133 -->

Let 2 vectors be $A_1 = \{\sqrt{a_1}, \sqrt{a_2}, \ldots, \sqrt{a_n}\}$ and $A_2 = \{\frac{1}{\sqrt{a_1}}, \frac{1}{\sqrt{a_2}}, \ldots, \frac{1}{\sqrt{a_n}}\}$.
Then
$${\left\| {{A_1}} \right\|^2} = \sum\limits_{i = 1}^n {a_i} \qquad {\left\| {{A_2}} \right\|^2} = \sum\limits_{i = 1}^n {\frac{1}{a_i}}$$
Using the Cauchy-Schwarz inequality ${\left\| {{A_1}} \right\|^2} \cdot {\left\| {{A_2}} \right\|^2} \geqslant {\left\| {{A_1} \cdot {A_2}} \right\|^2}$, we have:
$$\left( {\sum\limits_{i = 1}^n {a_i} } \right)\left( {\sum\limits_{i = 1}^n {\frac{1}{a_i}} } \right) \geqslant \left( {\sum\limits_{i = 1}^n {1} } \right)^2 = n^2$$
Thus,
$$\frac{1}{n}\sum\limits_{i = 1}^n {a_i} \ge \frac{n}{\sum\limits_{i = 1}^n {\frac{1}{a_i}} }$$
and equality holds if and only if $a_1 = a_2 = \ldots = a_n$. On the left side, we have the arithmetic mean, and on the right side, we have the harmonic mean. Thus, we have proved that the harmonic mean is less than or equal to the arithmetic mean.

## How much is the duration for a zero-coupon bond?

<!-- notecardId: 1740882963135 -->
Denoted by $D$,
$$D = \frac{1}{B}\sum\limits_{i = 1}^n {c_i t_i e^{ - r\left(0,t_i\right)t_i}} = \frac{1}{B}TF e^{ - r\left( {0,T} \right)T} = \frac{1}{B} T B = T$$

## Prove ${\left( {1 + \frac{1}{x}} \right)^x} < e < {\left( {1 + \frac{1}{x}} \right)^{x + 1}}$

<!-- notecardId: 1740882963137 -->

Left side:
$${\left( {1 + \frac{1}{x}} \right)^x} = {e^{\overbrace {\ln \left( {1 + \frac{1}{x}} \right)}^{\ln \left( {1 + y} \right) < y}x}} < {e^{\frac{1}{x}x}} = e$$

Right side:
$${\left( {1 + \frac{1}{x}} \right)^{x + 1}} > e\quad\text{for }x=1$$
If we can show that the derivative is negative, then we can conclude that the function is decreasing and thus the inequality holds for all $x\ge 1$.
$$\frac{d}{{dx}}{\left( {1 + \frac{1}{x}} \right)^{x + 1}} = \frac{d}{{dx}}{e^{\left( {x + 1} \right)\ln \left( {1 + \frac{1}{x}} \right)}} = {e^{\left( {x + 1} \right)\ln \left( {1 + \frac{1}{x}} \right)}}\underbrace {\left[ {\ln \left( {1 + \frac{1}{x}} \right) - \frac{{x + 1}}{{1 + \frac{1}{x}}}\frac{1}{{{x^2}}}} \right]}_{ \le 0?} \le 0?$$

$$\begin{aligned}
  \ln \left( {1 + \frac{1}{x}} \right)\mathop  < \limits^?  & \frac{{x + 1}}{{1 + \frac{1}{x}}}\frac{1}{{{x^2}}} = \frac{{x + 1}}{{\left( {x + 1} \right)x}} = \frac{1}{x}\quad x \leqslant 1 \\ 
  \ln \left( {1 + u} \right)\mathop  < \limits^?  & u\quad u \in [0,1] \\ 
  1 + u\mathop  < \limits^?  & {e^u} \\ 
\end{aligned} $$
Which is true for $u \in [0,1]$, so the right side inequality holds.

## How to create a one period market model for options market?

<!-- notecardId: 1741135566441 -->

Take some of the out-of-the-money options,
i.e. some put options with strike $K_i < S_0$
and some call options with strike $K_j > S_0$.
Select a call and put with the same strike $K$
closest to the spot price $S_0$.

Define possible future states of the world at maturity $T$
at spot values in the mean of the neighboring strike prices,
and one well below the lowest, and one well above the highest strike price.

- The number of options is $n$,
- the number of different strikes is $n-1$,
- the number of states is $n$.

Their payoffs at maturity are defined by
the option's strike and the spot price at maturity $S_T$,
denote it by $M$.
The options' current prices are known,
and we put them into a vector $C$. Then we can write the following system of equations with state price vector $Q$:
$$C = MQ$$
Here, the dimension of $C$ and $Q$ are $n$, and $M$ is $n \times n$.
Then we solve this for $Q$.

## What is F-test, and why is it better than t-test?

<!-- notecardId: 1741314235091 -->

Given two predictors $X_1$ and $X_2$ and a response $Y$,
we want to test if $X_1$ or $X_2$ is better at predicting $Y$.
The null hypothesis is that the two predictors are equally good at predicting $Y$.

F-test is better than t-test because it can test multiple predictors at once.
A t-test can only test one predictor at a time,
and doing multiple t-tests can lead to false positives.
While t-test tells us if a predictor is significant,
F-test tells us if a group of predictors is significant,
so it doesn't tell us which predictor is significant.

## What is the difference between Ridge and Lasso regression?

<!-- notecardId: 1741314235094 -->

Ridge and Lasso regression are both used to prevent overfitting in linear regression.
They both add a penalty term to the loss function.
In Ridge regression, the penalty term is the sum of the squares of the coefficients.
In Lasso regression, the penalty term is the sum of the absolute values of the coefficients.

$$J(\beta) = \sum_{i=1}^{n} (y_i - X_i \beta)^2 + \lambda \sum_{j=1}^{p} \beta_j^2$$

Ridge regression tends to shrink the coefficients towards zero,
but it doesn't set them exactly to zero.
Lasso regression tends to set some coefficients exactly to zero,
so it can be used for feature selection.

$$J(\beta) = \sum_{i=1}^{n} (y_i - X_i \beta)^2 + \lambda \sum_{j=1}^{p} |\beta_j|$$

## What is $Var(X+Y)$?

<!-- notecardId: 1741314403683 -->

$$Var(X+Y) = Var(X) + Var(Y) + 2Cov(X, Y)$$

## Prove that $-1 \le Corr(X, Y) \le 1$

<!-- notecardId: 1741314403686 -->

$$Var(X+cY) = Var(X) + c^2Var(Y) + 2cCov(X, Y) \ge 0$$
This is a quadratic function in $c$. For this to be always positive:
$$\Delta = 4Cov(X, Y)^2 - 4Var(X)Var(Y) \le 0$$
$$Cov(X, Y)^2 \le Var(X)Var(Y)$$
By dividing both sides by $Var(X)Var(Y)$, we have:
$$Corr(X, Y)^2 \le 1$$

## What is $Cov(X, Y + c\cdot Z)$?

<!-- notecardId: 1741314403689 -->

$$Cov(X, Y + c\cdot Z) = Cov(X, Y) + c\cdot Cov(X, Z)$$

## Let $Y = g(X)$ be a probability function of a random variable $X$. What is the probability density function of $Y$? Examples: $X \sim N(\mu,\sigma^2)$ and $Y = \exp(X)$; $X \sim U(-1,1)$ and $Y = X^2$; $X_1 \sim \exp(\lambda_1)$ and $X_2 \sim \exp(\lambda_2)$ and $Y = \begin{bmatrix} X_1+X_2 \\ X_1 - X_2 \end{bmatrix}$.

<!-- notecardId: 1741314626162 -->

$${f_Y}\left( y \right) = \sum\limits_{i = 1}^n {{f_X}\left( {{x_i}\left( y \right)} \right)\left| {\frac{d}{{dy}}{x_i(y)}{\text{ }}} \right|}$$

### example 1
$X \sim N(\mu,\sigma^2)$ and $Y = \exp(X)$
$$f_Y(y) = f_X(\ln(y))\left| \frac{d}{dy}\ln(y) \right| = f_X(\ln(y))\frac{1}{y}$$
$$f_Y(y) = \frac{1}{\sqrt{2\pi}\sigma y}\exp\left(-\frac{(\ln(y)-\mu)^2}{2\sigma^2}\right)$$

### example 2
$X \sim U(-1,1)$ and $Y = X^2$
$$f_Y(y) = f_X(\sqrt{y})\left| \frac{d}{dy}\sqrt{y} \right| + f_X(-\sqrt{y})\left| \frac{d}{dy}\left(-\sqrt{y}\right) \right| = \frac{1/2}{2\sqrt{y}} + \frac{1/2}{2\sqrt{y}} = \frac{1}{2\sqrt{y}}$$

### example 3
$X_1 \sim \exp(\lambda_1)$ and $X_2 \sim \exp(\lambda_2)$ and $Y = \begin{bmatrix} X_1+X_2 \\ X_1 - X_2 \end{bmatrix}$

$$Y(X) = \begin{bmatrix} X_1+X_2 \\ X_1 - X_2 \end{bmatrix} \Rightarrow X(Y) = \begin{bmatrix} \frac{Y_1+Y_2}{2} \\ \frac{Y_1-Y_2}{2} \end{bmatrix}$$
The absolute value of the Jacobian determinant is:
$$\left| \det \left(\frac{d}{dy}\begin{bmatrix} \frac{y_1+y_2}{2} \\ \frac{y_1-y_2}{2} \end{bmatrix} \right) \right|= \left|\det \begin{bmatrix} \frac{1}{2} & \frac{1}{2} \\ \frac{1}{2} & -\frac{1}{2} \end{bmatrix}\right| = \frac{1}{2}$$
So
$$f_Y(y) = f_X\left(\frac{y_1+y_2}{2}\right)f_X\left(\frac{y_1-y_2}{2}\right)\frac{1}{2}$$
$$f_Y(y) = \lambda_1\lambda_2\exp(-\lambda_1\frac{y_1+y_2}{2})\exp(-\lambda_2\frac{y_1-y_2}{2})\frac{1}{2}$$

Considering the domain of $Y$, we have:
$${x_1} \geqslant 0\quad {x_2} \geqslant 0\quad \Rightarrow \quad {y_1} = {x_1} + {x_2} \geqslant 0\quad {y_1} \geqslant {y_2} \geqslant - {y_1}$$