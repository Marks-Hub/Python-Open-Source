import os
import csv

os.chdir(os.path.dirname(os.path.realpath(__file__)))
f = open("Kepler.csv", "r")

planet = []
Ta = []
Aa = []

Tsquared = []
ACubed = []
x=0

with open("Kepler.csv", "r") as f:
   csv_reader= csv.reader(f, delimiter=",")

   for row in csv_reader:
        planet.append(row[0])
        Ta.append(float(row[1]))     # cast number data as an int
        Aa.append(float(row[2]))     # cast number data as an float
        for g in Ta:
            for i in range(len(Ta)):
                Tsquared.append(Ta[i] ** 2)
            for i in range(len(Aa)):
                ACubed.append(Aa[i] ** 3)
   print("{} T={} A={}  T^2/A^3= {}".format(planet[i], Ta[i], Aa[i], Tsquared[i]/ACubed[i]))
    #print(planet[i] + "M: " + Ta[i] + "R: " + Aa[i] + "M^3/R^4: " + Tsquared[i]/ACubed[i] ) 

lists = [55, 34, 44, 98, 100]

def small(k, lists):
    x=0
    num = k-1
    for i in range(len(lists)):       
        if lists[i] < lists[i+1]:
            smaller = lists[i]
            if x != num:
                x=x+1
            else:
                return smaller
Flip=small(2, lists)
print(Flip)