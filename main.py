import pandas as pd
import plotly.express as px

# Read the data from the provided CSV format
data = pd.read_csv("original.csv", sep=',')

# Filter data for issues with status "Deployed"
deployed_issues = data[data['status_to_name'] == 'Deployed']

# Convert date columns to datetime format
deployed_issues['issue_created_date'] = pd.to_datetime(deployed_issues['issue_created_date'])
deployed_issues['status_change_date'] = pd.to_datetime(deployed_issues['status_change_date'])

# Calculate lead time for each phase
deployed_issues['prioritized_to_development'] = deployed_issues['status_change_date'] - deployed_issues['issue_created_date']
deployed_issues['development_to_review'] = deployed_issues.groupby('issue_key')['status_change_date'].diff()
deployed_issues['review_to_deployed'] = deployed_issues.groupby('issue_key')['status_change_date'].diff()

# Fill missing values with 0
deployed_issues['prioritized_to_development'] = deployed_issues['prioritized_to_development'].fillna(pd.Timedelta(seconds=0))
deployed_issues['development_to_review'] = deployed_issues['development_to_review'].fillna(pd.Timedelta(seconds=0))
deployed_issues['review_to_deployed'] = deployed_issues['review_to_deployed'].fillna(pd.Timedelta(seconds=0))

# Convert timedelta to days
deployed_issues['prioritized_to_development'] = deployed_issues['prioritized_to_development'].dt.days
deployed_issues['development_to_review'] = deployed_issues['development_to_review'].dt.days
deployed_issues['review_to_deployed'] = deployed_issues['review_to_deployed'].dt.days

# Group by issue type and calculate the sum of lead times for each phase
lead_time_data = deployed_issues.groupby('issue_type_name').agg({
    'prioritized_to_development': 'sum',
    'development_to_review': 'sum',
    'review_to_deployed': 'sum'
}).reset_index()

# Melt the data to create a long format suitable for stacked column chart
lead_time_data_melted = pd.melt(lead_time_data, id_vars=['issue_type_name'], 
                                value_vars=['prioritized_to_development', 'development_to_review', 'review_to_deployed'],
                                var_name='phase', value_name='lead_time')

# Create a stacked column chart using Plotly Express
fig = px.bar(lead_time_data_melted, x='issue_type_name', y='lead_time', color='phase', 
             title='Lead Time Breakdown by Issue Type',
             labels={'issue_type_name': 'Issue Type', 'lead_time': 'Lead Time (Days)'},
             color_discrete_sequence=px.colors.sequential.YlOrRd)

# Update the layout
fig.update_layout(xaxis={'categoryorder': 'category ascending'}, 
                  legend_title='Phase', 
                  legend={'traceorder': 'normal'})

# Display the chart
fig.show()