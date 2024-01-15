import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
data = pd.read_csv("Screentime-App-Details.csv")

# Group by date and app, summing the usage
grouped_data = data.groupby(['Date', 'App']).sum().reset_index()

# Create a grouped bar plot
plt.figure(figsize=(12, 6))
for app, group in grouped_data.groupby('App'):
    plt.bar(group['Date'], group['Usage'], label=app, alpha=0.7, width=0.4)

plt.title("App Usage Over Time")
plt.xlabel("Date")
plt.ylabel("Usage")
plt.legend(title='App')
plt.show()
