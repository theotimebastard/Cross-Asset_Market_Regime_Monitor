
###### IMPORTING THE LIBRARIES ######
import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

###### FUNCTIONS DEFINITIONS ######

###### download data ######
def download_data(tickers, start_date=None, end_date=None):   # download close prices from Yahoo Finance for a list of tickers
    data = yf.download(tickers, 
    start=start_date, 
    end=end_date, 
    auto_adjust=True, 
    progress=False)["Close"]
    return data

###### load data ######
def load_data(path, tickers=None):    # load CSV, if missing download and save
    try:
        return pd.read_csv(path, index_col=0, parse_dates=True)
    except FileNotFoundError:
        if tickers is None:
            raise
        df = download_data(tickers)
        df.to_csv(path)
        return df

###### sanity check ######
def check_na(data, tag=""):
    n = len(data) or 1
    null_sum = data.isnull().sum()
    null_percentage = (null_sum / n).round(3)
    print(f"[{tag}] Ratio of missing values: {null_percentage}\n[{tag}] Count of missing values: {null_sum} ")

###### preprocess data ######
def preprocess(data):                       # forward-fill then drop any remaining missing rows (simple cleaning)
    data = data.ffill().dropna()
    return data

def normalize(prices):                      # convert price levels to cumulative returns
    returns = prices.pct_change().fillna(0)
    cum_returns = (1 + returns).cumprod()
    return cum_returns


###### create plot ######
def plot(data, title):
    fig = plt.figure(figsize=(8,6))
    plt.plot(data)
    plt.title(title)
    plt.xticks(rotation=45)
    plt.legend(data.columns.tolist(), loc="best")
    plt.tight_layout()
    #plt.savefig("Cross-Asset_Market_Dashboard")    # uncomment to save plot locally
    #plt.show()                                     # uncomment to show plot in browser
    return fig

###### create dashboard ######
def create_dashboard(data, title, fig):
    st.title(title)
    st.pyplot(fig)
    try:
        last_dt = data.index.max().date()
    except Exception:                           # indicating the last date of the data download
        last_dt = "N/A"
    st.caption(f"Last data download: {last_dt}")


###### MAIN WORKFLOW (FUNCTIONS CALLS) ######


###### download data ######
tickers = ["ES=F", "ZN=F", "GC=F", "CL=F",  "DX=F","ZW=F"]
#data = download_data(tickers)          # uncomment to redownload daily data, else use csv data file
#print(data)

###### save data locally ######
#data.to_csv("data.csv")                # uncomment to save updated data

###### load data ######
prices = load_data("data.csv", tickers=tickers)


###### rename tickers by corresponding asset ######
Ticker_labels = {
    "ES=F": "S&P 500 Future (ES)",
    "ZN=F": "US 10Y Note Future (ZN)",
    "GC=F": "Gold (GC)",
    "CL=F": "WTI Crude Oil (CL)",
    "DX=F": "US Dollar Index Future (DX)",
    "ZW=F": "Wheat (ZW)",
}
prices = prices.rename(columns=Ticker_labels)

###### sanity check ######
check_na(prices, tag="before_cleaning_data")                    # check before cleaning

###### preprocess data ######
prices = preprocess(prices)                                    # cleaning the data
check_na(prices, tag="after_cleaning_data")                    # check after cleaning
cum_returns = normalize(prices)

title = "Cross-Asset Market Dashboard"
fig = plot(cum_returns, title)
create_dashboard(cum_returns, title, fig)






