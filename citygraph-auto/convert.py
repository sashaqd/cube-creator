import csv
import openpyxl
import os
import pandas as pd
import shutil

def create_csv(file_path):
    csv_file_path = file_path.replace('.xlsx', '.csv')
    try:
        data = pd.read_excel(file_path)

        def format_numeric_value(value):
            if pd.notnull(value) and value == int(value):
                return str(int(value))
            return str(value)

        # Convert numeric columns to string format preserving original formatting
        numeric_columns = data.select_dtypes(include=[int, float]).columns
        data[numeric_columns] = data[numeric_columns].applymap(format_numeric_value)

        # Save DataFrame to CSV
        data.to_csv(csv_file_path, index=False)
        return csv_file_path
    except Exception as e:
        pass

# folder_path="file_generator/datasets"
folder_path = "/Users/sasha/desktop/bayanat-staging"

# for root, dirs, files in os.walk(folder_path):
#     for dir in dirs:
#         subfolder_path = os.path.join(root, dir)
#         #if the subfolder is empty remove it
#         if not os.listdir(subfolder_path):
#             os.rmdir(subfolder_path)


for root, dirs, files in os.walk(folder_path):
    for dir in dirs:
        subfolder_path = os.path.join(root, dir)
        for sub_root, sub_dirs, sub_files in os.walk(subfolder_path):
            for file in sub_files:
                csv_file_path = os.path.join(subfolder_path, file)
                if file.endswith(".xlsx"):
                    try:
                        create_csv(csv_file_path)
                        os.remove(csv_file_path)
                    except Exception as e:
                        shutil.rmtree(subfolder_path)
                        print(e)
                        pass


