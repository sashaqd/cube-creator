import os
import glob
import pandas as pd
import csv

# specify the path to the parent directory
parent_dir_path = '/Users/sasha/desktop/bayanat-data'
column_freq_dict = {}

# loop through each child directory in the parent directory
for child_dir in os.listdir(parent_dir_path):
    # check if the child is a directory
    if os.path.isdir(os.path.join(parent_dir_path, child_dir)):
        # get a list of all excel files in the child directory
        excel_files = glob.glob(os.path.join(parent_dir_path, child_dir, "*.xlsx"))
        # loop through each excel file in the child directory
        for excel_file in excel_files:
            # check if the file name starts with "(metadata)"
            if not excel_file.startswith(os.path.join(parent_dir_path, child_dir, "(metadata)")):

                df = pd.read_excel(excel_file)

                # loop through each column in the dataframe
                for col in df.columns:
                    # check if the column is of string type
                    if isinstance(df[col].iloc[0], str):
                        #  increment its frequency
                        col_lower = col.lower()
                        if col_lower in column_freq_dict:
                            column_freq_dict[col_lower] += 1
                        else:
                            column_freq_dict[col_lower] = 1

# write the final dictionary to a CSV file
with open("column_freq.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Column Name", "Frequency"])
    for key, value in column_freq_dict.items():
        writer.writerow([key, value])
