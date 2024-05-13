import pandas as pd
import plotly.express as px

# Read the data from the "original.csv" file
data = pd.read_csv("original.csv")

# Convert date columns to datetime format
data['issue_created_date'] = pd.to_datetime(data['issue_created_date'])
data['status_change_date'] = pd.to_datetime(data['status_change_date'])

# Calculate the current WIP and Cycle Time
current_wip = data['issue_key'].nunique()
cycle_time_data = data[data['status_to_name'] == 'Deployed'].groupby('issue_key').agg({
    'issue_created_date': 'min',
    'status_change_date': 'max'
})
cycle_time_data['cycle_time'] = (cycle_time_data['status_change_date'] - cycle_time_data['issue_created_date']).dt.days
current_cycle_time = cycle_time_data['cycle_time'].mean()

# Set the desired Cycle Time
desired_cycle_time = 15

# Calculate the current Throughput and desired WIP
current_throughput = current_wip / current_cycle_time
desired_wip = current_throughput * desired_cycle_time

# Create a DataFrame for the WIP chart
wip_chart_data = pd.DataFrame({
    'Scenario': ['Current WIP', 'Desired WIP'],
    'Number of Items': [current_wip, desired_wip]
})

# Create a bar chart for WIP using Plotly Express
wip_fig = px.bar(wip_chart_data, x='Scenario', y='Number of Items',
                 title='Current vs Desired WIP',
                 color='Scenario',
                 color_discrete_sequence=['#1f77b4', '#ff7f0e'],
                 text='Number of Items')

# Update the layout of the WIP chart
wip_fig.update_layout(
    xaxis_title='Scenario',
    yaxis_title='Number of Items',
    showlegend=False
)

# Update the text position and format of the WIP chart
wip_fig.update_traces(textposition='outside', texttemplate='%{text:.2f}')

# Calculate the throughput rate per day
throughput_data = data[data['status_to_name'] == 'Deployed']
throughput_data['date'] = throughput_data['status_change_date'].dt.date
throughput_rate = throughput_data.groupby('date').size().mean()

print(f"Throughput Rate: {throughput_rate:.2f} items per day")

# Calculate the arrival rate of items per day
arrival_data = data.groupby(data['issue_created_date'].dt.date).size().reset_index(name='count')
arrival_rate = arrival_data['count'].mean()

print(f"Arrival Rate: {arrival_rate:.2f} items per day")

# Create a DataFrame for the throughput and arrival rate chart
rate_chart_data = pd.DataFrame({
    'Rate': ['Throughput Rate', 'Arrival Rate'],
    'Items per Day': [throughput_rate, arrival_rate]
})

# Create a bar chart for throughput and arrival rate using Plotly Express
rate_fig = px.bar(rate_chart_data, x='Rate', y='Items per Day',
                  title='Throughput Rate vs Arrival Rate',
                  color='Rate',
                  color_discrete_sequence=['#2ca02c', '#d62728'],
                  text='Items per Day')

# Update the layout of the rate chart
rate_fig.update_layout(
    xaxis_title='Rate',
    yaxis_title='Items per Day',
    showlegend=False
)

# Update the text position and format of the rate chart
rate_fig.update_traces(textposition='outside', texttemplate='%{text:.2f}')

# Display the charts
wip_fig.show()
rate_fig.show()