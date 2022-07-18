import pymongo
client = pymongo.MongoClient("mongodb+srv://farha:12345@farha.kwooc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name": "farha",
    "email": "farha@ineuron",
    "surname": "sultana"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
farha sultana