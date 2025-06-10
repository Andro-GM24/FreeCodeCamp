import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 is important assign the header to visualize the axes in the  plot
df = pd.read_csv('medical_examination.csv', header=0)

# 2 function lambda to create and asign the correct data to overweight 
df = df.assign(overweight=lambda x: np.where(
    (x['weight'] / (x['height'] / 100)**2) > 25, 1, 0))

# 3 normalize data
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)


# 4
def draw_cat_plot():
    # 5 columns that we want in the plot
    df_cat_values = [
        'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'
    ]
    df_cat = df_cat = pd.melt(frame=df,
                              id_vars=['cardio'],#separe with cardio
                              value_vars=df_cat_values)#columns to show

    # 6
    df_cat = df_cat_cardio_counts = df_cat.groupby(
        ['cardio', 'variable', 'value']).size().reset_index(name='total')
    #group by that columns and count it

    # 7

    #make it in a serie

    # 8
    g = sns.catplot(
        data=df_cat_cardio_counts,
        x='variable',#name
        y='total',#total that count with group
        hue='value',  #value of each bar
        col='cardio',  #split by cardio
        kind='bar')

    fig = g.fig
    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi'])#verify use correct data
                     & (df['height'] >= df['height'].quantile(0.025))
                     & (df['height'] <= df['height'].quantile(0.975))
                     & (df['weight'] >= df['weight'].quantile(0.025))
                     & (df['weight'] <= df['weight'].quantile(0.975))]

    #height is more than the 97.5th percentile
    #weight is less than the 2.5th percentile
    #weight is more than the 97.5th percentile

    # 12 matrix of correlation
    corr = df_heat.corr()

    # 13
    mask = np.triu(np.ones_like(corr, dtype=bool))
    #only get the upper triangle( up of the diagonal)

    # 14
    fig, ax = plt.subplots(figsize=(7, 7))

    # 15

    # use mask to dont get the upper tringule
    #fromat to the numbers
    #annot to  get the numbers in the plot
    sns.heatmap(corr,
                mask=mask,
                annot=True,
                fmt='.1f',
                square=True,
                cbar_kws={"shrink": 0.5},
                center=0,
                ax=ax)
    # 16

    fig.savefig('heatmap.png')
    return fig
