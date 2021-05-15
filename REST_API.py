import requests
url = "https://jsonplaceholder.typicode.com/photos"

response=requests.get(url)
print(response.json())

jsonPayload={'albumId': 1, 'id': 1, 'title': 'idk', 'url':'idk.com', 'thumbnailUrl': 'idk'}
response=requests.post(url, json=jsonPayload)
response.json()
print(response.json())

url = "https://jsonplaceholder.typicode.com/photos/100"
jsonPayload={'albumId': 1, 'title': 'idk put', 'url':'idk.com', 'thumbnailUrl': 'idk'}
response=requests.put(url, json=jsonPayload)
response.json()
print(response.json())

response=requests.delete(url)
response.json()
print(response.json())