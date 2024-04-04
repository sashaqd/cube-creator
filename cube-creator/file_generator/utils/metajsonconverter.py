import json
import csv

class MetaJsonConverter:
    def __init__(self, csv_file_path, file, key_dimensions, data_types, version=1):
        # filename without extension
        self.filename = file.split('.')[0].strip()
        self.csv_file_path = csv_file_path
        self.key_dimensions = key_dimensions
        self.data_types = data_types
        
        # version
        self.version = version

    def generate_json(self):
        file_name = self.filename
        csv_file_path = self.csv_file_path

        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header_row = next(reader)
            column_names = [str(cell) for cell in header_row]
            column_names_wospace = [name.replace(" ", "") for name in column_names]     

        key = ""
        for dim in self.key_dimensions:
            key = key + "{" + dim + "}+" 
        key = key.rstrip("+")
        #key = column_names[0]
        json_data = {
            "@context": "http://www.w3.org/ns/csvw",
            "url": "file:input/{}".format(file_name+".csv"),
            "dialect": {
                "delimiter": ","
            },
            "tableSchema": {
                "aboutUrl": f"https://citygraph.abudhabi.nyu.edu/opendata/{file_name}/{self.version}/{key}",
                "columns": []
            }
        }

        for name, col in zip(column_names, column_names_wospace):
            try:
                column = {
                    "propertyUrl": f"https://citygraph.abudhabi.nyu.edu/opendata/{file_name}/{self.version}/dimension/{col.lower()}",
                    "datatype": self.data_types[col]["data_type"],
                    "titles": name
                }
                json_data["tableSchema"]["columns"].append(column)
            
            except KeyError:
                column = {
                    "propertyUrl": f"https://citygraph.abudhabi.nyu.edu/opendata/{file_name}/{self.version}/measure/{col.lower()}",
                    "datatype": "string",
                    "titles": name
                }
                json_data["tableSchema"]["columns"].append(column)
        
        return json.dumps(json_data, indent=2)


