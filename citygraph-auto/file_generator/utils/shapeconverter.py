import csv
import os
import openai


class ShapeConverter:
    def __init__(self,csv_file_path,file, version=1):
        # filename without extension
        self.csv_file_path = csv_file_path
        self.file_name =  file.split('.')[0].strip()
        # version
        self.version = version
        # self.measure_dimensions = []
        self.key_dimensions = []
        self.write_shape()
        self.shape_dict = self.create_shape_dict()
    
    def get_key_dimensions(self):
        for col in self.shape_dict:
            if self.shape_dict[col]['dimension'] == 'KeyDimension':
                self.key_dimensions.append(col)
        return self.key_dimensions

    def get_data_types(self):
        data_types = {}
        for col in self.shape_dict:
            data_types[col] = {"data_type": self.shape_dict[col]['data_type']}
        return data_types

    # def generate_shape(self):

    #     csv_file_path =  self.csv_file_path 
    #     file_name = self.file_name

    #     with open(csv_file_path, 'r') as csv_file:
    #         reader = csv.reader(csv_file)
    #         header_row = next(reader)
    #         column_names = [str(cell) for cell in header_row]
           
    #         for column_name in column_names:
    #             reader = csv.reader(csv_file)
    #             csv_file.seek(0)
    #             column_values = [str(row[column_names.index(column_name)]) for row in reader]
    #             value = column_values[1]
    #             try:
    #                 value = float(value)
    #                 self.measure_dimensions.append(column_name)

    #             except ValueError:
    #                 self.key_dimensions.append(column_name)
        
    #     key_dimensions_wospace = [name.replace(" ", "") for name in self.key_dimensions]
    #     measure_dimensions_wospace = [name.replace(" ", "") for name in self.measure_dimensions]
        
    #     shape = f"BASE <https://citygraph.co/opendata/{file_name}/>\n"
    #     shape+= "PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
    #     shape+= "PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>\n"
    #     shape+= "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n"
    #     shape+= "PREFIX schema: <http://schema.org/>\n"
    #     shape+= "PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n"
    #     shape+= "PREFIX cube: <https://cube.link/>\n"
    #     shape+= f"PREFIX dimension: <https://citygraph.co/opendata/{file_name}/{self.version}/dimension/>\n"
    #     shape+= "PREFIX sh: <http://www.w3.org/ns/shacl#>\n"
    #     shape+= "PREFIX meta: <https://cube.link/meta/>\n"
    #     shape+= "PREFIX qudt: <http://qudt.org/schema/qudt/>\n"
    #     shape+= "PREFIX time: <http://www.w3.org/2006/time#>\n"
    #     shape+= "PREFIX dcat: <http://www.w3.org/ns/dcat#>\n"
    #     shape+= "PREFIX dcterms: <http://purl.org/dc/terms/>\n"
    #     shape+="\n\n"

    #     shape += f"<{self.version}> cube:observationConstraint [\n"
    #     shape += f"  sh:property [\n"
    #     for dimension , dim_wospace in zip(self.measure_dimensions,measure_dimensions_wospace):
    #         shape += f"    a cube:MeasureDimension;\n"
    #         shape += f"      sh:path dimension:{dim_wospace.lower()};\n"
    #         shape += f"      schema:name \"{dimension}\"@en;\n"
    #         shape += f"      qudt:scaleType qudt:RatioScale;\n"
    #         shape += f"      sh:datatype xsd:decimal\n"
    #         shape += f"  ],[\n"

    #     for dimension , dim_wospace in zip(self.key_dimensions,key_dimensions_wospace):
    #         shape += f"    a cube:KeyDimension;\n"
    #         shape += f"      sh:path dimension:{dim_wospace.lower()};\n"
    #         shape += f"      schema:name \"{dimension}\"@en;\n"
    #         shape += f"      qudt:scaleType qudt:NominalScale;\n"
    #         shape += f"      sh:datatype xsd:string\n"
    #         shape += f"  ],[\n"

    #     shape = shape.rstrip(",[\n")  # Remove trailing comma and newline
    #     shape += "\n] ."

    #     return shape

    def write_shape(self):
        with open(self.csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            rows = []
            for i, row in enumerate(csv_reader):
                if i < 2:  # Get only the first two rows
                    rows.append(row)
                else:
                    break
            string =  '\n'.join([','.join(row) for row in rows])
            openai.api_key = ""
            message = "classify the type of columns based on scale(ratio/interval/ordinal/nominal) , classify if it should be a (key dimension/measure dimension) , classify it's data type (string/integer/decimal) for the given input, the output should be printed as a csv (column,scale,dimension,data type) : "
            message += string
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "user", "content": message},
                ]
            )
            data = response['choices'][0]['message']['content']
            # print(response)
            filename = "shape_data.txt"
            with open(filename, 'w') as file:
                for row in data:
                    file.write(row)
            file.close()

    def create_shape_dict(self): 
        filename = "shape_data.txt"   
        dict = {}
        flag = 0
        with open(filename, 'r') as file:
            data = file.readlines()
            for row in data:
                if flag != 0: 
                    row = row.split(",")
                    scale = "RatioScale" if "ratio" in row[1].lower() else "IntervalScale" if "interval" in row[1].lower() else "OrdinalScale" if "ordinal" in row[1].lower() else "NominalScale"
                    dimension = "MeasureDimension" if "measure" in row[2].lower() else "KeyDimension"
                    type = row[3].replace(" ", "").lower().rstrip('\n')
                    dict[row[0]] = {'scale':scale,'dimension':dimension,'data_type':type}
                flag = 1  
            file.close()
            return dict

    def generate_shape(self):

        file_name = self.file_name
        shape = f"BASE <https://citygraph.co/opendata/{file_name}/>\n"
        shape+= "PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n"
        shape+= "PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>\n"
        shape+= "PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>\n"
        shape+= "PREFIX schema: <http://schema.org/>\n"
        shape+= "PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n"
        shape+= "PREFIX cube: <https://cube.link/>\n"
        shape+= f"PREFIX dimension: <https://citygraph.co/opendata/{file_name}/{self.version}/dimension/>\n"
        shape+= "PREFIX sh: <http://www.w3.org/ns/shacl#>\n"
        shape+= "PREFIX meta: <https://cube.link/meta/>\n"
        shape+= "PREFIX qudt: <http://qudt.org/schema/qudt/>\n"
        shape+= "PREFIX time: <http://www.w3.org/2006/time#>\n"
        shape+= "PREFIX dcat: <http://www.w3.org/ns/dcat#>\n"
        shape+= "PREFIX dcterms: <http://purl.org/dc/terms/>\n"
        shape+="\n\n"

        shape += f"<{self.version}> cube:observationConstraint [\n"
        shape += f"  sh:property [\n"
        for col in self.shape_dict:
            shape += f"    a cube:{self.shape_dict[col]['dimension']};\n"
            col_name_wospace = col.replace(" ", "") 
            col_name_wospace = col_name_wospace.lower()
            shape += f"      sh:path dimension:{col_name_wospace};\n"
            shape += f"      schema:name \"{col}\"@en;\n"
            shape += f"      qudt:scaleType qudt:{self.shape_dict[col]['scale']};\n"
            shape += f"      sh:datatype xsd:{self.shape_dict[col]['data_type']}\n"
            shape += f"  ],[\n"

        shape = shape.rstrip(",[\n")  # Remove trailing stuff
        shape += "\n] ."

        return shape

          




