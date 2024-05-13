import pandas as pd
import plotly.express as px

# Read the data from the provided CSV format
data = pd.read_csv("original.csv", sep=',')

# Convert date columns to datetime format
data['issue_created_date'] = pd.to_datetime(data['issue_created_date'])
data['status_change_date'] = pd.to_datetime(data['status_change_date'])

# Remove the "In Preparation" status
data = data[data['status_to_name'] != 'In Preparation']

# Group by status change date and status name, and count the number of issues
cfd_data = data.groupby(['status_change_date', 'status_to_name']).size().reset_index(name='count')

# Pivot the data to create columns for each status name
cfd_data_pivoted = cfd_data.pivot(index='status_change_date', columns='status_to_name', values='count')

# Fill missing values with 0 and cumulate the count
cfd_data_pivoted = cfd_data_pivoted.fillna(0).cumsum()

# Reset the index to make status_change_date a regular column
cfd_data_pivoted = cfd_data_pivoted.reset_index()

# Specify the desired order of statuses
status_order = ['To Do', 'Prioritized', 'In Progress', 'Review', 'Accepted', "Can't Fix", 'Deployed']

# Reorder the columns based on the specified status order
cfd_data_pivoted = cfd_data_pivoted[['status_change_date'] + status_order]

# Create a CFD chart using Plotly Express
fig = px.area(cfd_data_pivoted, x='status_change_date', y=status_order,
              title='Cumulative Flow Diagram (Optimized)',
              labels={'status_change_date': 'Date', 'value': 'Number of Issues'},
              color_discrete_sequence=px.colors.qualitative.Plotly)

# Update the layout
fig.update_layout(xaxis_title='Date', yaxis_title='Number of Issues', legend_title='Status')

# Display the chart
fig.show()

# Identify the bottleneck phase
bottleneck_phase = cfd_data_pivoted.iloc[-1, 1:].idxmax()
print(f"The bottleneck phase is: {bottleneck_phase}")

# Calculate the average time spent in the bottleneck phase
bottleneck_data = data[data['status_to_name'] == bottleneck_phase]
bottleneck_time = (bottleneck_data['status_change_date'] - bottleneck_data['issue_created_date']).dt.days.mean()
print(f"Average time spent in the bottleneck phase ({bottleneck_phase}): {bottleneck_time:.2f} days")

# Suggest actions to reduce lead time
print("Suggestions to reduce lead time:")
print(f"1. Focus on resolving issues in the bottleneck phase ({bottleneck_phase}) to improve flow.")
print("2. Consider removing the 'In Preparation' status if it doesn't add significant value to the process.")
print("3. Analyze the reasons for issues being stuck in the bottleneck phase and address any blockers.")
print("4. Encourage collaboration and communication among team members to expedite issue resolution.")