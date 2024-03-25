import json
import os

url = "https://jsonplaceholder.typicode.com/posts"

os.chdir(os.path.dirname(os.path.realpath(__file__)))

import urllib.request     # https://docs.python.org/3/library/urllib.request.html
data = urllib.request.urlopen(url).read().decode()
user_info = json.loads(data)  # parse json object


from urllib.request import Request, urlopen
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read()
user_info = json.loads(data)

for i in range(len(user_info)-1, -1, -1):
    
    if user_info[i]["userId"]==5:
            user_info.pop(i)
            print(user_info)  

with open("new_json.json", "w") as f2:
    f2.write(json.dumps(user_info, indent=2))
