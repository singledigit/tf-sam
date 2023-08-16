import json

def open_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Hello TF World",
        }),
    }
