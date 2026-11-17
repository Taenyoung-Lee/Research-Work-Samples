# Robust Margin-Based Classification

This project comes from my master's thesis, *Robust Margin-Based Classification via Loss-Shifting*. I implemented and compared binary classifiers that use modified margin-based losses under asymmetric training-label noise.

## Classifiers

The [R implementation](R/loss_shifting_v4.R) supports hinge, squared hinge, logistic, and exponential losses with linear or Gaussian kernels. For a margin $u=yf(x)$, the soft and hard shifts leave the base loss unchanged for $u\geq-\eta$ and evaluate the loss at the effective margin $u-r(u)$ below $-\eta$. The soft version uses $r(u)=(1+\alpha)(u+\eta)$ and is continuous at the threshold. The hard version uses $r(u)=(1+\alpha)u$ and has a jump there. The fitting code includes majorization-minimization for hinge and squared hinge, iteratively reweighted least squares for logistic and exponential losses, and optional quadratic-programming solvers for hinge and squared hinge. The training wrapper implements cross-validation, multiple starts, and an objective-based line search.

## Simulation

The [XOR experiment](xor.Rmd) generates two-dimensional training and test samples from four Gaussian clusters. The class depends on the signs of the cluster center coordinates. It flips a specified fraction of training labels within each class and leaves the test labels intact. The default experiment uses 200 training observations, 400 test observations, and 10 replications at each of five positive-class flip rates (0%, 5%, 10%, 15%, and 20%). The negative-class flip rate stays at zero.

The report compares unshifted, soft-shifted, and hard-shifted versions of the four losses. Benchmarks include a radial SVM (`e1071`), ridge logistic regression on features from a Gaussian kernel eigendecomposition (labeled `glm` in the original table), and the theoretical XOR sign rule. The output reports mean test accuracy and its across-replication standard deviation. This experiment uses fixed simulation seeds through the original driver.

## How to run

From this project directory, install R and Pandoc, then run:

```sh
Rscript -e 'install.packages(c("rmarkdown","knitr","e1071","tidyr","dplyr","kableExtra","future","future.apply","progressr","glmnet","kernlab","quadprog"), repos="https://cloud.r-project.org")'
Rscript -e 'rmarkdown::render("xor.Rmd")'
```

The full grid performs 50 replications across the five noise settings, with cross-validation and multiple optimization starts for each candidate classifier. It runs with multiple R processes by default and creates `xor.html` and `xorffinal.csv`. For a shorter check, run one replication at a 10% positive flip rate in a single R process.

```sh
Rscript -e 'Sys.setenv(LOSS_SHIFT_QUICK="1", LOSS_SHIFT_WORKERS="1"); rmarkdown::render("xor.Rmd")'
```

A single replication estimates no across-replication variation. The original table formatter reports 0 in the standard-deviation column in that case. The runner and core implementation were reviewed statically. Neither the short nor the full experiment has been rerun for this portfolio. The simulation table is generated on demand.

## Original source

The [archived classifier implementation](https://github.com/Taenyoung-Lee/Margin_based_Loss_shifting_Binary_classfication/blob/b35f82919266e6d79419d37241e730f89ffd2451/loss_shifting_v4.R) is included unchanged. The [original simulation report](https://github.com/Taenyoung-Lee/Margin_based_Loss_shifting_Binary_classfication/blob/678e36e65465b9f8afe09be8fae4cb92517c9308/loss_shift_paper_table_parallel_xor_v5_2.Rmd) is the matching v4-based driver. The portfolio version updates its source path, uses the standard `predict()` generic for the `glmnet` models, and adds optional controls for a single-process run and a smaller grid.
