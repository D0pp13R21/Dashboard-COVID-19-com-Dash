import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Carregar dados
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
data = pd.read_csv(url)
brazil_data = data[data["location"] == "Brazil"]

# Criar gráficos interativos
fig_cases = px.line(brazil_data, x="date", y="new_cases", title="Casos Diários no Brasil")
fig_deaths = px.line(brazil_data, x="date", y="new_deaths", title="Mortes Diárias no Brasil")

# Configurar app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard COVID-19 - Brasil", style={"textAlign": "center"}),
    dcc.Graph(figure=fig_cases),
    dcc.Graph(figure=fig_deaths),
])

if __name__ == "__main__":
    app.run_server(debug=True)
