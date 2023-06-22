from utils.metajsonconverter import MetaJsonConverter
from utils.shapeconverter import ShapeConverter
from utils.metadataconverter import MetaDataConverter
import csv
import os
import openpyxl
import json

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