from utils.metajsonconverter import MetaJsonConverter
from utils.shapeconverter import ShapeConverter
from utils.metadataconverter import MetaDataConverter
import csv
import os
import openpyxl
import json

def add_index_column(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Add the "Index" column header to the first row
    data[0].insert(0, "Index")
    # Add row numbers to each row
    for i in range(1, len(data)):
        data[i].insert(0, i)

    # Open the same CSV file in write mode
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def remove_index_column(csv_file_path):
    with open(csv_file_path, 'r') as file:
        # Read the existing data from the CSV file
        reader = csv.reader(file)
        data = list(reader)

    # Check if the "Index" column exists in the first row
    if "Index" in data[0]:
        index_column_index = data[0].index("Index")
        for row in data:
            del row[index_column_index]

        with open(csv_file_path, 'w', newline='') as file:
            # Write the modified data back to the CSV file
            writer = csv.writer(file)
            writer.writerows(data)

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
                csv_file_path = os.path.join(subfolder_path, file)
                # add_index_column(csv_file_path)
                shape_obj = ShapeConverter(csv_file_path, file)
                shape = shape_obj.generate_shape()
                key_dimensions = shape_obj.get_key_dimensions()
                json = MetaJsonConverter(csv_file_path, file, key_dimensions).generate_json()
                
                metadata = MetaDataConverter(csv_file_path, meta_file_path, other_meta_file_path, dir, file).generate_metaData()
                # remove_index_column(csv_file_path)
                f1.write(json)
                f2.write(shape)
                f3.write(metadata)
f1.close()
f2.close()
f3.close()