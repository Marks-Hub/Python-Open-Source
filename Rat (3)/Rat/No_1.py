# Mark Okin

# Have user input a pH (which is an float)

'''
 determine between 
    > 14 "Out of range"
    8.5 - 14  "Strong Base"
    7.4 - 8.5 "Weak Base"
    6.6 - 7.4 "Neutral"
    5.5 - 6.6 "Weak Acid"
    0 - 5.5  "Strong Acid"
    > 0 "Out of range"
'''
ans = input("Enter ph: ")
 #unsure why <= wasn't working
if ans > 14:
    print("Out of range")
#if ans >= 8.5 and <= 14:
    print("Strong Base")
#if ans >= 8.5 and <= 14:
    print("Weak Base")
#if ans >= 8.5 and <= 14:
    print("Neutral")
#if ans >= 8.5 and <= 14:
    print("Weak Acid")
#if ans >= 8.5 and <= 14:
    print("Strong Acid")
if ans <0:
    print("Out of range")
