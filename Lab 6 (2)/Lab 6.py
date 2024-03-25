from tkinter import *
import json
import urllib.request






root = Tk()
root.geometry("400x400")   # size of interface


topFrame = Frame(root)     # frame is a container, root is its parent
topFrame.pack(side=TOP)    # pack() helps determine where an item will be placed
middleFrame = Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

# https://www.tutorialspoint.com/python/tk_label.htm
headerLabel = Label(topFrame, text=" Nobel prize win ", bg="#ffcc99", fg="#003366")
# bg background color  fg foreground/font color 
headerLabel.pack(fill=X)      # fill container horizontally
# https://www.tutorialspoint.com/python/tk_pack.htm

categorylabel = Label(topFrame, text=" Category ", bg="#003366", fg="#ffcc99")
categorylabel.pack(side=LEFT)

# https://www.tutorialspoint.com/how-to-detect-when-an-optionmenu-or-checkbutton-changes-in-tkinter
categoryOptions = ["physics", "chemistry", "medicine", "peace", "literature", "economics"]    # list choices for category
category = StringVar()                        # variable for user's choice of category 
category.set(categoryOptions[0])                  # initialize user's choice to first option of list 
categoryDrop = OptionMenu(topFrame, category, *categoryOptions)   
'''
   create a "drop-down"
   its parent is topFrame
   the selected value is room (initialized to first choice)
   *roomOptions  
'''
categoryDrop.pack(side=LEFT)

# label for year
yearLabel = Label(topFrame, text=" Year ", bg="#003366", fg="#ffcc99")
yearLabel.pack(side=LEFT)

# year drop-down
yearOptions = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
year = StringVar()
year.set(yearOptions[0])
yearDrop = OptionMenu(topFrame, year, *yearOptions)
yearDrop.pack(side=LEFT)





# function called by button
def winner():

    
    concat = "http://api.nobelprize.org/v1/prize.json?category="+category.get()+"&year="+year.get()
    print(concat)

    url = "http://api.nobelprize.org/v1/prize.json?category="+category.get()+"&year="+year.get()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    data = urllib.request.urlopen(req).read().decode()
    print("made it")
    nobel_info = json.loads(data)

    print(json.dumps(nobel_info, indent=2))   
    
    
    print(nobel_info["prizes"][0])
    for i, laureteas in enumerate(nobel_info["prizes"][0]["laureates"]):
        winners= nobel_info["prizes"][0]["laureates"][i]["firstname"]
        print(winners)
        choseLabel.configure(text=winners)

    
    

        
# button 
chosen = Button(middleFrame, text="Who Won", command=winner)
chosen.pack()

choseHeader = Label(bottomFrame, text="nobel")
choseHeader.pack(fill=X)
choseAction = Label(bottomFrame, text="---", bg="#ff9999", fg="#660000")
choseAction.pack(fill=X)
choseLabel = Label(bottomFrame, text="")
choseLabel.pack(fill=X)
root.mainloop()