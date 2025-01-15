# Data-Driven-Stock-Analysis
The Stock Performance Dashboard aims to provide a comprehensive visualization and analysis of the Nifty 50 stocks' performance over the past year.  The solution will offer interactive dashboards using Streamlit and Power BI to help Investors, analysts, and enthusiasts make informed decisions based on the stock performance trends.
## Features
1. **Volatility Analysis**: Identify the most volatile stocks.
2. **Cumulative Return**: Visualize the cumulative performance of top stocks.
3. **Sector-Wise Performance**: Analyze sector-level trends.
4. **Stock Price Correlation**: Explore the correlation between stock prices.
5. **Monthly Gainers and Losers**: Examine top-performing and underperforming stocks on a monthly basis.
## Prerequisites
To run the project, ensure you have the following installed:

- Python 3.7 or above
- streamlit
- pandas
- matplotlib
- seaborn 
- Power BI Desktop (optional for advanced visualization)
  ## Setup Instructions

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/stock-analysis-dashboard.git
cd stock-analysis-dashboard
```

### Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install streamlit
```
### Step 3: Prepare Your Data
Ensure you have the following datasets:
- **Stock Data CSV**: combined_data.csv
- **Sector Data CSV**: Sector_data - Sheet1.csv
### Step 4: Run the Streamlit Application
Launch the Streamlit dashboard:
```bash
streamlit run app.py
```
### Step 5: Visualize with Power BI (Optional)
To visualize data in Power BI:
1. Import the datasets (`top_cumulative_stocks.csv`, etc.).
2. Create slicers and visuals for a detailed analysis.
   
## Project Workflow

### Data Processing
1. Load stock and sector datasets.
2. Calculate metrics such as daily returns, cumulative returns, and monthly performance.
3. Merge datasets for sector-level analysis.

### Dashboard Visualizations in Streamlit
- **Volatility Analysis**: Bar chart of the top 10 most volatile stocks.
- **Cumulative Return**: Line chart for the top 5 stocks.
- **Sector Performance**: Bar chart showing average yearly returns for each sector.
- **Price Correlation**: Heatmap of stock price correlations.
- **Monthly Gainers/Losers**: Separate bar charts for each month.

### Power BI Workflow
1. Load the processed data files into Power BI.
2. Create slicers for filtering by month, stock, or sector.
3. Design dashboards to provide a high-level overview of stock performance.

## Contact
For any questions or suggestions, feel free to reach out:
- **Name**: Arti Kushwaha
- **Email**: artikwh@gmail.com
- **LinkedIn**: [Arti Kushwaha](https://www.linkedin.com/in/arti-kushwaha-32a68634)

