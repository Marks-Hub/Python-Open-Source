import re  # regular expressions
import os 
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from Lab_7Class import Sixers

# constructor now has PlayerNum attribute with default value 00
# we can supply a value
#player2 = HockeyPlayer("8476461", "Sean", "Couturier", "14")
# print(player2.__dict__)

sixe = []

with open("Sixers.csv", "r") as f:
   first_line = f.readline()  # contains headers   
   for line in f:
      if line.strip(): #ignoring blank lines 
         x = line.rstrip().split(",")

         parts = re.split(r"\s+", x[1], 1)         
         #split on first occurrence of white space 
         # first occurrence James van Riemsdyk -- separate James keep rest together 
         # parts = x[1].split(" ")
         sixe.append(Sixers(x[0], parts[0], parts[1], x[2], x[3], x[4], (Sixers.convertHeightFromString(x[4])/39.37), x[5], x[6], x[7]))
         print(x[5])
         #print(parts[0])

for player in sixe:
   print("{} {} salary is {}".format(player.lastName, player.position, player.Salary))

