# Your name here

import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import csv

f = open("Shakespeare.csv", "r")
questions = f.read()
reader= csv.reader(f, delimiter=",")
print(questions)
print("\n_______________________________________________________\n")

# Write a Play class with the properties title, genre, date, wordNo and speechNo
'''
   Add a method that calculates the average number of 
   words per speech for the play (wordNo/speechNo) 
'''

# Read the file Shakespear.csv 
# Create a list of Play objects

# Loop through the list of plays print out the data 
# including the words-per-speech
