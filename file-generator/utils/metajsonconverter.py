import json
import csv

class MetaJsonConverter:
    def __init__(self, csv_file_path, file, key_dimensions, version=1):
        # filename without extension
        self.filename = file.split('.')[0].strip()
        self.csv_file_path = csv_file_path
        self.key_dimensions = key_dimensions
        
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

            data_types = []

            for column_name in column_names:
                reader = csv.reader(csv_file)
                csv_file.seek(0)
                column_values = [str(row[column_names.index(column_name)]) for row in reader]
                value = column_values[1]
                try:
                    value = float(value)
                    data_types.append("decimal")

                except ValueError:
                    data_types.append("string")

        key = ""
        # self.key_dimensions = [name.replace(" ", "") for name in self.key_dimensions]
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
                "aboutUrl": f"https://citygraph.co/opendata/{file_name}/{self.version}/{key}",
                "columns": []
            }
        }

        for name, data_type, col in zip(column_names, data_types, column_names_wospace):
            column = {
                "propertyUrl": f"https://citygraph.co/opendata/{file_name}/{self.version}/dimension/{col.lower()}",
                "datatype": data_type,
                "titles": name
            }
            json_data["tableSchema"]["columns"].append(column)
        
        return json.dumps(json_data, indent=2)


