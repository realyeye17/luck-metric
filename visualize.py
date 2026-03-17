import plotly.express as px
import numpy as np



def make_scatter_plot(data):
    #Creates scatterplot that compares Skill and Outcome metrics
    fig = px.scatter(data, x='Skill+', y='Outcome+',
                     hover_name='Name', hover_data={'Skill+': ':.1f', 'Outcome+': ':.1f'},
                     title = 'Skill+ vs Outcome+', template='plotly_dark', trendline='ols')
    fig.show()

def make_luck_graph(data):
    #Creates bar graph that demonstrates luckiest and unluckiest hitters
    fig = px.bar(data, x='Luck', y='Name',
                 orientation='h', color='Luck',
                 color_continuous_scale='RdYlGn',
                 title = 'Luckiest and Unluckiest Hitters')
    
    fig.add_vline(x=0, line_dash='dash', line_color='white')
    fig.show()