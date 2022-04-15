from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel
from read_files import read_csvfile, read_excelfile, read_jsonfile, read_database, read_picklefile
import os
from custom_exceptions.file_exceptions import TypeMismatchError

# Create app
app = FastAPI()

class Source(BaseModel):
    file_name: str
    type: str

# Create home page
@app.post("/")
def home():
    pass


# Read csv file
@app.post("/read_csv")
def read_csv(source: Source):
    try:
        if source.type == 'csv':
            read_csvfile.read(os.path.join("datasets", source.file_name))
        else:
            raise TypeMismatchError()
    except TypeMismatchError as e:
        print(e)
    except Exception as e:
        print(e)

# Read excel file
@app.post("/read_excel")
def read_excel(source: Source):
    try:
        if source.type == 'xlsx':
            read_excelfile.read(os.path.join("datasets", source.file_name))
        else:
            raise TypeMismatchError()
    except TypeMismatchError as e:
        print(e)
    except Exception as e:
        print(e)

# Read json file
@app.post("/read_json")
def read_json(source: Source):
    try:
        if source.type == 'json':
            read_jsonfile.read(os.path.join("datasets", source.file_name))
        else:
            raise TypeMismatchError()
    except TypeMismatchError as e:
        print(e)
    except Exception as e:
        print(e)

# Read database file
@app.post("/read_db")
def read_db(source: Source):
    try:
        if source.type == 'db':
            read_database.read(os.path.join("datasets", source.file_name))
        else:
            raise TypeMismatchError()
    except TypeMismatchError as e:
        print(e)
    except Exception as e:
        print(e)

# Read pickle file
@app.post("/read_pickle")
def read_pickle(source: Source):
    try:
        if source.type == 'pkl':
            read_picklefile.read(os.path.join("datasets", source.file_name))
        else:
            raise TypeMismatchError()
    except TypeMismatchError as e:
        print(e)
    except Exception as e:
        print(e)

# Starting point of the app
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    # uvicorn main:app --reload