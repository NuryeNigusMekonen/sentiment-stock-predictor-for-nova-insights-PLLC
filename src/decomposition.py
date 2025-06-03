# src/decomposition.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

def decompose_time_series(df, column='Close', period=30, model='additive', plot=True):
    """
    Perform seasonal decomposition on a time series.

    Args:
        df (pd.DataFrame): DataFrame indexed by Date.
        column (str): Column name to decompose.
        period (int): Seasonality period (e.g., 30 for ~monthly).
        model (str): 'additive' or 'multiplicative'.
        plot (bool): Whether to plot the decomposition.

    Returns:
        pd.DataFrame: Original df with added trend, seasonal, and residual columns.
    """
    df = df.copy()
    ts = df[column].dropna()
    result = seasonal_decompose(ts, model=model, period=period)

    df[f'{column}_trend'] = result.trend
    df[f'{column}_seasonal'] = result.seasonal
    df[f'{column}_residual'] = result.resid

    if plot:
        plt.figure(figsize=(10, 8))
        result.plot()
        plt.suptitle(f"{column} Decomposition ({model} model)", fontsize=16)
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.show()

    return df
