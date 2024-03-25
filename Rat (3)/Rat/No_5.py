# Mark Okin

from tkinter import *
root = Tk()
root.geometry("800x300")

topFrame = Frame(root)
topFrame.pack(side=TOP)
middleFrame=Frame(root)
middleFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()

headerLabel= Label(topFrame, text=" RATE ME")
headerLabel.pack(fill=X)

ratingHeader= Label(topFrame, text="Please select your rating 1-5 for the following categories ")
ratingHeader.pack(fill=X)
ratingOptions = ["1", "2", "3", "4", "5"]

ratingLabel_1= Label(topFrame, text="Service ")
ratingLabel_1.pack(side=LEFT)
rating_1=StringVar()
rating_1.set(ratingOptions[2])
ratingDrop_1 = OptionMenu(topFrame, rating_1, *ratingOptions)
ratingDrop_1.pack(side=LEFT)

ratingLabel_2= Label(topFrame, text="Cleanliness ")
ratingLabel_2.pack(side=LEFT)
rating_2=StringVar()
rating_2.set(ratingOptions[2])
ratingDrop_2 = OptionMenu(topFrame, rating_2, *ratingOptions)
ratingDrop_2.pack(side=LEFT)

ratingLabel_3= Label(topFrame, text="Parking ")
ratingLabel_3.pack(side=LEFT)
rating_3=StringVar()
rating_3.set(ratingOptions[2])
ratingDrop_3 = OptionMenu(topFrame, rating_3, *ratingOptions)
ratingDrop_3.pack(side=LEFT)

ratingLabel_4= Label(topFrame, text="Quality of food ")
ratingLabel_4.pack(side=LEFT)
rating_4=StringVar()
rating_4.set(ratingOptions[2])
ratingDrop_4 = OptionMenu(topFrame, rating_4, *ratingOptions)
ratingDrop_4.pack(side=LEFT)

ratingLabel_5= Label(topFrame, text="Choice of food ")
ratingLabel_5.pack(side=LEFT)
rating_5=StringVar()
rating_5.set(ratingOptions[2])
ratingDrop_5 = OptionMenu(topFrame, rating_5, *ratingOptions)
ratingDrop_5.pack(side=LEFT)

# replace pass with code that 
# collects the user's ratings
# then averages them

def submit_ratings():
   service = int(rating_1.get())
   Clean = int(rating_2.get())
   Park = int(rating_3.get())
   Qof = int(rating_4.get())
   Cof = int(rating_5.get())
   Average = (service+Clean+Park+Qof+Cof)/5

submitRatingsButton = Button(middleFrame, text=" SUBMIT RATINGS ", command=submit_ratings)
submitRatingsButton.pack()

ratingHeader= Label(bottomFrame, text="Result of ratings")
ratingHeader.pack(fill=X)
ratingResult= Label(bottomFrame, text=" ")
ratingResult.pack(fill=X)

root.mainloop() 