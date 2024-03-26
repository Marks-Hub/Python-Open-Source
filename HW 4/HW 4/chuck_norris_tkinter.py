# Mark Okin

import os
import json
import urllib.request

url ="http://dummy.restapiexample.com/api/v1/employees"

os.chdir(os.path.dirname(os.path.realpath(__file__)))

sample=24
from urllib.request import Request, urlopen
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(req).read()
info = json.loads(data)

for i in range(sample):
    del (info["data"][i]["employee_age"])
    del (info["data"][i]["profile_image"])
print(info["data"])
 


from tkinter import *
root = Tk()
root.geometry("800x300")

topFrame = Frame(root)
topFrame.pack(side=TOP)
middleFrame=Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

headerLabel= Label(topFrame, text=" Chuck Norris Jokes ")
headerLabel.pack(fill=X)

numLabel= Label(topFrame, text=" Number of Jokes ")
numLabel.pack(side=LEFT)
numOptions = ["1", "2", "3", "4", "5", "6"]
number=StringVar()
number.set(numOptions[0])
numDrop = OptionMenu(topFrame, number, *numOptions)
numDrop.pack(side=LEFT)

# replace pass with code that 
# retrieves the user's choice for a number
# concantenates that on the end of http://api.icndb.com/jokes/random/
# Goes to that URL to get the JSON
# The Value property is an array/list.  Loop over that list and display the "joke" property.  
# Display the jokes on the jokesList . 
def reserve():

    concat = "http://api.icndb.com/jokes/random/"+number.get()
    print(concat)

    url = "http://api.icndb.com/jokes/random/"+number.get()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    data = urllib.request.urlopen(req).read().decode()
    joke_info = json.loads(data)

    print(json.dumps(joke_info, indent=2))   
    
    for i in range(len(joke_info["value"])):
        print(i)
        jokes = joke_info["value"][i]["joke"]
        print(jokes)
        jokesList.configure(text=jokes)

getJokeButton = Button(middleFrame, text="Get Jokes", command=reserve)
getJokeButton.pack()

jokesHeader= Label(bottomFrame, text="Jokes")
jokesHeader.pack(fill=X)
jokesList= Label(bottomFrame, text="---")
jokesList.pack(fill=X)

root.mainloop() 