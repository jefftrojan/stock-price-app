import yfinance as yf
import streamlit as st
import pandas as pd


st.write(
    """
    # Stock price application

    Shown are the stock closing price and volume of Google

    """ 
)

# define ticker symbol
ticker_symbol = "GOOGL"

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period="1d", start="2020-5-30", end="2022-10-30")

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
