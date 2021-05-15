list=[1,2,3,1,2,3]
print(set(list))

import requests
url = "https://jsonplaceholder.typicode.com/photos"

response=requests.get(url)
json_data=response.json()

url_list=[]
for photo in json_data:
    url_list.append(photo['url'])

print(len(url_list)) #total
print(len(set(url_list)))
