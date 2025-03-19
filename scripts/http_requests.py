import requests
import json

def get_item(id: str):
    res = requests.get(f"http://127.0.0.1:62422/api/v1/items/{id}")

    if res.status_code != 200:
        print("There was an issue processing the request")
        print(res.status_code)
        return

    print(res.json())

def create_item(name: str, age: int):
    headers = { "Content-Type": "application/json" }
    data = { "name": name, "age": age }
    res = requests.post("http://127.0.0.1:62422/api/v1/items", headers=headers, json=data)

    if res.status_code != 200:
        print("There was an issue processing the request")
        print(res.json())
        print(res.status_code)
        return
    
    print(res.status_code)

if __name__ == "__main__":
    create_item("Charlie", 6)
