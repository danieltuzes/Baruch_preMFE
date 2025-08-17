library("Ecdat")
?CPSch3
data(CPSch3)
dimnames(CPSch3)[[2]]
male.earnings <- CPSch3[CPSch3[, 3] == "male", 2]


library("fGarch")
fitGED <- sgedFit(male.earnings, hessian = TRUE)
paramsGED <- fitGED$par
muGED <- paramsGED["mean"]
sigmaGED <- paramsGED["sd"]
nuGED <- paramsGED["nu"]
xiGED <- paramsGED["xi"] # Add this line to extract skewness

x <- seq(min(male.earnings), max(male.earnings), length.out = 500)
emp_density <- density(male.earnings)
fitted_density_GED <- dsged(x, mean = muGED, sd = sigmaGED, nu = nuGED, xi = xiGED)

pdf("fitted_vs_empirical_ged.pdf", width = 7, height = 5)
plot(density(male.earnings),
    main = "Empirical vs Fitted Skewed GED Density",
    xlab = "Earnings", ylab = "Density", lwd = 2
)
lines(x, fitted_density_GED, col = "blue", lwd = 2)
legend("topright",
    legend = c("Empirical", "Fitted skewed GED"),
    col = c("black", "blue"), lwd = 2
)

dev.off()
