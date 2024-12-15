import os
import pandas as pd

folder_path = 'C:/Users/yashvi.n/Desktop/salesDataset/output/high_priority_orders.csv'  # Replace with your folder path
output_path = 'C:/Users/yashvi.n/Desktop/salesDataset/output/high_priority_orders.csv/output_file.csv'  # Path where the merged CSV will be saved

all_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# List to hold the dataframes
dfs = []

for file in all_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    dfs.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv(output_path, index=False)
print("Merged CSV file saved to", output_path)
