from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}/items/{item_id}")
async def getInfo(user_id:int, item_id:int):
    return {
        "user_id": user_id,
        "item_id": item_id,
        "Message":f"this is a test from {user_id} and the item id is {item_id}"
    }
    
    

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]