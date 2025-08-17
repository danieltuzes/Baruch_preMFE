data <- read.csv("../MCD_PriceDaily.csv")
adjPrice <- data[, 7]
LogRet <- diff(log(adjPrice))

library(MASS)
library(fGarch)

fit.T <- fitdistr(LogRet, "t")
params.T <- fit.T$estimate
mean.T <- params.T[1]
sd.T <- params.T[2] * sqrt(params.T[3] / (params.T[3] - 2))
nu.T <- params.T[3]

x <- seq(-0.04, 0.04, by = 0.0001)
pdf("mcd_price_LogHist_t.pdf", width = 6, height = 4) # size in inches
hist(LogRet, breaks = 80, freq = FALSE)
lines(x, dstd(x, mean = mean.T, sd = sd.T, nu = nu.T),
    lwd = 2, lty = 2, col = "red"
)
dev.off()
