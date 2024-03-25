import os

import csv

email = []
yes_no1 =[]
yes_no2 =[]
yes_no3 =[]
yes_no4 =[]
yes_no5 =[]
yes_no6 =[]
no_go_emails = []
# change directory to program's folder
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# open a file, read all of it, close it
f = open("COVID_Questions.txt", "r")

questions = f.read()
f.close()         # close what you opened 
print(questions)
print("\n_______________________________________________________\n")

with open("COVID_survey.csv", "r") as f:
   csv_reader= csv.reader(f, delimiter=",")
   
   for row in csv_reader:
      email.append(row[0])
      yes_no1.append(int(row[1]))     # cast number data as an int
      yes_no2.append(int(row[2]))     # cast number data as an int
      yes_no3.append(int(row[3]))     # cast number data as an int
      yes_no4.append(int(row[4]))     # cast number data as an int
      yes_no5.append(int(row[5]))     # cast number data as an int
      yes_no6.append(int(row[6]))     # cast number data as an int
  
   for i in range(len(email)):
      if yes_no1[i] == 1:
         
         if yes_no2[i] == 1:
            no_go_emails.append(email[i])
         if yes_no3[i] == 1:
            no_go_emails.append(email[i])
         if yes_no4[i] == 1:
            no_go_emails.append(email[i])
         if yes_no5[i] == 1:
            no_go_emails.append(email[i])
         if yes_no6[i] == 1:
            no_go_emails.append(email[i])
            
   # how to remove duplicates in list: https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
   res = []
   for i in no_go_emails:
    if i not in res:
        res.append(i)
   print(res)

