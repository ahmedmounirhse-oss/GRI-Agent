import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(layout='wide')
st.title('Sustainability GRI Dashboard — Starter')

PARQUET_DIR = Path('data/parquet')
files = list(PARQUET_DIR.glob('*.parquet'))

if not files:
    st.warning('No parquet files found. Drop CSV/XLSX into `data/` to auto-convert.')
else:
    sel = st.selectbox('Select dataset', [f.name for f in files])
    df = pd.read_parquet(PARQUET_DIR / sel)
    st.subheader('Preview')
    st.dataframe(df.head())
    st.subheader('Numeric overview')
    nums = df.select_dtypes(include='number').fillna(0)
    if not nums.empty:
        st.line_chart(nums)
    else:
        st.write('No numeric columns to plot.')
