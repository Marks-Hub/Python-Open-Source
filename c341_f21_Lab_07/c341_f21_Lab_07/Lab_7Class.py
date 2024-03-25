'''
   define and use a class
'''
import re
####  start HOCKEYPLAYER CLASS ####
class Sixers:

   # init (aka constructor)  
   def __init__(self, pics, firstName, lastName, playerNum = "00", 
   position="_", age="00", HeightInInches=72, WeightPounds=190, 
   college="_", Salary="00"):
      self.pics = pics
      self.firstName = firstName
      self.lastName = lastName      
      self.position = position
      self.age = age
      self.HeightInInches = HeightInInches
      self.WeightPounds = WeightPounds
      self.college = college
      self.Salary = Salary 

   # method -- definition requires self argument 
   # that argument will (usually) be implied when you call the method
   def fullname(self):
      return "{} {}".format(self.firstName, self.lastName) 

   # creates a URL based on the other data
   def url(self):
      return "https://www.espn.com/nba/player/_/id/"+self.pics+ "/" + self.firstName.lower()+"-"+self.lastName.lower()

   @staticmethod
   def convertHeightFromString(FtIn):
      # FtIn is like 5' 11"

      FtIn = re.sub(r"\s+", "", FtIn)  #elimnate white space
      # re regular expression
      # \s+ regular expression for white space 
      # sub is substitute
      FtIn = re.sub(r"\"", "", FtIn) # eliminate " marking inches 
      tokens=FtIn.split("'")         # split into two pieces using ' as delimiter
      total = int(tokens[0])*12+int(tokens[1])  # cast tokens as integers & calculate height in inches 
      return total

#### end HOCKEYPLAYER CLASS ####

player1 = Sixers("3907387", "ben", "simmons")  # use constructor
player1.PlayerNum = "10"      # add a property 

print(player1)             # print object will output memory location
print(player1.__dict__)    # will take object properties/attributes and make dictionary
print(player1.lastName)    # print property set by constructor
print(player1.fullname())  # print the string output of a method
print(player1.PlayerNum)   # print property/attribute set after instantiation

# a different way to call an object's method 
# this way the self argument is more explicit
print(Sixers.url(player1)) # print the string output of a method
import webbrowser
webbrowser.open(Sixers.url(player1), new=2)

