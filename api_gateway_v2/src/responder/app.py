import json

def open_handler(event, context):
    return json.dumps({"message": "Hello TF World"})
