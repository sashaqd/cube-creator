import csv
import openai
openai.api_key = "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"

message = "classify the type of columns based on scale(ratio/interval/ordinal/nominal) , classify if it should be a (key dimension/measure dimension) , classify it's data type (string/decimal) for the given input, the output should be printed as a csv (column,scale,dimension,data type) : "
message += """Year,Authority_en,Authority_ar,value_gwh 
                2008.0,Sharjah Electricity & Water Authority (SEWA),هيئة مياه وكهرباء الشارقة ,1523.0"""

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": message},
    ]
)


data = response['choices'][0]['message']['content']

filename = "output.txt"

with open(filename, 'w') as file:
    for row in data:
        file.write(row)

