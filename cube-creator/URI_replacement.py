import csv

def create_name_file(replacement_dic):
    new_file = 'name.nt'
    with open(new_file, 'w') as f:
        for key, value in replacement_dic.items():
            f.write(f'<{value}> <http://schema.org/name> "{key}" .\n')


def replace_keys_place_holder_file(replacement_dic):
    new_dic = {}
    for key, value in replacement_dic.items():
        new_dic['\"' + key + '\"'] = '<' + value + '>'

    output_file = 'output/place_holder.nt'
    with open(output_file, 'r') as file:
        file_contents = file.read()

    for key, value in new_dic.items():
        if key in file_contents:
            file_contents = file_contents.replace(key, value)
        else:
            print(f'Key not found: {key}')

    with open(output_file, 'w') as file:
        file.write(file_contents)

    print('Replacement completed')

def replace_from_name_file():
    file = 'name.nt'
    replacement_dic = {}
    for line in csv.reader(open(file), delimiter=' '):
        if len(line) > 0:
            replacement_dic[line[2].strip('"')] = line[0]
    
    new_dic = {}
    for key, value in replacement_dic.items():
        new_dic['\"' + key + '\"'] = value 

    output_file = 'output/place_holder.nt'
    with open(output_file, 'r') as file:
        file_contents = file.read()

    for key, value in new_dic.items():
        if key in file_contents:
            file_contents = file_contents.replace(key, value)
        else:
            print(f'Key not found: {key}')

    with open(output_file, 'w') as file:
        file.write(file_contents)

    print('Replacement completed')

def create_replacement_dic():
    file = input('Enter the file name: ')
    replacement_dic = {}
    for line in csv.reader(open(file)):
        for i in range(len(line)):
            if i + 1 < len(line) and line[i+1].startswith('https://'):
                replacement_dic[line[i]] = line[i+1]
    return replacement_dic


# replacement_dic = create_replacement_dic()
# create_name_file(replacement_dic)
# replace_keys_place_holder_file(replacement_dic)

replace_from_name_file()

