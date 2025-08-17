# Load data
library(Ecdat)
data(EuStockMarkets)
log_ret <- diff(log(EuStockMarkets[, "DAX"]))
n <- length(log_ret)

# Grid of theoretical probabilities
q_grid <- (1:n) / (n + 1)

# Sorted sample
sorted_data <- sort(log_ret)

# Degrees of freedom to compare
df_values <- c(4, 5, 6)

# Function to compute line through 25th and 75th percentiles
qq_abline <- function(theoretical, sample) {
    q_theo <- quantile(theoretical, probs = c(0.25, 0.75))
    q_sample <- quantile(sample, probs = c(0.25, 0.75))
    slope <- diff(q_sample) / diff(q_theo)
    intercept <- q_sample[1] - slope * q_theo[1]
    abline(intercept, slope, col = "red", lwd = 2)
}

# Plot
pdf("qqplots_normal_t_iqr.pdf", width = 8, height = 10)
par(mfrow = c(3, 2), mar = c(4, 4, 2, 1))

# Q-Q: Normal
theo_norm <- qnorm(q_grid)
qqplot(theo_norm, sorted_data,
    main = "Q-Q Plot: Normal",
    xlab = "Theoretical Quantiles",
    ylab = "Sample Quantiles"
)
qq_abline(theo_norm, sorted_data)

# Q-Q: t-distributions
for (df in df_values) {
    theo_t <- qt(q_grid, df)
    qqplot(theo_t, sorted_data,
        main = paste("Q-Q Plot: t, df =", df),
        xlab = "Theoretical Quantiles",
        ylab = "Sample Quantiles"
    )
    qq_abline(theo_t, sorted_data)
}

dev.off()




# Sample data (e.g., DAX log returns)
x <- diff(log(EuStockMarkets[, "DAX"]))
n <- length(x)

# 1. Compute excess kurtosis
library(e1071)
kurt <- kurtosis(x, type = 2) # type=2 gives excess kurtosis (normal = 0)

# 2. Compute standard error of excess kurtosis
se_kurt <- sqrt(24 * n * (n - 1)^2 / ((n - 3) * (n - 2) * (n + 3) * (n + 5)))

# 3. Compute test statistic (z-score)
z <- kurt / se_kurt

# 4. Compute two-sided p-value
pval <- 2 * pnorm(-abs(z))

# 5. Output results
cat(sprintf("Excess kurtosis: %.5f\n", kurt))
cat(sprintf("Standard error: %.5f\n", se_kurt))
cat(sprintf("z-statistic: %.5f\n", z))
cat(sprintf("p-value: %.5f\n", pval))
