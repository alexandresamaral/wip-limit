import pandas as pd
import plotly.express as px

# Read the data from the provided CSV format
data = pd.read_csv("original.csv", sep=',')

# Convert date columns to datetime format
data['issue_created_date'] = pd.to_datetime(data['issue_created_date'])
data['status_change_date'] = pd.to_datetime(data['status_change_date'])

# Create a dictionary to map status names to categories
status_categories = {
    'To Do': 'To Do',
    'Prioritized': 'To Do',
    'In Progress': 'In Progress',
    'Review': 'In Progress',
    'Deployed': 'Done',
    "Can't Fix": 'Done',
    'Accepted': 'In Progress'
}

# Map status names to categories
data['status_category'] = data['status_to_name'].map(status_categories)

# Group by status change date and status category, and count the number of issues
cfd_data = data.groupby(['status_change_date', 'status_category']).size().reset_index(name='count')

# Pivot the data to create columns for each status category
cfd_data_pivoted = cfd_data.pivot(index='status_change_date', columns='status_category', values='count')

# Fill missing values with 0 and cumulate the count
cfd_data_pivoted = cfd_data_pivoted.fillna(0).cumsum()

# Reset the index to make status_change_date a regular column
cfd_data_pivoted = cfd_data_pivoted.reset_index()

# Create a CFD chart using Plotly Express
fig = px.area(cfd_data_pivoted, x='status_change_date', y=cfd_data_pivoted.columns[1:],
              title='Cumulative Flow Diagram',
              labels={'status_change_date': 'Date', 'value': 'Number of Issues'},
              color_discrete_sequence=px.colors.qualitative.Plotly)

# Update the layout
fig.update_layout(xaxis_title='Date', yaxis_title='Number of Issues', legend_title='Status Category')

# Display the chart
fig.show()

# Identify the bottleneck phase
bottleneck_phase = cfd_data_pivoted.iloc[-1, 1:].idxmax()
print(f"The bottleneck phase is: {bottleneck_phase}")