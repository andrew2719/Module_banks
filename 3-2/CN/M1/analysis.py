import re
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to your log file
log_file_path = 'mul_client.log'

# Regular expression to parse the log
log_pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) \[Thread-(\d+) .+\] \[INFO\] ({.+})'

# Parsing log data
parsed_data = []
with open(log_file_path, 'r') as file:
    for line in file:
        match = re.match(log_pattern, line)
        if match:
            timestamp, thread, metrics = match.groups()
            metrics_dict = eval(metrics)
            metrics_dict['Thread'] = 'Thread-' + thread
            parsed_data.append(metrics_dict)

# Convert to DataFrame
df = pd.DataFrame(parsed_data)

# Convert numeric columns to the correct data type
numeric_columns = ['Transmission Speed (bps)', 'Transmission Delay (s)', 
                   'Propagation Delay (s)', 'Round Trip Time (s)', 
                   'End-to-End Delay (s)']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric)

# Calculating averages for each metric across all threads
overall_average_metrics = df[numeric_columns].mean()

# Display the overall averages
print("Overall Averages:")
print(overall_average_metrics)

# Plotting the average Transmission Speed for each thread
plt.figure(figsize=(12, 6))
sns.barplot(x='Thread', y='Transmission Speed (bps)', data=df)
plt.title('Average Transmission Speed per Thread')
plt.xticks(rotation=45)
plt.show()

# Plotting the average End-to-End Delay for each thread
plt.figure(figsize=(12, 6))
sns.barplot(x='Thread', y='End-to-End Delay (s)', data=df)
plt.title('Average End-to-End Delay per Thread')
plt.xticks(rotation=45)
plt.show()
