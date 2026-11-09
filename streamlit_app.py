import yfinance as yf
import streamlit as st
import yfinance as yf
# Fetches 5 years of MSFT data and prints the final overall average closing price.
st.title("MSFT 5-Year Average Stock Price")
# Fetch 5 years of historical data for MSFT
data = yf.Ticker("MSFT").history(period="5y")
if not data.empty:
# Calculate the total average closing price
  overall_average = data['Close'].mean()
# Print the result directly to the screen
  st.metric(label="5-Year Average Price", value=f"${overall_average:.2f}")
else:
  st.error("No data found for MSFT.")
