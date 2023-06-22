from utils.metajsonconverter import MetaJsonConverter
from utils.shapeconverter import ShapeConverter
from utils.metadataconverter import MetaDataConverter
import csv
import os
import openpyxl
import json

def convert_to_csv(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    csv_file_path = file_path.replace('.xlsx', '.csv')
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for row in sheet.iter_rows(values_only=True):
            writer.writerow(row)
    return csv_file_path


other_meta_file_path = '/Users/sasha/desktop/bayanat/otherMetadata.csv'
meta_file_path = '/Users/sasha/desktop/bayanat/metadata.csv'
folder_path = '/Users/sasha/desktop/b'


f1 = open("new_json.ttl", "w")
f2 = open("new_shape.ttl", "w")
f3 = open("new_metadata.ttl", "w")
for root, dirs, files in os.walk(folder_path):
    for dir in dirs:
        subfolder_path = os.path.join(root, dir)
        for sub_root, sub_dirs, sub_files in os.walk(subfolder_path):
            for file in sub_files:
                if file.endswith('.xlsx'):
                    file_path = os.path.join(subfolder_path, file)
                    csv_file_path = convert_to_csv(file_path)
                    json = MetaJsonConverter(csv_file_path, file).generate_json()
                    shape = ShapeConverter(csv_file_path, file).generate_shape()
                    metadata = MetaDataConverter(csv_file_path, meta_file_path, other_meta_file_path, dir, file).generate_metaData()
                    f1.write(json)
                    f2.write(shape)
                    f3.write(metadata)
                    os.remove(csv_file_path)  # Remove the temporary CSV file
f1.close()
f2.close()
f3.close()