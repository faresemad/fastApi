# Step 1: import FastAPI from fastapi.
from fastapi import FastAPI
# Step 2: create a FastAPI "instance"
app = FastAPI()
# Step 3: create a path operation
@app.get("/")
# Step 4: define the path operation function
async def helloMsg():
    # Step 5: return the content
    return {"message": "Hello Mother Fucker"}

@app.get("/components/{component_id}")
async def get_component(component_id: int) -> int:
    return {"component_id": component_id}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]
#=========================================
# @app.get("/components/{component_id}")
# async def get_component(component_id):
#     return {"component_id": component_id}
#=========================================
