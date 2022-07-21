# FastAPI
```python
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
```
