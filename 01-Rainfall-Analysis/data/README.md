# Rainfall data

Use the original course CSV from [Week 8](https://github.com/Taenyoung-Lee/assignments/blob/8691d9023612b2067f38c376081a185ce3e9064a/time_series_analysis/week8/%EA%B0%95%EB%A6%89%EA%B0%95%EC%88%98%EB%9F%89_s.csv). [Week 6](https://github.com/Taenyoung-Lee/assignments/blob/8691d9023612b2067f38c376081a185ce3e9064a/time_series_analysis/week6/%EA%B0%95%EB%A6%89%EA%B0%95%EC%88%98%EB%9F%89_s.csv) contains the same file. The course export does not record the provider or the reuse terms for the file. The CSV is available from the original assignment and is stored locally for this project.

From the `01-Rainfall-Analysis` directory, download the archived file as follows.

```r
download.file(
  "https://raw.githubusercontent.com/Taenyoung-Lee/assignments/8691d9023612b2067f38c376081a185ce3e9064a/time_series_analysis/week8/%EA%B0%95%EB%A6%89%EA%B0%95%EC%88%98%EB%9F%89_s.csv",
  "data/gangneung-monthly.csv",
  mode = "wb"
)
```

The file has the columns `일시` (year and month, for example `1998년 1월`) and `강수량(mm)` (total precipitation in millimeters). The archived GitHub file is encoded as UTF-8, which the portfolio report uses by default. For a local EUC-KR copy with the same headers, set `RAINFALL_ENCODING=EUC-KR` in the environment before rendering.

The [Korea Meteorological Administration ASOS portal](https://data.kma.go.kr/data/grnd/selectAsosList.do?pgmNo=36) also offers monthly precipitation records for Gangneung (station 105). A fresh download may differ from the archived course CSV.
