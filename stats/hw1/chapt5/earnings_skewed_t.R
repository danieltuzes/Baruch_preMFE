library("Ecdat")
?CPSch3
data(CPSch3)
dimnames(CPSch3)[[2]]
male.earnings <- CPSch3[CPSch3[, 3] == "male", 2]

library("fGarch")
fit <- sstdFit(male.earnings, hessian = TRUE)
# Open PDF device
pdf("fitted_vs_empirical.pdf", width = 7, height = 5)

# Ensure single plot layout
par(mfrow = c(1, 1))

# Extract fitted parameters
params <- fit$estimate
mu <- params["mean"]
sigma <- params["sd"]
nu <- params["nu"]
xi <- params["xi"]

# Grid and densities
x <- seq(min(male.earnings), max(male.earnings), length.out = 1000)
emp_density <- density(male.earnings)
fitted_density <- dsstd(x, mean = mu, sd = sigma, nu = nu, xi = xi)

# Plot
plot(emp_density,
    main = "Empirical vs Fitted Skewed t Density",
    xlab = "Earnings", ylab = "Density", lwd = 2
)
lines(x, fitted_density, col = "red", lwd = 2)
legend("topright",
    legend = c("Empirical", "Fitted skewed t"),
    col = c("black", "red"), lwd = 2
)

# Close PDF device
dev.off()
