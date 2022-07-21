# Step 1: import FastAPI from fastapi.
from fastapi import FastAPI
# Step 2: create a FastAPI "instance"
app = FastAPI()
# Step 3: create a path operation
@app.get("/")
# Step 4: define the path operation function
async def create():
    return {"Name": "Fares"}

class ModelName(str):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{userId}")
async def getUser(userId):
    return {"UserId": userId}

@app.get("/files/{filesPath:path}")
async def getFiles(filesPath:str):
    return {"FilePath": filesPath}