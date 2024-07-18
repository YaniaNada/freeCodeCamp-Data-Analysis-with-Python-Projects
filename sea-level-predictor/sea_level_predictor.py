import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('sea-level-predictor/epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize= (14,6))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level')


    # Create first line of best fit
    result= linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    slope= result.slope
    intercept= result.intercept

    future_years = np.arange(1880, 2051)
    predicted_sea_level_rise = slope * future_years + intercept

    plt.figure(figsize= (14,6))
    plt.scatter(data=df, x='Year', y='CSIRO Adjusted Sea Level', color='blue')
    plt.plot(future_years, predicted_sea_level_rise, color= 'red')
  

    # Create second line of best fit
    filtered_df= df[df['Year']>= 2000]
    filtered_years = filtered_df['Year']
    filtered_sea_level_rise = filtered_df['CSIRO Adjusted Sea Level']

    result= linregress(filtered_years,filtered_sea_level_rise)
    slope= result.slope
    intercept= result.intercept

    future_years= np.arange(2000, 2051)

    predicted_sea_level_rise= slope*future_years + intercept

    plt.scatter(filtered_df['Year'], filtered_df['CSIRO Adjusted Sea Level'], color='blue')
    plt.plot(future_years, predicted_sea_level_rise, color='orange')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()