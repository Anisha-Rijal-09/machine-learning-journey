from fastapi import FastAPI,Path
import json

app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data


@app.get("/")
def hello():
    return {'message':'Patient management system API'}


@app.get("/about")
def about():
    return{'message':'Fully functional API to manage patient recors'}

@app.get("/view")
def view():
    data = load_data()
    return data


# path parameters

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='Id of the patient in the DB',example='P001')):
    data =load_data() # load json file
    if patient_id in data:
        return data[patient_id]
    return {'message':'patient not found'}
