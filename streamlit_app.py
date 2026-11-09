import yfinance as yf
import streamlit as st
import pandas as pd
st.title("MSFT Monthly Sharpe Ratio")
# Define the ticker and risk-free rate
ticker = 'MSFT'
rf_monthly = 0.0025  # 0.25% per month

# Download monthly stock price data for the past 5 years
data = yf.download(ticker, period='5y', interval='1mo')

# Handle yfinance returning a MultiIndex or single-level column
if isinstance(data.columns, pd.MultiIndex):
    close_prices = data['Close'][ticker]
else:
    close_prices = data['Close']

# Calculate monthly returns
monthly_returns = close_prices.pct_change().dropna()

# Calculate average excess return and standard deviation of returns
excess_returns = monthly_returns - rf_monthly
mean_excess_return = excess_returns.mean()
std_dev_return = monthly_returns.std()

# Calculate the Monthly Sharpe Ratio
monthly_sharpe_ratio = mean_excess_return / std_dev_return

# Display results in Streamlit
st.write(f"**Ticker:** {ticker}")
st.metric(label="Monthly Sharpe Ratio", value=f"{monthly_sharpe_ratio:.3f}")
