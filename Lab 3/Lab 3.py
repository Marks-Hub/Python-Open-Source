import math
import random
import statistics

sample = 100
summ = 0
flipped = []
number = []

def coinFlip():
    flips_required=0
    coin1=2
    coin2=2
    coin3=2
    coin4=2
    coin5=2
    
    
    while coin1+coin2+coin3+coin4+coin5 != 5 and coin1+coin2+coin3+coin4+coin5 != 0:
        
        coin1=random.randint(0,1)
        coin2=random.randint(0,1)
        coin3=random.randint(0,1)
        coin4=random.randint(0,1)
        coin5=random.randint(0,1)
        flips_required+=1         
    
    return flips_required
    



averag = 0   

for i in range(sample):
    Flip=coinFlip()  
    flipped.append(Flip)
    print("All the same after {} rolls".format(Flip))
    summ += Flip
print(len(flipped))

#for calculating variance and standev https://stackabuse.com/calculating-variance-and-standard-deviation-in-python/
def variance(flipped, ddof=0):
    n = len(flipped)
    mean = sum(flipped) / n
    return sum((x - mean) ** 2 for x in flipped) / (n - ddof)


def stdev(flipped):
    var = variance(flipped, ddof=0)
    std_dev = math.sqrt(var)
    return std_dev

print("The Minimum is {}".format(min(flipped)))
print("The Maximum is {}".format(max(flipped)))
print("The average number of flips to all 5 is {}".format(summ/sample))
 

standDev = math.sqrt(averag)
stndev = stdev(flipped)
print("the standard dev is {}".format(stndev))

print(statistics.median(flipped))

