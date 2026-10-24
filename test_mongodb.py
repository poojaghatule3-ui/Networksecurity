from pymongo.mongo_client  import MongoClient
uri = "mongodb+srv://poojaghatule3:<@password>@cluster0.tx2iulm.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

