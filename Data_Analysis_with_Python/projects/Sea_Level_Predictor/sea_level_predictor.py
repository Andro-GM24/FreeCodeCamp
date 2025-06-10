import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(5, 10))

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    years_extended = pd.Series(range(df['Year'].max() + 1, 2051))
    all_years = pd.concat([df['Year'], years_extended])

    slope, intercept, r_value, p_value, std_err = linregress(
        df['Year'], y=df['CSIRO Adjusted Sea Level'])
    #make the function
    # is the slope and x that model tha indepent value and itercept like the value of y if x=0

    years_for_regression = np.arange(df['Year'].min(), 2051)
    regresssion_func = slope * years_for_regression + intercept
    plt.plot(years_for_regression, regresssion_func)

    slope_1, intercept_2, r_value_3, p_value_4, std_err_5 = linregress(
        df['Year'].loc[df['Year'] >= 2000],
        y=df['CSIRO Adjusted Sea Level'].loc[df['Year'] >= 2000])
    recently_years = np.arange(2000, 2051)
    regresssion_func_recent = slope_1 * recently_years + intercept_2
    plt.plot(recently_years, regresssion_func_recent)

    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    plt.show()

    # Create second line of best fit

    # Add labels and title

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
