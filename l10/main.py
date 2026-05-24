import pandas as pd
import numpy as np
import matplotlib as plt
import plotly
import plotly.express as px
import plotly.graph_objects as go

# second parameter refers to the ISO standard Latin-1 character set and encoding format. it is an 8-bit character set that includes all the characters used in Western EU alphabets
data = pd.read_csv("WHO-COVID-19-global-data.csv", encoding = "ISO-8859-1")

data.columns = ("Date_reported", "Country_code", "Country", "WHO_region", "New_cases", "Cumulative_cases", "New_deaths", "Cumulative_deaths")

# Date_reported columns is string, typecast it to datetime format
data["Date_reported"] = pd.to_datetime(data["Date_reported"])

dataDates = data.groupby("Date_reported").sum()

fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=dataDates.index, y=dataDates["Cumulative_cases"], fill="tonexty", line_color="blue"))
fig1.update_layout(title="Comulative cases worldwide")
fig1.write_html("Fig1.html", auto_open=True)

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=dataDates.index, y=dataDates["New_cases"], fill="tonexty", line_color="blue"))
fig2.update_layout(title="new cases worldwide")
fig2.write_html("Fig2.html", auto_open=True)

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=dataDates.index, y=dataDates["Cumulative_deaths"], fill="tonexty", line_color="blue"))
fig3.update_layout(title="cumulative deaths worldwide")
fig3.write_html("Fig3.html", auto_open=True)

fig4 = go.Figure()
fig4.add_trace(go.Scatter(x=dataDates.index, y=dataDates["New_deaths"], fill="tonexty", line_color="blue"))
fig4.update_layout(title="new deaths worldwide")
fig4.write_html("Fig4.html", auto_open=True)