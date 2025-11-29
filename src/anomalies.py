import numpy as np
import pandas as pd

def iqr_outliers(series: pd.Series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return (series < lower) | (series > upper)

def zscore_outliers(series: pd.Series, thresh=3):
    z = (series - series.mean()) / series.std(ddof=0)
    return z.abs() > thresh
