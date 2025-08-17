# Load packages and data
library(Ecdat)
library(fGarch)

data(EuStockMarkets)
Y <- diff(log(EuStockMarkets[, 4])) # DAX

# Fit skewed Student-t distribution
fit <- sstdFit(Y, hessian = TRUE)
params <- fit$estimate
mu <- params["mean"]
sigma <- params["sd"]
nu <- params["nu"]
xi <- params["xi"]

# KDE
kde <- density(Y)

# Grid for fitted density
x_grid <- seq(min(Y), max(Y), length.out = 1000)
fitted_density <- dsstd(x_grid, mean = mu, sd = sigma, nu = nu, xi = xi)

# Plot
plot(kde,
    main = "KDE and Fitted Skewed t-Density",
    xlab = "Return", ylab = "Density", lwd = 2
)
lines(x_grid, fitted_density, col = "blue", lwd = 2)
legend("topright",
    legend = c("KDE", "Fitted Skewed t"),
    col = c("black", "blue"), lwd = 2
)
