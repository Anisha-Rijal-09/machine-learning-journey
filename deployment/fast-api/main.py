from fastapi import FastAPI,Path,HTTPException,Query
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
    raise HTTPException(status_code=404, detail='Patient not found')

# Query()
@app.get('/sort')
def sort_patients(sort_by:str= Query(...,description='Sort on the basis of height,weight or bmi'),order:str=Query('asc',description='Sort in asc or dsc order')):

  valid_fields=['height','weight','bmi']

  if sort_by not in valid_fields:
    raise HTTPException(status_code=400,detail='invalid field select from {valid_field}')

  if order not in ['asc','desc']:
    raise HTTPException(status_code=400,detail='invalid field select from {valid_field}')

  data =load_data()

  sort_order =True if order=='desc' else False

  sorted_data=sorted(data.values() ,key=lambda x:x.get(sort_by,0),reverse=sort_order)

  return sorted_data


