import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
@st.cache_data
def load_data(csv_file):
    data = pd.read_csv(csv_file)
    data['date'] = pd.to_datetime(data['date'])
    return data

# Visualization 1: Volatility Analysis
def volatility_analysis(data):
    st.markdown("Volatility Analysis")
    data['DailyReturn'] = data.groupby('Ticker')['close'].pct_change()
    volatility = data.groupby('Ticker')['DailyReturn'].std().sort_values(ascending=False)
    top_10_volatility = volatility.head(10)

    # Plot
    plt.figure(figsize=(10, 6))
    top_10_volatility.plot(kind='bar', color='orange')
    plt.title('Top 10 Most Volatile Stocks')
    plt.ylabel('Volatility (Standard Deviation)')
    plt.xlabel('Ticker')
    st.pyplot(plt)

# Visualization 2: Cumulative Return
def cumulative_return(data):
    st.markdown("Cumulative Return")
    data['DailyReturn'] = data.groupby('Ticker')['close'].pct_change()
    data['CumulativeReturn'] = data.groupby('Ticker')['DailyReturn'].transform(lambda x: (1 + x).cumprod() - 1)

    # Top 5 performing stocks
    final_returns = data.groupby('Ticker')['CumulativeReturn'].last().sort_values(ascending=False)
    top_5_stocks = final_returns.head(5).index
    top_5_data = data[data['Ticker'].isin(top_5_stocks)]

    # Plot
    plt.figure(figsize=(10, 6))
    for ticker in top_5_stocks:
        stock_data = top_5_data[top_5_data['Ticker'] == ticker]
        plt.plot(stock_data['date'], stock_data['CumulativeReturn'], label=ticker)

    plt.title('Top 5 Performing Stocks - Cumulative Return')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Return')
    plt.legend()
    st.pyplot(plt)

# Visualization 3: Sector-Wise Performance
def sector_performance(stock_data, sector_csv):
    st.markdown("Sector-Wise Performance")
    sector_data = pd.read_csv(sector_csv)
    stock_data['Ticker'] = stock_data['Ticker'].str.upper().str.strip()
    sector_data['CleanSymbol'] = sector_data['Symbol'].apply(lambda x: x.split(':')[-1].strip().upper())
    merged_data = pd.merge(stock_data, sector_data, left_on='Ticker', right_on='CleanSymbol', how='left')
    merged_data['DailyReturn'] = merged_data.groupby('Ticker')['close'].pct_change()
    yearly_return = merged_data.groupby('sector')['DailyReturn'].mean()

    # Plot
    plt.figure(figsize=(10, 6))   
    yearly_return.sort_values(ascending=False).plot(kind='bar', color='blue')
    plt.title('Sector-Wise Average Yearly Return')
    plt.ylabel('Average Yearly Return')
    plt.xlabel('Sector')
    st.pyplot(plt)

# Visualization 4: Stock Price Correlation
def stock_correlation(data):
    st.markdown("Stock Price Correlation Heatmap")
    pivot_data = data.pivot(index='date', columns='Ticker', values='close')
    correlation_matrix = pivot_data.corr()

    # Heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, cmap='coolwarm', annot=False, cbar=True, linewidths=0.5)
    plt.title('Stock Price Correlation Heatmap')
    st.pyplot(plt)

def gainers_losers_monthly(data):
    st.markdown(" Top Gainers and Losers (Month-wise)")
    # Create YearMonth column
    data['YearMonth'] = data['date'].dt.to_period('M')
    # Calculate monthly return
    data['MonthlyReturn'] = data.groupby(['Ticker', 'YearMonth'])['close'].transform(
        lambda x: (x.iloc[-1] - x.iloc[0]) / x.iloc[0]
    )
    # Get unique months
    monthly_data = data.drop_duplicates(subset=['Ticker', 'YearMonth'], keep='last')
    months = monthly_data['YearMonth'].drop_duplicates().sort_values()

    for month in months:
        st.markdown(f'<h5 style="text-decoration: underline;">Month: {month}</h5>', unsafe_allow_html=True)
        month_data = monthly_data[monthly_data['YearMonth'] == month]
        
        # Get top 5 gainers and losers
        top_gainers = month_data.nlargest(5, 'MonthlyReturn')
        top_losers = month_data.nsmallest(5, 'MonthlyReturn')

        # Create subplots
        fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

        # Plot gainers
        sns.barplot(
            data=top_gainers,
            x='MonthlyReturn',
            y='Ticker',
            palette='Greens',
            ax=axes[0]
        )
        axes[0].set_title("Top Gainers")
        axes[0].set_xlabel("Monthly Return")
        axes[0].set_ylabel("Ticker")

        # Plot losers
        sns.barplot(
            data=top_losers,
            x='MonthlyReturn',
            y='Ticker',
            palette='Reds',
            ax=axes[1]
        )
        axes[1].set_title("Top Losers")
        axes[1].set_xlabel("Monthly Return")
        axes[1].set_ylabel("Ticker")

        # Display the plots in Streamlit
        st.pyplot(fig)

# Set page configuration
#st.set_page_config(page_title="Stock Analysis Dashboard", layout="wide")
st.markdown("## **Stock Analysis Dashboard 📈**")
# Create a two-column layout
col1, col2 = st.columns([1, 3])  # Adjust the ratio as needed for left pane width

# Left navigation pane (col1)
with col1:    
    tab = st.radio(
        "Visualizations", 
        [
            "Volatility Analysis",
            "Cumulative Return Over Time",
            "Sector-Wise Performance",
            "Stock Price Correlation",
            "Top Gainers and Losers (Month-wise)",
        ],
        index=0,
    )

# Content area (col2)
with col2:
    # Load the data
    csv_file = 'combined_data.csv'
    sector_csv = 'Sector_data - Sheet1.csv'
    
    if csv_file:
        data = load_data(csv_file)

        if tab == "Volatility Analysis":
            volatility_analysis(data)

        elif tab == "Cumulative Return":
            cumulative_return(data)

        elif tab == "Sector-Wise Performance":
            if sector_csv:
                sector_performance(data, sector_csv)
            else:
                st.warning("Please upload a sector CSV file to view this analysis.")

        elif tab == "Stock Price Correlation":
            stock_correlation(data)

        elif tab == "Top Gainers and Losers (Month-wise)":
            gainers_losers_monthly(data)
    else:
        st.warning("Please upload a stock data CSV file to proceed.")
