import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    fig , ax = plt.subplots(figsize = (12,8))
    ax = plt.scatter(x,y)

    # Create first line of best fit
    line_first = linregress(x,y)
    print(line_first)
    x_pred = pd.Series([i for i in range(x.min(),2051)])
    y_pred = line_first.intercept + line_first.slope * x_pred
    plt.plot(x_pred, y_pred, 'r-', label="Line of Best Fit")

    df_new = df.loc[df['Year'] >= 2000]
    x_new = df_new['Year']
    y_new = df_new['CSIRO Adjusted Sea Level']

    # Create second line of best fit
    line_second = linregress(x_new,y_new)
    print(line_second)

    x_pred_new = pd.Series([i for i in range(2000,2051)])
    y_pred_new = line_second.intercept + line_second.slope * x_pred_new
    plt.plot(x_pred_new, y_pred_new, 'green', label="Line of Best Fit")

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()