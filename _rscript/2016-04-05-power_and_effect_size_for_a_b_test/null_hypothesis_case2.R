# load package and color set 
library(openintro)
data(COL)

# 2 sample proportion z test
x1 <- 14517
x2 <- 14391
n1 <- 109925
n2 <- 110402

prop.z <- function(x1, x2, n1, n2) {
  p1 <- x1 / n1
  p2 <- x2 / n2
  p.pooled <- (x1 + x2) / (n1 + n2)
  se <- sqrt(p.pooled * (1 - p.pooled) * (1 / n1 + 1 / n2))
  d <- p1 - p2
  score.z <- d / se
  return(score.z)
}

# draw dist

draw.norm <- function(x1, x2, n1, n2) {
  zscore <- prop.z(x1, x2, n1, n2)
  p1 <- x1 / n1
  p2 <- x2 / n2
  normTail(U = zscore,
           col = COL[1],
           xlim = c(-3, 4),
           axes  =  FALSE,
           lwd  =  2)
  at <- c(-6, 0, zscore, 6)
  labels <- c(expression(0, H[0]*': '*d*' = 0  '),
              paste0('diff. = ', round(p1 - p2, 4)), 0)
  axis(1, at, labels, cex.axis = 1)
  yMax <- 0.4
  
  arrows(2.5, yMax / 2,
         2.0, yMax / 6,
         length = 0.1,
         col = COL[1],
         lwd = 1.5)
  text(2.5, yMax / 2, paste0('p-value\n', round(1 - pnorm(zscore), 4)),
       pos = 3,
       cex = 1.2,
       col = COL[1])
  
  arrows(qnorm(0.95), yMax / 1.3,
         qnorm(0.95), 0.005,
         length = 0.1,
         col = COL[4],
         lwd = 1.5)
  text(qnorm(0.95), yMax / 1.3, 'Critical\nValue',
       pos = 3,
       cex = 1.2,
       col = COL[1])
}

# draw dist
myPDF('null_hypothesis_case2.pdf', 6.75, 2.64,
      mar = c(2, 0, 0.5, 0),
      mgp = c(3, 0.65, 0))
draw.norm(x1, x2, n1, n2)
dev.off()
