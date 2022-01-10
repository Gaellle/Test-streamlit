import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title('Analysis of cars features between 1971 and 1983')
st.write ('Select a continent :')

continent = ['All','USA','Japan','Europe']
menu = st.radio('Choose',continent)


data = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv', sep = ',')
data['continent'] = data.continent.replace({' US.': 'USA', ' Europe.':'Europe',' Japan.':'Japan'})


# graph 1

def graph1 (data) :
    corr_cub_weight = px.scatter(data_frame = data, x= "cubicinches", y="weightlbs", 
                 title = 'Correlation between engine size and car weight (1971 - 1983)', 
                 color = 'continent',
                 labels = {'cubicinches' : 'Engine size (in CID)', 'weightlbs':'Car weight (in lb)', 'continent':'Continent'},
                 color_discrete_sequence=["mediumseagreen",'coral','crimson']
                )

    corr_cub_weight.update_layout(title_x=0.5, 
                  legend=dict(
                              orientation="h",
                              yanchor="bottom",
                              y=1.02,
                              xanchor="center",
                              x=0.5
))
    return st.plotly_chart(corr_cub_weight)

# CORRELATION CONSOMMATION / POIDS

def graph2 (data) :
    fig2 = px.histogram(data, x="weightlbs", y="mpg", histfunc='avg',
                  title = 'Correlation between car weight and average efficiency', 
                 labels = {'mpg' : 'Efficiency (in MPG - miles per gallon)', 'weightlbs':'Car weight (in lb)', 'continent':'Continent'},
                 color_discrete_sequence=["indigo"])

    fig2.update_layout(bargap=0.1, title_x=0.5)
    fig2.update_yaxes(title='Average efficiency (in MPG - miles per gallon)')
    return st.plotly_chart(fig2)

# DISTRIBUTION YEARS

def graph3 (data):
    fig3 = px.histogram(data, x="year",
                  title = 'Cars years distribution', 
                 labels = {'year' : 'Year', 'continent':'Continent'},
                 color_discrete_sequence=["mediumseagreen",'coral','crimson'],
                 color = 'continent', nbins = 14)

    fig3.update_layout(bargap=0.1, title_x=0.5, legend=dict(
                              orientation="h",
                              yanchor="bottom",
                              y=1.02,
                              xanchor="center",
                              x=0.5
))
    return st.plotly_chart(fig3)

# CORRELATION ACCELERATION / CONSOMMATION

def graph4(data):
    fig4 = px.scatter(data, x='mpg', y='time-to-60', color = 'continent',trendline="ols",
                 title = 'Correlation between fuel consumption and acceleration', 
                 labels = {'time-to-60' : 'Acceleration measured in time to 60 mph (in sec.)', 'continent':'Continent', 'mpg' : 'Efficiency (in MPG - miles per gallon)'},
                 color_discrete_sequence=["mediumseagreen",'coral','crimson'])
    fig4.update_layout(title_x=0.5,  legend=dict(
                              orientation="h",
                              yanchor="bottom",
                              y=1.02,
                              xanchor="center",
                              x=0.5
))

    return st.plotly_chart(fig4)

if menu == 'USA' :
    usa = data[data['continent'] == 'USA']
    graph1(usa)
    graph2(usa)
    graph3(usa)
    graph4(usa)

elif  menu == 'Japan' :
    japan = data[data['continent'] == 'Japan']
    graph1(japan)
    graph2(japan)
    graph3(japan)
    graph4(japan)

elif  menu == 'Europe' :
    europe = data[data['continent'] == 'Europe']
    graph1(europe)
    graph2(europe)
    graph3(europe)
    graph4(europe)

elif  menu == 'All' :
    graph1(data)
    graph2(data)
    graph3(data)
    graph4(data)
