# Cross-Asset Market Regime Monitor · Prototype v1

*A minimal Streamlit dashboard as the first step toward a multi-asset regime monitor.*

## Overview
This project aims to build a **Cross-Asset Market Regime Monitor**: download and clean data across major asset classes, align series, and produce indicators/visuals to understand regime shifts.

## What’s in v1 (this repo)
- Load prices from a local CSV (`data.csv`). If the file is missing, it falls back to a one-shot download via Yahoo Finance and saves the CSV for reproducibility.
- Basic missing-value check (counts & ratios).
- Simple preprocessing: forward-fill, then drop remaining gaps.
- Normalize to cumulative returns for comparability.
- Single matplotlib chart displayed and saved locally or rendered inside Streamlit with clear labels and last data download.

### Assets included
- WTI Crude Oil (CL)  
- US Dollar Index Future (DX)  
- S&P 500 Future (ES)  
- Gold (GC)  
- US 10Y Note Future (ZN)  
- Wheat (ZW)

## How to run
```
pip install streamlit pandas yfinance matplotlib
streamlit run dashboard.py
```
## Roadmap (next steps)
- Robust fetching & validation (types, ranges, missing values) across asset classes.
- Align series on a common start date before comparison.
- Add analytics: returns vs. prices, drawdowns, rolling volatility, simple regime flags.
- Multi-panel visuals and clean CSV exports for reuse.

*This is a transparent starting point: a minimal, working app that will be expanded progressively.*






