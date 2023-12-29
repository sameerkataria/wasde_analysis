from dash import Dash, html, dcc, Input, Output, State, dash
import plotly.express as px
import process_data as process_data
import dash_bootstrap_components as dbc  # Import Dash Bootstrap Components

# Initialize the Dash app with Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# List of commodities for the dropdown menu
commodities = ['Corn', 'Soybeans']  # Add more commodities as needed

# Layout of the app
app.layout = html.Div([
    html.Div([
        html.H1('Data Analytics for WASDE report by USDA', style={'textAlign': 'center', 'margin-bottom': '20px'}),
        html.H5('Select the commodity for Analysis', style={'textAlign': 'center', 'margin-bottom': '20px'}),
        dcc.Dropdown(
            id='commodity-dropdown',
            options=[{'label': commodity, 'value': commodity} for commodity in commodities],
            value='Corn',  # Set 'Corn' as the default selected commodity
            style={'width': '30%', 'margin': '0 auto', 'margin-bottom': '10px'}  # Adjust width and margin
        )]),
        # html.Button('Load Data', id='load-data-button'), 
        html.Div([
            dbc.Button("Load Data", color="primary", id='load-data-button')
        ],className="d-grid gap-2 col-1 mx-auto"),

    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='time-series-plot1',
                style={'height': '400px'}  # Adjust height
            ),
        ], width=6),

        dbc.Col([
            dcc.Graph(
                id='time-series-plot3',
                style={'height': '400px'}  # Adjust height
            ),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='time-series-plot2',
                style={'height': '400px'}  # Adjust height
            ),
        ], width=6),

        dbc.Col([
            dcc.Graph(
                id='time-series-plot4',
                style={'height': '400px'}  # Adjust height
            ),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='time-series-plot5',
                style={'height': '400px'}  # Adjust height
            ),
        ], width=6),

        dbc.Col([
            dcc.Graph(
                id='time-series-plot6',
                style={'height': '400px'}  # Adjust height
            ),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id='time-series-plot7',
                style={'height': '400px'}  # Adjust height
            ),
        ], width=6)
    ])
])


# Callback to update the graphs based on user input
@app.callback(
    [Output('time-series-plot1', 'figure'),
     Output('time-series-plot2', 'figure'),
     Output('time-series-plot3', 'figure'),
     Output('time-series-plot4', 'figure'),
     Output('time-series-plot5', 'figure'),
     Output('time-series-plot6', 'figure'),
     Output('time-series-plot7', 'figure')],
    [Input('load-data-button', 'n_clicks')],
    [State('commodity-dropdown', 'value')]
)
def update_graphs(n_clicks, selected_commodity):
    # Load data for the selected commodity only when the button is clicked
    if n_clicks is None or n_clicks == 0:
        # This means the button has not been clicked yet
        raise dash.PreventUpdate

    df = process_data.commodity_data(selected_commodity)
    harvested = process_data.get_area_harvested(df)
    planted = process_data.get_area_planted(df)
    beig_stocks = process_data.get_beigning_stocks(df)
    end_stocks = process_data.get_ending_stocks(df)
    imports = process_data.get_imports(df)
    exports = process_data.get_exports(df)
    yeild = process_data.get_yeild(df)

    fig_harvested = px.line(harvested, x='report_month', y='value', title='Area Harvested')
    fig_planted = px.line(planted, x='report_month', y='value', title='Area Planted')
    fig_beig = px.line(beig_stocks, x='report_month', y='value', title='Beginning Stocks')
    fig_end = px.line(end_stocks, x='report_month', y='value', title='Ending Stocks')
    fig_export = px.line(exports, x='report_month', y='value', title='Exports')
    fig_import = px.line(imports, x='report_month', y='value', title='Imports')
    fig_yeild = px.line(yeild, x='report_month', y='value', title='Yeild')

    return fig_harvested, fig_planted, fig_beig, fig_end, fig_export, fig_import, fig_yeild


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
