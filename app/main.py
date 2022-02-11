from fastapi import FastAPI, Query
from app.models.item import Item, UpdatedItem
from app.models.user import UserIn, UserOut
from app.models.db import Items, items_coll
from typing import List, Optional

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add-data/")
async def post_item(item: Item):
    item = item.dict()
    data = Items(
        name=item["name"], 
        description=item["description"], 
        price=item["price"], 
        tax=item["tax"])
    data.save()
    return {"msg":"Success", "data":item}

@app.get("/items/")
async def get_all_item():
    items = [i.name for i in Items.objects]
    return {"msg":"Success", "data":items}

@app.get("/items/{items_name}")
async def get_item(items_name: str):
    item = Items.objects.get(name=items_name)
    data = {
        "name":item.name,
        "description":item.description,
        "price":item.price,
        "tax":item.tax
    }
    return {"msg":"Success", "data":data}

@app.delete("/items/{items_name}")
async def get_item(items_name: str):
    item = Items.objects.get(name=items_name)
    item_name = item.name
    item.delete()
    return {"msg":"item {} has been deleted".format(item_name)}

@app.put("/items/{items_name}")
async def update_item(items: UpdatedItem, items_name: str):
    item = Items.objects.get(name=items_name)
    print("ITEM : ", items.price)
    if item:
        item.update(
            name=items.name if items.name else items_name,
            description=items.description,
            price=items.price,
            tax=items.tax
            # **items.dict()
        )
        data = {
            "name":item.name,
            "description":item.description,
            "price":item.price,
            "tax":item.tax
        }
        return data
    else:
        return False

# @app.get("/items/")
# async def read_items(q : Optional[List[str]] = Query(None)):
#     query_items = {"q": q}
#     return query_items

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# @app.post("/items/", response_model=Item)
# async def create_item(item: Item):
#     print(item)
#     return item

# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn):
#     return user