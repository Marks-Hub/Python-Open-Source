# Mark Okin

import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))
f = open("Kleiber.csv", "r")
questions = f.read()
reader= csv.reader(f, delimiter=",")
print(questions)
print("\n_______________________________________________________\n")



animal = []
Mass = []
Rate = []

cubed = []
powerof4 = []



# use data to set list values

for row in reader:
    animal.append(row[0])
    Mass.append(int(row[1]))     # cast number data as an int
    Rate.append(float(row[2]))     # cast number data as an float
    for i in range(len(Mass)):
        cubed.append(Mass[i] ** 3)
    for i in range(len(Rate)):
        powerof4.append(Rate[i] ** 4)
    print(animal[i] + "M: " + Mass[i] + "R: " + Rate[i] + "M^3/R^4: " + cubed[i]/powerof4[i] ) 

# Print out info include M^3/R^4 (carets don't work)

