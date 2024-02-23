import pandas as pd
import re

def parse_log_file(log_file):
    # Regular expression to extract relevant parts of the log
    regex = r"\[(.*?)\] \[INFO\] ({.*?})"

    records = []

    with open(log_file, "r") as file:
        for line in file:
            match = re.search(regex, line)
            if match:
                thread_info, data = match.groups()
                thread_name, thread_function = thread_info.split(" ", 1)
                data_dict = eval(data)  # Convert string representation of dict to actual dict
                data_dict["Thread Name"] = thread_name
                data_dict["Thread Function"] = thread_function
                records.append(data_dict)

    return pd.DataFrame(records)

# Path to the log file
log_file = 'mul_client.log'

# Parse the log file and create a DataFrame
df = parse_log_file(log_file)

# Display the first few rows of the DataFrame
print(df.head())

# Example analysis: Calculate the average transmission speed
average_transmission_speed = df["Transmission Speed (bps)"].mean()
print(f"Average Transmission Speed: {average_transmission_speed} bps")
