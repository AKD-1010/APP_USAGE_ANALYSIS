import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("< location of the csv file in your system >")  # importing the datafile

# print(data.isnull().sum())  #checking if any column has null values

# print(data.describe()) # for quick analysis of each column


# for date vs usage graph
figure = px.bar(data_frame = data,  x="Date", y="Usage", color = "App",   
        title = "USAGE GRAPH")
figure.show()

#-------------------------------------------------------------------------------------------------------------------------------

# FOR DATE VS NOTIFICATION GRAPH
figure = px.bar(data_frame = data,  x="Date", y="Notifications", color = "App",    
         title = "Notification  GRAPH")
figure.show()


#-------------------------------------------------------------------------------------------------------------------------------


# FOR DATE VS Times opened GRAPH
figure = px.bar(data_frame = data,  x="Date", y="Times opened", color = "App",      
        title = "OPENING  GRAPH")
figure.show()

#------------------------------------------------------------------------------------------------------------------------------


# FOR NOTIFICATION VS USAGE SCATTER GRAPH
figure = px.scatter(data_frame = data,  x="Notifications", y="Usage", size = "Notifications", trendline = "ols",     
        title ="NOTIFICATION VS USAGE")
figure.show()
