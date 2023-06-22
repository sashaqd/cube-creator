import csv
from datetime import date
import os

class MetaDataConverter:
    def __init__(self,csv_file_path, meta_file_path, other_meta_file_path, dir, file, version=1):
        self.csv_file_path = csv_file_path
        self.meta_file_path = meta_file_path
        self.other_meta_file_path = other_meta_file_path
        # filename without extension
        self.file_name =  file.split('.')[0].strip()
        self.dir = dir
        self.version = version
        #creating a dictionary of description and tags
        self.metadata_dictionary = self.create_metadata_dictionary()
        self.other_metadata_dictionary = self.create_other_metadata_dictionary()

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

    def generate_metaData(self):
        file_name = self.file_name
        
        dir = self.dir
        if dir in self.metadata_dictionary:
            tags = self.metadata_dictionary[dir]['tags']
            description = self.metadata_dictionary[dir]['description']
        else:
            tags = []
            description = ""

        themes = self.other_metadata_dictionary[dir]["theme"]
        organizations = self.other_metadata_dictionary[dir]["organization"]
        organizations = [name.replace(" ", "") for name in organizations]
        
        metaData = f"BASE <https://citygraph.co/opendata/{file_name}/{self.version}/>\n"
        metaData+= "PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        metaData+= "PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>\n"
        metaData+= "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n"
        metaData+= "PREFIX schema: <http://schema.org/>\n"
        metaData+= "PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n"
        metaData+= "PREFIX cube: <https://cube.link/>\n"
        metaData+= f"PREFIX dimension: <https://citygraph.co/opendata/{file_name}/{self.version}/dimension/>\n"
        metaData+= "PREFIX sh: <http://www.w3.org/ns/shacl#>\n"
        metaData+= "PREFIX meta: <https://cube.link/meta/>\n"
        metaData+= "PREFIX qudt: <http://qudt.org/schema/qudt/>\n"
        metaData+= "PREFIX time: <http://www.w3.org/2006/time#>\n"
        metaData+="\n\n"
      
        metaData += f"<{self.version}> a cube:Cube ;\n"
        for theme in themes:
            metaData += f"  dcat:theme <https://citygraph.co/opendata/theme/{theme}> ;\n"
        metaData += f'  dcterms:description "{description}"@en ;\n'
        metaData += f'  dcterms:title "{dir}"@en ;\n'
        metaData += f'  dcterms:identifier "{dir}"@en ;\n'
        metaData += f'  schema:name "{dir}"@en ;\n'
        metaData += f'  schema:description "{description}"@en ;\n'
        metaData += '  schema:publisher <https://citygraph.co/opendata/cities> ;\n'
        for org in organizations:
            metaData += f'  schema:creator <https://citygraph.co/opendata/{org}> ;\n'
        metaData += '  schema:contactPoint <https://citygraph.co/opendata/cities> ;\n'
        metaData += '  schema:contributor <https://citygraph.co/opendata/cities> ;\n'
        metaData += '  schema:creativeWorkStatus <https://ld.admin.ch/vocabulary/CreativeWorkStatus/Published> ;\n'
        metaData += '  schema:workExample <https://ld.admin.ch/application/visualize> ;\n'
        metaData += '  dcterms:creator <https://citygraph.co/opendata/cities> ;\n'
        metaData += f'  dcterms:issued "{date.today()}"^^xsd:date ;\n'
        metaData += '  dcterms:publisher <https://citygraph.co/opendata/cities> ;\n'
        metaData += f'  schema:dateCreated "{date.today()}"^^xsd:date ;\n'
        metaData += f'  schema:datePublished "{date.today()}"^^xsd:date ;\n'
        metaData += f'  schema:dateModified "{date.today()}"^^xsd:date .\n'     

        return metaData









