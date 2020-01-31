"""
Import Data 
Adapted from: https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
"""

import yfinance as yf # https://pypi.org/project/yfinance/

tickers = ['AMZN','GOOG','AAPL']
output = True
bar = '~'*100
print(bar)

for ticker in tickers:
    ticker_obj = yf.Ticker(ticker)
    history_df = ticker_obj.history(period='1d', start='2010-1-1', end='2020-1-1')
    recommends_df = ticker_obj.recommendations
    print('\n%s\n'%ticker)
    print('History\n%s\n'%history_df.head())
    print('Recommendations\n%s\n'%recommends_df.head())
    print(bar)
    if output:
        history_df.to_csv('data/original/%s_history.csv'%ticker)
        recommends_df.to_csv('data/original/%s_recommends.csv'%ticker)
