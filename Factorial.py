tc = input("Enter the number of test cases: ")
a=[]
for i in range(tc):
    a.append(input("Enter the input of "+str(i+1)+ " test case: "))
def factorial( n ):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
for na in a:
    if na<0:
        print("Invalid")
    else:
        print(str(factorial(na)))
    
