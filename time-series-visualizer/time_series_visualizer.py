import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('time-series-visualizer/fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] > df['value'].quantile(0.025))]
df = df[(df['value'] < df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    fig= plt.figure(figsize=(14,6))
    plt.plot(df.index, df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    monthly_data = df.groupby(pd.Grouper(freq='M'))['value'].sum()
    monthly_data_df = monthly_data.to_frame()
    monthly_data_df.index=monthly_data_df.index.to_period('M')
    df_bar = monthly_data_df.pivot_table(index=monthly_data_df.index.year , columns=monthly_data_df.index.month, values='value')

    # Draw bar plot
    fig= plt.figure(figsize=(14,6))
    df_bar.plot(kind='bar', ax=plt.gca())
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    month_names = [calendar.month_name[i] for i in range(1, 13)]
    plt.legend(title='Months', labels=month_names)
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    sns.boxplot(df_box, x=df_box['year'], y=df_box['value'], hue=df_box['year'], palette='pastel', ax=ax1)
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_title('Year-wise Box Plot (Trend)')

    month_order = [calendar.month_abbr[i] for i in range(1, 13)]
    sns.boxplot(df_box, x=df_box['month'], y=df_box['value'], hue=df_box['month'], order=month_order, ax=ax2)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
