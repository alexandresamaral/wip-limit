import pandas as pd
import plotly.express as px

# Data
current_wip = 15
current_cycle_time = 18.92
desired_cycle_time = 15
current_throughput = current_wip / current_cycle_time
desired_wip = current_throughput * desired_cycle_time

# Create a DataFrame
data = pd.DataFrame({
    'Scenario': ['Current WIP', 'Desired WIP'],
    'Number of Items': [current_wip, desired_wip]
})

# Create a bar chart using Plotly Express
fig = px.bar(data, x='Scenario', y='Number of Items',
             title='Current vs Desired WIP',
             color='Scenario',
             color_discrete_sequence=['#1f77b4', '#ff7f0e'],
             text='Number of Items')

# Update the layout
fig.update_layout(
    xaxis_title='Scenario',
    yaxis_title='Number of Items',
    showlegend=False
)

# Update the text position and format
fig.update_traces(textposition='outside', texttemplate='%{text:.2f}')

# Display the chart
fig.show()