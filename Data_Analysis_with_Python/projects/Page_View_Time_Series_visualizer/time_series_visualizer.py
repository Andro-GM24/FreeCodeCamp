import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np

register_matplotlib_converters()

df = pd.read_csv('fcc-forum-pageviews.csv',
                 header=0,
                 dtype={'value': np.float64})

df = df.loc[(df['value'] < df['value'].quantile(0.975))
            & (df['value'] > df['value'].quantile(0.025))]

df['months_year'] = df['date'].str[5:7]
df['years'] = df['date'].str[0:4]
df.set_index('date', inplace=True)

# Clean data


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(10, 5))
    # use index because there is not a column
    ax.plot(df.index, df['value'], color='b')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")

    plt.grid(True)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():

    df_bar = df.copy()
    df_bar = df_bar.groupby(['years', 'months_year']).mean().reset_index(
    )  #agrupa por año y despues por mes y saca el el promedio

    month_map = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }
    df_bar['month'] = df_bar['months_year'].map(month_map)

    month_order = list(month_map.values())
    df_bar['month'] = pd.Categorical(df_bar['month'],
                                     categories=month_order,
                                     ordered=True)

    # Draw bar plot
    cat_plot = sns.catplot(
        data=df_bar,
        x='years',  #this is the x in the plot to compare, that we organizate
        y='value',  #the value
        hue='month',  #the split it 
        kind='bar')
    plt.legend(title='Months')
    cat_plot.set(xlabel='Years', ylabel='Average Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = pd.to_datetime(df_box['date']).dt.year
    df_box['month'] = pd.to_datetime(df_box['date']).dt.strftime('%b')
    df_box['month_num'] = pd.to_datetime(df_box['date']).dt.month
    df_box = df_box.sort_values('month_num')
    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(data=df_box,
                x='month',
                y='value',
                ax=axes[1],
                order=[
                    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                    'Sep', 'Oct', 'Nov', 'Dec'
                ])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    plt.tight_layout()

    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
