import requests
import json

# def main():
#     url = "http://127.0.0.1:8000/items/"
#     data = {
#         "name": "Test Item",
#         "discription": "This is a test item.",
#         "price": 100,
#         "tax": 1.1
#     }
#     response = requests.post(url, json.dumps(data))
#     print(response.json())

def main():
    url = "http://127.0.0.1:8000"
    data = {
       "x": 2.3,
       "y": 3.3
    }
    response = requests.post(url, json.dumps(data))
    print(response.json())

if __name__ == "__main__":
    main()