import fastapi
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os 

app = FastAPI()

class Person(BaseModel):
    name: str
    occupation: str
    address: str

Data = []

@app.get("/person")
async def get_list():
    return Data


@app.post("/person")
async def add_person(person_request: Person):

    for x in person_request:
        if person_request.address == "" or person_request.name == "" or person_request.occupation == "":
            success = False
            return{"Success": success, "Results": "Error message: Invalid Request"}
        else:
            success = True
            Data.append(person_request)
    
    person_json = jsonable_encoder

    #return JSONResponse (content = person_json)
    return {"Success": success, "Results": person_request}