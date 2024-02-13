from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

origins = [
    "http://127.0.0.1:5500", 
    "http://localhost:8000",  
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    query: str

@app.post("/run-query")
async def run_query(query: Query) -> Any:
    
    api_key = "" # add key here
    client = OpenAI(api_key=api_key)

    # text_query = input('Input your query: ')
    text_query = query.query

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
            "role": "system",
            "content": "Write an appropriate SPARQL Query to retrieve the following information from Wikidata: " + text_query
            }
        ]
    )

    sparql_query = completion.choices[0].message.content

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
            "role": "system",
            "content": "From the following text insert the just the SPARQL Query in \"\"\" insert query here \"\"\": " + str(sparql_query)
            }
        ]
    )

    final_query = completion.choices[0].message.content

    # print("Generated SPARQL Query:")
    # if final_query[final_query.find('\"\"\"')+3:final_query.rfind('\"\"\"')] == "":
    #     print("Error: Invalid text query!")

    # else:
    #     print(final_query[final_query.find('\"\"\"')+3:final_query.rfind('\"\"\"')])

    if final_query[final_query.find('\"\"\"')+3:final_query.rfind('\"\"\"')] == "":
        result = {"Error: Invalid text query!"}

    else:
        result = final_query[final_query.find('\"\"\"')+3:final_query.rfind('\"\"\"')]

    return result
