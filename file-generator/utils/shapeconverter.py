import csv


class ShapeConverter:
    def __init__(self,csv_file_path,file, version=1):

        # filename without extension
        self.csv_file_path = csv_file_path
        self.file_name =  file.split('.')[0].strip()

        # version
        self.version = version

    def generate_shape(self):

        csv_file_path =  self.csv_file_path 
        file_name = self.file_name

        with open(csv_file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            header_row = next(reader)
            column_names = [str(cell) for cell in header_row]

            measure_dimensions = []
            key_dimensions = []

            for column_name in column_names:
                reader = csv.reader(csv_file)
                csv_file.seek(0)
                column_values = [str(row[column_names.index(column_name)]) for row in reader]
                value = column_values[1]
                try:
                    value = float(value)        
                    measure_dimensions.append(column_name)

                except ValueError:
                    key_dimensions.append(column_name)
        
        key_dimensions_wospace = [name.replace(" ", "") for name in key_dimensions]
        measure_dimensions_wospace = [name.replace(" ", "") for name in measure_dimensions]
        
        shape = f"BASE <https://citygraph.co/opendata/{file_name}/{self.version}/>\n"
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
        shape+="\n\n"

        shape += f"<{self.version}> cube:observationConstraint [\n"
        shape += f"  sh:property [\n"
        for dimension , dim_wospace in zip(measure_dimensions,measure_dimensions_wospace):
            shape += f"    a cube:MeasureDimension;\n"
            shape += f"      sh:path dimension:{dim_wospace.lower()};\n"
            shape += f"      schema:name \"{dimension}\"@en;\n"
            shape += f"      qudt:scaleType qudt:RatioScale;\n"
            shape += f"      sh:datatype xsd:decimal\n"
            shape += f"  ],[\n"

        for dimension , dim_wospace in zip(key_dimensions,key_dimensions_wospace):
            shape += f"    a cube:KeyDimension;\n"
            shape += f"      sh:path dimension:{dim_wospace.lower()};\n"
            shape += f"      schema:name \"{dimension}\"@en;\n"
            shape += f"      qudt:scaleType qudt:NominalScale;\n"
            shape += f"      sh:datatype xsd:string\n"
            shape += f"  ],[\n"

        shape = shape.rstrip(",[\n")  # Remove trailing comma and newline
        shape += "\n] ."

        return shape