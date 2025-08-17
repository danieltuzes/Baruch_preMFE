library("Ecdat")
?CPSch3
data(CPSch3)
dimnames(CPSch3)[[2]]
male.earnings <- CPSch3[CPSch3[, 3] == "male", 2]
sqrt.male.earnings <- sqrt(male.earnings)
# raise to the power of 0.4
p03.male.earnings <- male.earnings^0.3
p04.male.earnings <- male.earnings^0.4
p06.male.earnings <- male.earnings^0.6
p07.male.earnings <- male.earnings^0.7

log.male.earnings <- log(male.earnings)

pdf("stats/1/chapt5/qqplots.pdf", width = 8, height = 10)
par(mfrow = c(4, 2))
qqnorm(male.earnings, datax = TRUE, main = "untransformed")
qqnorm(sqrt.male.earnings, datax = TRUE, main = "square-root transformed")
qqnorm(p03.male.earnings, datax = TRUE, main = "pow 0.3 transformed")
qqnorm(p04.male.earnings, datax = TRUE, main = "pow 0.4 transformed")
qqnorm(p06.male.earnings, datax = TRUE, main = "pow 0.6 transformed")
qqnorm(log.male.earnings, datax = TRUE, main = "log-transformed")
dev.off()

pdf("stats/1/chapt5/boxplots.pdf", width = 8, height = 10)
par(mfrow = c(4, 2))
boxplot(male.earnings, main = "untransformed")
boxplot(sqrt.male.earnings, main = "square-root transformed")
boxplot(p03.male.earnings, main = "pow 0.3 transformed")
boxplot(p04.male.earnings, main = "pow 0.4 transformed")
boxplot(p06.male.earnings, main = "pow 0.6 transformed")
boxplot(log.male.earnings, main = "log-transformed")
dev.off()

pdf("stats/1/chapt5/densities.pdf", width = 8, height = 10)
par(mfrow = c(4, 2))
plot(density(male.earnings), main = "untransformed")
plot(density(sqrt.male.earnings), main = "square-root transformed")
plot(density(p03.male.earnings), main = "pow 0.3 transformed")
plot(density(p04.male.earnings), main = "pow 0.4 transformed")
plot(density(p06.male.earnings), main = "pow 0.6 transformed")
plot(density(log.male.earnings), main = "log-transformed")
dev.off()

pdf("stats/1/chapt5/boxcox.pdf", width = 8, height = 10)
library("MASS")
par(mfrow = c(1, 1))
bc <- boxcox(male.earnings ~ 1,
    lambda = seq(0.3, 0.45, by = 1 / 100),
    interp = FALSE
)
ind <- (bc$y == max(bc$y))
ind2 <- (bc$y > max(bc$y) - qchisq(0.95, df = 1) / 2)
bc$x[ind]
bc$x[ind2]
dev.off()
cat(sprintf("MLE of lambda: %.15f\n", bc$x[ind]))
cat(sprintf("95%% CI for lambda: %.15f to %.15f\n", bc$x[ind2][1], bc$x[ind2][length(bc$x[ind2])]))
