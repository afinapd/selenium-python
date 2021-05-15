import requests
url = "https://api.github.com/users"

response=requests.get(url)
print(response.json())

response=requests.get(url, auth=('djw-test','password1'))
print(response.json())

response=requests.get(url, headers={'Authorization':'Bearer 4eb3b67cbea7c0182d25de281c527423b2e2d4f4'})
print(response.json())
#
# my_json = response.json()
# print(my_json['id'])
# for key in my_json.keys():
#     print(key)
