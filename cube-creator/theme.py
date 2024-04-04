import csv

def create_dataset_dictionary(csv_file_path):
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

# Specify the path to your CSV file
csv_file_path = '/Users/sasha/desktop/bayanat/otherMetadata.csv'
# Call the function to create the dataset dictionary
dataset_dictionary = create_dataset_dictionary(csv_file_path)

# Print the dataset dictionary
for dataset, attributes in dataset_dictionary.items():
    print("Dataset:", dataset)
    print("Attributes:")
    for attribute_type, attribute_name in attributes.items():
        print("- Type:", attribute_type)
        print("- Name:", attribute_name)
    print()


