from utils.metajsonconverter import MetaJsonConverter
from utils.shapeconverter import ShapeConverter
from utils.metadataconverter import MetaDataConverter
import csv
import os
import json
import sys


class dic_generator:
    def __init__(self,meta_file_path, other_meta_file_path, org_file_path, link_file_path ):
        self.meta_file_path = meta_file_path
        self.other_meta_file_path = other_meta_file_path
        self.org_file_path = org_file_path
        self.link_file_path = link_file_path

    def create_metadata_dictionary(self):
        csv_file_path = self.meta_file_path
        metadata = {}
        with open(csv_file_path, newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the header row
            for row in reader:
                folder_name = row[0]  # Assuming folder name is in the first column
                description = row[1]
                tags = [row[i] for i in range(2, len(row))]
                metadata[folder_name] = {"description":description, "tags":tags}
        return metadata

    def create_other_metadata_dictionary(self):
        csv_file_path = self.other_meta_file_path
        dataset_dict = {}
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                attribute_type = row[0]
                attribute_name = row[1]

                for dataset in row[2:]:
                    if dataset not in dataset_dict:
                        dataset_dict[dataset] = {}
                        dataset_dict[dataset]["theme"] = []
                        dataset_dict[dataset]["organization"] = []
                        dataset_dict[dataset]["goal"] = []
                    
                    dataset_dict[dataset][attribute_type].append(attribute_name)
        return dataset_dict

    def create_org_dictionary(self):
        data_dict = {}
        with open(self.org_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                org = row['Org']
                website = row['Website']
                abbreviation = row['Abbreviation']
                data_dict[org] = {'Website': website, 'Abbreviation': abbreviation}
        return data_dict
    
    def get_abbreviation(self, dir):
        other_meta_dictionary = self.create_other_metadata_dictionary()
        org_dictionary = self.create_org_dictionary()
        org = other_meta_dictionary[dir]["organization"]
        return org_dictionary[org[0]]['Abbreviation']

    def create_link_dictionary(self):
        data_dict = {}
        with open(self.link_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                pos = row['Position']
                title = row['title']
                link = row['link']
                data_dict[title] = { 'link': link}
        return data_dict



class file_generator: 
    def __init__(self,dir, file, csv_file_path, meta_dictionary, other_meta_dictionary, org_dictionary, link_dictionary):
        self.dir = dir
        self.file = file
        self.csv_file_path = csv_file_path
        self.meta_dictionary = meta_dictionary 
        self.other_meta_dictionary = other_meta_dictionary
        self.org_dictionary = org_dictionary
        self.link_dictionary = link_dictionary

    def generate(self):
        f1 = open("test.csv.meta.json", "w") 
        f2 = open("shape.ttl", "w")
        f3 = open("metadata.ttl", "w")
                
        shape_obj = ShapeConverter(self.csv_file_path, self.file)
        shape = shape_obj.generate_shape()
        key_dimensions = shape_obj.get_key_dimensions()
        data_types = shape_obj.get_data_types()
        
        json = MetaJsonConverter(self.csv_file_path, self.file, key_dimensions, data_types).generate_json()
        metadata = MetaDataConverter(self.dir, self.file, self.csv_file_path, self.meta_dictionary, self.other_meta_dictionary, self.org_dictionary, self.link_dictionary).generate_metaData()

        f1.write(json)
        f2.write(shape)
        f3.write(metadata)
        f1.close()
        f2.close()
        f3.close()


csv_file_path = sys.argv[1] #"file_generator/datasets/Key Statistics of Oil and Gas Activity/KeyStatisticsofOilandGasActivity.csv"
directory, file = os.path.split(csv_file_path)
directory, dir = os.path.split(directory)

other_meta_file_path = 'file_generator/datasets/otherMetadata.csv'
meta_file_path = 'file_generator/datasets/metadata.csv'
org_file_path = 'file_generator/datasets/organizations.csv'
link_file_path = 'file_generator/datasets/links.csv'

meta_dic = dic_generator(meta_file_path,other_meta_file_path,org_file_path, link_file_path).create_metadata_dictionary()
other_meta_dic = dic_generator(meta_file_path,other_meta_file_path,org_file_path, link_file_path).create_other_metadata_dictionary()
org_dic = dic_generator(meta_file_path,other_meta_file_path,org_file_path, link_file_path).create_org_dictionary()
link_dic = dic_generator(meta_file_path,other_meta_file_path,org_file_path, link_file_path).create_link_dictionary()
file_generator(dir, file, csv_file_path, meta_dic, other_meta_dic, org_dic, link_dic).generate()

abr = dic_generator(meta_file_path,other_meta_file_path,org_file_path, link_file_path).get_abbreviation(dir)
with open('abr.txt', 'w') as f:
    f.write(abr)
