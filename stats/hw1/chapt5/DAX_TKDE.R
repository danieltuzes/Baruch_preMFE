# Load data and library
data(Garch, package = "Ecdat")
library(fGarch)
data(EuStockMarkets)
Y <- diff(log(EuStockMarkets[, 1])) # DAX log returns

# Fit symmetric t-distribution to Y
loglik_std <- function(x) -sum(dstd(Y, x[1], x[2], x[3], log = TRUE))
start <- c(mean(Y), sd(Y), 4)
fit_std <- optim(start, loglik_std,
    method = "L-BFGS-B",
    lower = c(-0.1, 0.001, 2.1),
    upper = c(0.1, 1, 20), hessian = TRUE
)
par_std <- fit_std$par
mu <- par_std[1]
sigma <- par_std[2]
nu <- par_std[3]

# Step 1: Transform Y to Z = Φ⁻¹(F(Y))
Fy <- pstd(Y, mean = mu, sd = sigma, nu = nu)
Z <- qnorm(Fy)

# Step 2: KDE in Z-space (standard normal)
dens_Z <- density(Z)
z_grid <- dens_Z$x
fz <- dens_Z$y

# Step 3: Inverse transform: y = g⁻¹(z) = qstd(pnorm(z))
y_grid <- qstd(pnorm(z_grid), mean = mu, sd = sigma, nu = nu)

# Step 4: Compute g'(y)
gprime_num <- dstd(y_grid, mean = mu, sd = sigma, nu = nu)
Fy_grid <- pstd(y_grid, mean = mu, sd = sigma, nu = nu)
g_y <- qnorm(Fy_grid)
gprime_den <- dnorm(g_y)
gprime <- gprime_num / gprime_den

# Step 5: TKDE density
fY <- fz * gprime

# Step 6: Empirical KDE
emp_kde <- density(Y)

# Step 7: Restrict x-range
xlim <- c(-0.06, 0.06)
keep_kde <- emp_kde$x >= xlim[1] & emp_kde$x <= xlim[2]
keep_tkde <- y_grid >= xlim[1] & y_grid <= xlim[2]

# Step 8: Plot both on same PDF
pdf("TKDE_DAX.pdf", width = 7, height = 8)
par(mfrow = c(2, 1), mar = c(4, 4, 3, 2))

# Top plot: linear y-scale
plot(emp_kde$x[keep_kde], emp_kde$y[keep_kde],
    type = "l", lwd = 2,
    xlab = "Log Return (Y)", ylab = "Density", xlim = xlim,
    main = "KDE vs TKDE (Linear Scale)"
)
lines(y_grid[keep_tkde], fY[keep_tkde], col = "red", lty = 2, lwd = 2)
legend("topright",
    legend = c("KDE", "TKDE"),
    col = c("black", "red"), lwd = 2, lty = c(1, 2)
)

# Bottom plot: log y-scale
plot(emp_kde$x[keep_kde], emp_kde$y[keep_kde],
    type = "l", lwd = 2, log = "y",
    xlab = "Log Return (Y)", ylab = "Density (log scale)", xlim = xlim,
    main = "KDE vs TKDE (Log Y Scale)"
)
lines(y_grid[keep_tkde], fY[keep_tkde], col = "red", lty = 2, lwd = 2)
legend("topright",
    legend = c("KDE", "TKDE"),
    col = c("black", "red"), lwd = 2, lty = c(1, 2)
)

dev.off()
