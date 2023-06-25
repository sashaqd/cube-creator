import csv
import openpyxl
import os

def create_csv(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    csv_file_path = file_path.replace('.xlsx', '.csv')

    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in sheet.iter_rows(values_only=True):
            writer.writerow(row)

    return csv_file_path

folder_path="file_generator/datasets"

# for root, dirs, files in os.walk(folder_path):
#     for dir in dirs:
#         subfolder_path = os.path.join(root, dir)
#         for sub_root, sub_dirs, sub_files in os.walk(subfolder_path):
#             for file in sub_files:
#                 csv_file_path = os.path.join(subfolder_path, file)
#                 csv_file_path = create_csv(csv_file_path)




