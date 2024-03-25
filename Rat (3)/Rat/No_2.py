# Your name here

numbs = [10, 20, 30, 1, 2, 3]
squared = []
# replace word pass below with your code 
# that returns the sum of squares of the list items
def sumOfSquares(*args):
   for i in range(len(numbs)):
      squared.append(numbs[i]**2)
   return sum(squared)

print(sumOfSquares(*numbs)) 
