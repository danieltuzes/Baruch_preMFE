# Load libraries
library(Ecdat)
library(fGarch)

# Load DAX returns
Y <- diff(log(EuStockMarkets[, "DAX"]))

# Step 0: Fit symmetric t-distribution
loglik_std <- function(x) -sum(dstd(Y, x[1], x[2], x[3], log = TRUE))
start <- c(mean(Y), sd(Y), 4)
fit_std <- optim(
    start, loglik_std,
    method = "L-BFGS-B",
    lower = c(-0.1, 0.001, 2.1),
    upper = c(0.1, 1, 20), hessian = TRUE
)
mu <- fit_std$par[1]
sigma <- fit_std$par[2]
nu <- fit_std$par[3]

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

# Step 6: KDE and fitted t-density
kde <- density(Y)
t_density_grid <- dstd(y_grid, mean = mu, sd = sigma, nu = nu)

# Step 7: Plot both panels
pdf("tkde_full_and_zoomed.pdf", width = 7, height = 8)
par(mfrow = c(2, 1), mar = c(4, 4, 2, 1))

# Full range plot
plot(kde,
    main = "Full Range: KDE, Fitted t, TKDE", xlab = "Return",
    ylim = range(c(kde$y, fY, t_density_grid))
)
lines(y_grid, t_density_grid, col = "blue", lwd = 2)
lines(y_grid, fY, col = "red", lwd = 2)
legend("topright",
    legend = c("KDE", "Fitted t", "TKDE"),
    col = c("black", "blue", "red"), lwd = 2, bty = "n"
)

# Zoomed plot on linear y-axis
# Define x-zoom interval
x_lower <- 0.035
x_upper <- 0.06

# Select points in the zoom range
kde_mask <- kde$x >= x_lower & kde$x <= x_upper
tkde_mask <- y_grid >= x_lower & y_grid <= x_upper

# Compute y-range from all three curves within x limits
y_vals_zoom <- c(
    kde$y[kde_mask],
    t_density_grid[tkde_mask],
    fY[tkde_mask]
)
y_range_zoom <- range(y_vals_zoom)

# Plot with x zoom and dynamic y limits
plot(kde,
    main = "Zoomed In: 0.035 < x < 0.06", xlab = "Return",
    xlim = c(x_lower, x_upper), ylim = y_range_zoom
)
lines(y_grid, t_density_grid, col = "blue", lwd = 2)
lines(y_grid, fY, col = "red", lwd = 2)
legend("topright",
    legend = c("KDE", "Fitted t", "TKDE"),
    col = c("black", "blue", "red"), lwd = 2, bty = "n"
)


dev.off()
