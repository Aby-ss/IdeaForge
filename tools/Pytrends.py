import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

from rich.traceback import install
install(show_locals=True)

def get_trends(keywords, timeframe='today 5-y', geo='US'):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo=geo)
    interest_over_time_df = pytrends.interest_over_time()
    return interest_over_time_df

def plot_trends(data, title):
    plt.figure(figsize=(10, 6))
    for keyword in data.columns:
        plt.plot(data.index, data[keyword], label=keyword)
    plt.xlabel('Date')
    plt.ylabel('Interest Over Time')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

def main():
    # List of business keywords
    business_keywords = ['cryptocurrency', 'ecommerce', 'artificial intelligence', 'stock market']

    # Fetch Google Trends data
    trends_data = get_trends(business_keywords)

    # Plot the trends
    plot_trends(trends_data, 'Business Trends Over Time')

if __name__ == "__main__":
    main()