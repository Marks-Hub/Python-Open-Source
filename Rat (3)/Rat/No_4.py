# Mark Okin

import json
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

url = "https://www1.lasalle.edu/~blum/c230wks/coen.json"

os.chdir(os.path.dirname(os.path.realpath(__file__)))

import urllib.request     # https://docs.python.org/3/library/urllib.request.html
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)  # parse json object

from urllib.request import Request, urlopen
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read()
info = json.loads(data)

for i in range(len(info)-1, -1, -1):
    
    if info["movies"][i]["runtime"]>100:
            info.pop(i)  
            print(info)

with open("new_json.json", "w") as f2:
    f2.write(json.dumps(info, indent=2))

# Read the JSON found at  
 
# Loop through the "movies" array/list 
# Write code that deletes any movies that have runtimes more than 100 minutes 

# write the edited JSON to a new file
