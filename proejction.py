import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Read the data from the "original.csv" file
data = pd.read_csv("original.csv")

# Convert date columns to datetime format
data['issue_created_date'] = pd.to_datetime(data['issue_created_date'])
data['status_change_date'] = pd.to_datetime(data['status_change_date'])

# Calculate the throughput rate per day
throughput_data = data[data['status_to_name'] == 'Deployed']
throughput_data['date'] = throughput_data['status_change_date'].dt.date
throughput_rate = throughput_data.groupby('date').size().mean()

print(f"Throughput Rate: {throughput_rate:.2f} items per day")

# Set the number of items in the backlog and the number of blocked items
backlog_items = 40
blocked_items = 3

# Set the number of simulations to run
num_simulations = 1000

# Perform Monte Carlo simulation
completion_dates = []
for _ in range(num_simulations):
    remaining_items = backlog_items
    blocked_days = np.random.choice([0, 7], size=blocked_items).sum()
    days_to_complete = int(blocked_days)  # Convert to regular Python integer
    while remaining_items > 0:
        completed_items = min(remaining_items, np.random.poisson(throughput_rate))
        remaining_items -= completed_items
        days_to_complete += 1
    completion_date = datetime.now().date() + timedelta(days=days_to_complete)
    completion_dates.append(completion_date)

# Calculate the 95th percentile completion date
percentile_95 = np.percentile(completion_dates, 95, interpolation='nearest')
percentile_95_date = pd.to_datetime(percentile_95).date()

print(f"95th Percentile Completion Date: {percentile_95_date}")

# Calculate the number of working days from now until the 95th percentile completion date
working_days = np.busday_count(datetime.now().date(), percentile_95_date)

# Calculate the best WIP based on the number of developers and QA
num_developers = 5
num_qa = 2
best_wip = (num_developers + num_qa) * 2

# Create a DataFrame for the WIP and throughput rate
wip_data = pd.DataFrame({'WIP': [best_wip], 'Throughput Rate': [throughput_rate]})

# Create a bar chart using Plotly Express
fig = px.bar(wip_data, x='WIP', y='Throughput Rate',
             title=f'Best WIP to Achieve 40 Items in Backlog by {percentile_95_date}',
             color_discrete_sequence=['#1f77b4'])

# Update the layout
fig.update_layout(
    xaxis_title='WIP',
    yaxis_title='Throughput Rate (items per day)',
    showlegend=False
)

# Display the chart
fig.show()