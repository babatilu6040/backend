import json

def defult_response():
    with open("../defult_response.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return {
        "status": "success",
        "message": "user found successfully!",
        "result": data
    }
