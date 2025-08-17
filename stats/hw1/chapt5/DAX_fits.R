data(Garch, package = "Ecdat")
library("fGarch")
data(EuStockMarkets)
Y <- diff(log(EuStockMarkets[, 1])) # DAX

##### Fit symmetric t-distribution #####
loglik_std <- function(x) -sum(dstd(Y, x[1], x[2], x[3], log = TRUE))

start <- c(mean(Y), sd(Y), 4)
fit_std <- optim(start, loglik_std,
    method = "L-BFGS-B",
    lower = c(-0.1, 0.001, 2.1),
    upper = c(0.1, 1, 20), hessian = TRUE
)
par_std <- fit_std$par
AIC_std <- 2 * fit_std$value + 2 * length(par_std)
cat("Symmetric t MLE:", round(par_std, 5), "\tAIC =", round(AIC_std, 2), "\n")

##### Fit skewed t-distributions for 3 initial xi values #####
loglik_skewed_t <- function(x) {
    -sum(dsstd(Y,
        x[1], x[2], x[3], x[4],
        log = TRUE
    ))
}

# Store fits in list
xi_starts <- c(0.5, 1, 2)
fit_skewed_list <- list()
for (xi in xi_starts) {
    start_skewed <- c(par_std, xi)
    fit <- optim(start_skewed, loglik_skewed_t,
        method = "L-BFGS-B",
        lower = c(-0.1, 0.005, 2.1, 0.05),
        upper = c(0.1, 1, 50, 20),
        hessian = TRUE,
        control = list(
            fnscale = 1, maxit = 10000,
            trace = 0, factr = 1e3, pgtol = 1e-8
        )
    )
    fit_skewed_list[[as.character(xi)]] <- fit
    cat(
        "Skewed t (start xi =", xi, ") MLE:",
        round(fit$par, 5), "\tAIC =", round(2 * fit$value + 2 * 4, 2), "\n"
    )
}

###### Plot ######
pdf("DAX_fits.pdf", width = 8, height = 6)
x <- seq(-0.05, 0.05, length.out = 500)

# Empirical KDE
emp_density <- density(Y)
emp_x <- emp_density$x
emp_y <- emp_density$y
keep <- emp_x >= -0.05 & emp_x <= 0.05

# Densities
dens_std <- dstd(x, mean = par_std[1], sd = par_std[2], nu = par_std[3])
dens_skewed_list <- lapply(fit_skewed_list, function(fit) {
    p <- fit$par
    dsstd(x, mean = p[1], sd = p[2], nu = p[3], xi = p[4])
})

# Plot
plot(emp_x[keep], emp_y[keep],
    type = "l", log = "y",
    xlim = c(-0.05, 0.05),
    ylim = range(c(emp_y[keep], dens_std, unlist(dens_skewed_list))),
    main = "Log-Scale Density: Empirical vs Symmetric & Skewed t-Fits",
    xlab = "Log Returns", ylab = "Density", lwd = 2, col = "black"
)

lines(x, dens_std, col = "blue", lwd = 2, lty = 2)

cols <- c("red", "darkgreen", "orange")
lt <- c(3, 4, 5)
i <- 1
for (xi in xi_starts) {
    lines(x, dens_skewed_list[[as.character(xi)]],
        col = cols[i], lwd = 2, lty = lt[i]
    )
    i <- i + 1
}

legend("bottom",
    legend = c(
        "Empirical KDE", "Symmetric t-distribution",
        "Skewed t (start xi = 0.5)",
        "Skewed t (start xi = 1)", "Skewed t (start xi = 2)"
    ),
    col = c("black", "blue", cols),
    lwd = 2, lty = c(1, 2, lt)
)

dev.off()
