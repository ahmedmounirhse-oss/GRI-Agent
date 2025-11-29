import pandas as pd

def emissions_intensity(df: pd.DataFrame, emissions_col='emissions', denom_col='production'):
    df = df.copy()
    if emissions_col in df.columns and denom_col in df.columns:
        df['emissions_intensity'] = df[emissions_col] / df[denom_col].replace({0: pd.NA})
    return df
