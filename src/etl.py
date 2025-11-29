import pandas as pd
from pathlib import Path

PARQUET_DIR = Path('data/parquet')

def list_parquets():
    return list(PARQUET_DIR.glob('*.parquet'))

def load_parquet(path: Path) -> pd.DataFrame:
    return pd.read_parquet(path)

def clean_basic(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(how='all')
    df.columns = [c.strip() for c in df.columns]
    for c in df.columns:
        if 'date' in c.lower() or 'year' in c.lower():
            df[c] = pd.to_datetime(df[c], errors='coerce')
    return df

if __name__ == '__main__':
    pars = list_parquets()
    for p in pars:
        df = load_parquet(p)
        df = clean_basic(df)
        print(p.name, df.shape)
