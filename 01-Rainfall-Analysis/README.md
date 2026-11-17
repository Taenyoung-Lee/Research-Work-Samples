# Gangneung Rainfall Analysis

For a time series course in my master’s program, I analyzed monthly rainfall from a weather station in Gangneung, South Korea. I wanted to see which months were unusually wet or dry after accounting for seasonality.

## Data

The course CSV contains 331 monthly totals in millimeters from January 1998 through September 2025. December 2022 and February 2025 have no records. Two observed months have zero precipitation. The report parses the Korean year-month labels, converts rainfall to numeric values, drops invalid records, and sums entries by calendar month. See the [data instructions](data/) for the exact input file.

## Methods

1. Plot the series and compare monthly distributions. Examine autocorrelation and partial autocorrelation.
2. Search seasonal ARIMA orders by AIC using maximum likelihood. Inspect the original report's selected ARIMA(2,0,2)(0,1,1)[12] model separately. Also search ARMA orders with 12 calendar-month indicators and inspect residual correlation and normality.
3. Fit a Gamma distribution by maximum likelihood to the 329 positive totals. Assess fit with density, Q–Q, CDF, and P–P plots and report goodness-of-fit statistics.
4. Fit a Gamma GLM with a log link and a categorical month effect. Divide each deviance residual by the square root of the estimated dispersion times one minus the observation's leverage. Flag values outside ±1.96 as an exploratory screen. The cutoff uses a normal reference and is unadjusted for screening many months.

I kept the two missing months as `NA` so each observation stays in the right calendar month. The original analysis compressed those gaps, so the ARIMA fits and diagnostics can differ. The Gamma models still use the observed positive totals. I compute the Gamma regression’s residual ACF in observation order.

## Results

The month-specific regression flagged 17 low and 4 high observations. For example, December 2005 had 0.1 mm of rainfall, compared with a fitted mean of 35.7 mm and a standardized deviance residual of −3.70. These values agree with my coursework presentation. The figure below is from that analysis.

![Original Gamma distribution diagnostics for positive precipitation](figures/gamma-fit.png)

The [original residual-flag plot](figures/residual-flags.png) shows both tails against the rainfall series.

## How to run

From this project directory, install R and Pandoc, put the CSV in `data/` as instructed, and run:

```sh
Rscript -e 'install.packages(c("rmarkdown","knitr","readr","dplyr","lubridate","stringr","ggplot2","fitdistrplus","forecast","tseries","nortest","gridExtra","tibble","zoo"), repos="https://cloud.r-project.org")'
Rscript -e 'rmarkdown::render("rainfall.Rmd")'
```

The report writes the summaries, model fits, and diagnostic plots to `rainfall.html`. I haven’t rerun the full report since updating the code to keep missing months on the calendar.

## Original source

The [Week 16 R Markdown](https://github.com/Taenyoung-Lee/assignments/blob/8691d9023612b2067f38c376081a185ce3e9064a/time_series_analysis/week16/Timeseries_%EA%B0%95%EB%A6%89%EA%B0%95%EC%88%98%EB%9F%89_final.Rmd) contains the original analysis and preprocessing code. It uses the rainfall CSV saved in [Week 6](https://github.com/Taenyoung-Lee/assignments/blob/8691d9023612b2067f38c376081a185ce3e9064a/time_series_analysis/week6/%EA%B0%95%EB%A6%89%EA%B0%95%EC%88%98%EB%9F%89_s.csv) and [Week 8](https://github.com/Taenyoung-Lee/assignments/blob/8691d9023612b2067f38c376081a185ce3e9064a/time_series_analysis/week8/%EA%B0%95%EB%A6%89%EA%B0%95%EC%88%98%EB%9F%89_s.csv). I updated the [report](rainfall.Rmd) to read the CSV from `data/` and kept the focus on the rainfall analysis.
