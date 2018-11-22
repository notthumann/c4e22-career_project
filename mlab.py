import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds055980.mlab.com:55980/c4e22-career-quiz
host = "ds055980.mlab.com"
port = 55980
db_name = "c4e22-career-quiz"
user_name = "nothuman"
password = "minhngoc123"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())