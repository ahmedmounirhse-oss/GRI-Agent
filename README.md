# Sustainability GRI Agent — Starter

Starter repo for an automation agent that ingests sustainability data (GRI), computes KPIs,
shows a Streamlit dashboard, scaffolds RAG chatbot, and can auto-generate/send reports.

## Quick start
1. Create and activate a Python virtual environment (Python 3.10+ recommended).
2. Install requirements: `pip install -r requirements.txt`
3. Drop a CSV/XLSX file into `data/` and run the ingestion watcher:
   `python src/ingestion.py`
4. Run dashboard: `streamlit run src/dashboard/app.py`

## Repo structure
See `src/` for core modules: ingestion, etl, kpi, anomalies, dashboard, chatbot scaffold, reports and emailer.
