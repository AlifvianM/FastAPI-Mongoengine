from mongoengine import *
import datetime

client = connect(host="mongodb://root:example@mongo:27017/mongodb?authSource=admin")
items_coll = client.get_database("mongodb").list_collection_names()

# name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     tags: List[str] = []

class Items(Document):
    name = StringField(max_length=200)
    description = StringField(max_length=200, required=False)
    price = FloatField(required=False)
    tax = FloatField(required=False)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)

