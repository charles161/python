tc = int(input("Enter the number of testcases :\n"))
import re
for i in range(tc):
    s=str(input("Enter your email: \n"))
    if re.match("(^[a-zA-Z0-9]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", s):
        n=s.find('@')
        print("Your name is :")
        print (s[:n])
        n=0
    else:
        print("Invalid email")

'''
print ("Valid") if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", word) else "Invalid"
'''
