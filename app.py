import dash 
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# load our data 
def load_data():
    df = pd.read_csv('assets/healthcare.csv')
    # data framing
    # check its in the numeric form, else replace to a nunm form
    df['Billing Amount'] = pd.to_numeric(df['Billing Amount'], errors='coerce')
    df['Date of Admission'] = pd.to_datetime(df["Date of Admission"])
    # create a new row
    df['YearMonth'] = df["Date of Admission"].dt.to_period("M")
    return df

data = load_data()
# get num of recors
num_records = len(data)
# get average billing
avg_billing = data["Billing Amount"].mean()

# create the web app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# app layout and design
app.layout = dbc.Container([
    # structure for container (rows + cols)
    dbc.Row([
        dbc.Col(html.H1("Heathcare Dashboard"), width=15, className="text-center")
    ]),

    dbc.Row([
        dbc.Col(html.Hr(),width=15)
    ], className="my-0"),

    # hospital statistics
    dbc.Row([
        dbc.Col(html.Div(f"Total Pacient Records: {num_records}"), className="top-text", width=4),
        dbc.Col(html.Div(f"Average Billing Amount: {avg_billing:,.2f}"), className="top-text", width=4)
    ], className="mb-5 top-box"),

    # patient demographics
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Patient Demographics", className="card-title"),
                    dcc.Dropdown(
                        id="gender-filter",
                        options=[{"label":gender, "value":gender} for gender in data["Gender"].unique()],
                        value=None,
                        placeholder="Select a Gender"
                    ),
                    dcc.Graph(
                        id="age-distribution"
                    )
                ])
            ])
        ], width=6),

        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                   html.H4("Medical Condition Distribution", className="card-title"),
                   dcc.Graph(
                       id="condition-distribution"
                   )
                ])
            ])
        ], width=6)
    ], className="mb-5 row"),
    
    # Insurance provider data
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Insurance Provider comparison", className="card-title"),
                    dcc.Graph(
                        id="insurance-comparison"
                    )
                ])
            ])
        ], width=15)
    ]),

    # Billing Distribution
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Billing Amount Distribution", className="card-title"),
                    dcc.Slider(
                        id="billing-slider",
                        min=data["Billing Amount"].min(),
                        max=data["Billing Amount"].max(),
                        value=data["Billing Amount"].median(), 
                        marks={int(value):f"${int(value)}" for value in data["Billing Amount"].
                            quantile([0, 0.25, 0.5, 0.75, 1]).values},
                            step=100
                    ),
                    dcc.Graph(
                        id="billing-distribution"
                    )
                ])
            ])
        ], width=15)
    ]),
 
    # Trends in Admission 
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Trends in admission", className="card-title"),
                    dcc.RadioItems(
                        id="chart-type", 
                        options=[{"label":"Line Chart", "value":"line"},
                                 {"label":"Bar Chart", "value":"bar"}],
                        value="line",
                        inline=True,
                        className="mb-5"
                    ),
                    dcc.Dropdown(
                        id="condition-filter",
                        options=[{"label": condition, "value": condition} for condition in data["Medical Condition"].unique()],
                        value=None,
                        placeholder="Select a Medical Condition"
                    ),
                    dcc.Graph(
                        id="admission-trends"
                    )
                ])
            ])
        ])
    ])
], fluid=True)

# Create callbacks
# callbacks take two params
@app.callback(
    Output('age-distribution', 'figure'),
    Input('gender-filter', 'value')
)
def updateDistribution(selected_gender):
    if selected_gender:
        filtered_df = data[data["Gender"] == selected_gender]
    else:
        # no filter applied
        filtered_df = data
    
    # if theres nothing deal with it
    if filtered_df.empty:
        return {}
    
    fig = px.histogram(
        filtered_df,
        x = "Age",
        nbins = 10,
        color="Gender",
        title="Age Distribution By Gender",
        color_discrete_sequence=["#355C7D", "#FF7582"]
    )

    return fig

# medical condition distribution
@app.callback(
    Output("condition-distribution", 'figure'),
    Input("gender-filter", "value")
)
def updateMedCondition(selected_gender):
    filtered_df = data[data["Gender"] == selected_gender] if selected_gender else data
    fig = px.pie(
        filtered_df, 
        names="Medical Condition", 
        title="Medical Condition Distribution")
    return fig

# insurance provider comparison
@app.callback(
    Output("insurance-comparison", "figure"),
    Input("gender-filter", "value")
)
def updateInsurance(selected_gender):
    filtered_df = data[data["Gender"] == selected_gender] if selected_gender else data
    fig = px.bar(
        filtered_df,
        x="Insurance Provider",
        y="Billing Amount",
        color="Medical Condition",
        title="Insurance Provided Price Comparison",
        color_discrete_sequence=["#75BDE0","#355C7D","#725A7A", "#C56C86", "#FF7582", "#FD836D", "#FFBA69"]
    )
    return fig

# billing distribution
@app.callback(
    Output("billing-distribution", "figure"),
    [Input("gender-filter", "value"),
     Input("billing-slider", "value")]
)
def updateBillingDist(selected_gender, slider_val):
    filtered_df = data[data["Gender"] == selected_gender] if selected_gender else data
    filter_data = filtered_df[filtered_df["Billing Amount"] <= slider_val]
    fig = px.histogram(
        filter_data,
        x="Billing Amount",
        nbins=10,
        barmode="group",
        title="Billing Amount Distribution",
        color_discrete_sequence=["#FF7582", "#725A7A"]
    )
    return fig

# trends in admission
@app.callback(
    Output("admission-trends", "figure"),
    [Input("chart-type", "value"),
     Input("condition-filter", "value")]
)
def updateAdmission(chart_type, selected_condition):
    filtered_df = data[data["Medical Condition"] == selected_condition] if selected_condition else data
    trend_df = filtered_df.groupby("YearMonth").size().reset_index(name="Count")
    trend_df["YearMonth"] = trend_df["YearMonth"].astype(str)
    if chart_type == "line":
        fig = px.line(
            trend_df,
            x="YearMonth",
            y="Count",
            title="Admission Trends Over Time"
        )
    else:
        fig = px.bar(
            trend_df,
            x="YearMonth",
            y="Count",
            title="Admission Trends Over Time"
        )
    return fig

if __name__ == "__main__":
    app.run(debug=True)