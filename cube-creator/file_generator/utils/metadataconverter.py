import csv
from datetime import date
import os

class MetaDataConverter:
    def __init__(self , dir, file,csv_file_path, meta_dictionary, other_meta_dictionary, org_dictionay, link_dictionary, version=1):
        self.csv_file_path = csv_file_path
        # filename without extension
        self.file_name =  file.split('.')[0].strip()
        self.dir = dir
        self.version = version
        #creating a dictionary of description and tags
        self.metadata_dictionary = meta_dictionary
        self.other_metadata_dictionary = other_meta_dictionary
        self.org_dictionary = org_dictionay
        self.link_dictionary = link_dictionary
    

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
        themes = [name.replace(" ", "") for name in themes]
        organizations = self.other_metadata_dictionary[dir]["organization"]
        organizations_wspace = organizations
        organizations = [name.replace(" ", "") for name in organizations]
        
        metaData = f"BASE <https://citygraph.abudhabi.nyu.edu/opendata/{file_name}/>\n"
        metaData+= "PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        metaData+= "PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>\n"
        metaData+= "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n"
        metaData+= "PREFIX schema: <http://schema.org/>\n"
        metaData+= "PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n"
        metaData+= "PREFIX cube: <https://cube.link/>\n"
        metaData+= f"PREFIX dimension: <https://citygraph.abudhabi.nyu.edu/opendata/{file_name}/{self.version}/dimension/>\n"
        metaData+= "PREFIX sh: <http://www.w3.org/ns/shacl#>\n"
        metaData+= "PREFIX meta: <https://cube.link/meta/>\n"
        metaData+= "PREFIX qudt: <http://qudt.org/schema/qudt/>\n"
        metaData+= "PREFIX time: <http://www.w3.org/2006/time#>\n"
        metaData+= "PREFIX dcat: <http://www.w3.org/ns/dcat#>\n"
        metaData+= "PREFIX dcterms: <http://purl.org/dc/terms/>\n"
        metaData+="\n\n"
      
        metaData += f"<{self.version}> a cube:Cube ;\n"
        metaData += f'  dcterms:description "{description}"@en ;\n'
        metaData += f'  dcterms:title "{dir}"@en ;\n'
        metaData += f'  dcterms:identifier "{dir}"@en ;\n'
        metaData += f'  schema:name "{dir}"@en ;\n'
        metaData += f'  schema:description "{description}"@en ;\n'
        for theme in themes:
            metaData += f"  dcat:theme <https://citygraph.abudhabi.nyu.edu/opendata/theme/{theme}> ;\n"
        for org in organizations_wspace:
            metaData += f'  schema:publisher "{org}"@en ;\n'
        for org in organizations:
            metaData += f'  schema:creator <https://citygraph.abudhabi.nyu.edu/opendata/{org}> ;\n'
        for org in organizations:
            metaData += f'  dcterms:creator <https://citygraph.abudhabi.nyu.edu/opendata/{org}> ;\n'
        metaData += f'  dcterms:issued "{date.today()}"^^xsd:date ;\n'
        for org in organizations_wspace:
            metaData += f'  dcterms:publisher "{org}"@en ;\n'
        metaData += '  schema:contributor <https://citygraph.abudhabi.nyu.edu/opendata/cities> ;\n'
        metaData += '  schema:creativeWorkStatus <https://ld.admin.ch/vocabulary/CreativeWorkStatus/Published> ;\n'
        metaData += '  schema:workExample <https://ld.admin.ch/application/visualize> ;\n'
        try:
            link = self.link_dictionary[dir]['link']
        except:
            link = ""
        metaData += f'  dcat:landingPage "{link}"^^xsd:string ;\n'
        metaData += f'  schema:dateCreated "{date.today()}"^^xsd:date ;\n'
        metaData += f'  schema:datePublished "{date.today()}"^^xsd:date ;\n'
        metaData += f'  schema:version "{self.version}"^^xsd:integer ;\n'
        metaData += f'  schema:dateModified "{date.today()}"^^xsd:date .\n'  
        metaData += f"\n\n<https://citygraph.abudhabi.nyu.edu/opendata/{file_name}/{self.version}> <http://www.w3.org/ns/dcat#contactPoint> [\n"
        metaData += "  a <http://www.w3.org/2006/vcard/ns#Organization> ;\n"
        metaData += "  <http://www.w3.org/2006/vcard/ns#fn> \"Bayanat.ae\" ;\n"
        metaData += "  <http://www.w3.org/2006/vcard/ns#hasEmail> \"contact@bayanat.ae\"\n"
        metaData += "] ."   

        return metaData









