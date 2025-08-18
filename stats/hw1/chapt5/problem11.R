data <- read.csv("../MCD_PriceDaily.csv")
adjPrice <- data[, 7]
LogRet <- diff(log(adjPrice))

library(MASS)
library(fGarch)

fit.T <- fitdistr(LogRet, "t")
vcov_mat <- fit.T$vcov
se_mu <- sqrt(vcov_mat["m", "m"]) # standard error of mean
cat("Standard error of the mean:", se_mu, "\n")

mu <- fit.T$estimate["m"]
z <- mu / se_mu
pval <- 2 * pnorm(-abs(z))

cat("z =", z, "\np =", pval, "\n")
