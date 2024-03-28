import csv
import openai
import os

obs_count = 0
count = 0

def classify(csv_path):
    try : 
        with open(csv_path, 'r') as file:
            csv_reader = csv.reader(file)
            rows = []
            for i, row in enumerate(csv_reader):
                if i < 5:  # Get only the first i rows
                    rows.append(row)
                else:
                    break
            string =  '\n'.join([','.join(row) for row in rows])
            openai.api_key = ""
            message = "(Answer in a few words) Based on the following, does the dataset contain information about the entities or does is it contain observations related to the entites : "
            message += string
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message},]
            )
            data = response['choices'][0]['message']['content']
            print(data)
            if "observation" in data.lower():
                return 1
            else:
                return 0
    except Exception as e:
        return 0

folder = "file_generator/datasets"
for root, dirs, files in os.walk(folder):
    for dir in dirs:    
        subfolder_path = os.path.join(root, dir)
        for sub_root, sub_dirs, sub_files in os.walk(subfolder_path):
            for file in sub_files:
                csv_file_path = os.path.join(subfolder_path, file)
                print(csv_file_path, end = " : ")
                obs_count += classify(csv_file_path)
                count+=1
        
print("count : ",count)
print("number of obs : ",obs_count)