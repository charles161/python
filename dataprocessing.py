tc = input("Enter the number of test cases: ")
sort=[]
def valid(number):
    
    n=int(number)
    if n>=1 and n<=126:
     
            return 'Class A'           
        
    elif n>=128 and n<=191:
      
            return 'Class B'
        
    elif n>=192 and n<=223:
     
            return 'Class C'
        
    elif n>=224 and n<=239:
     
            return 'Class D'
        
    elif n>=240 and n<=254:
  
            return 'Class E'
    
def validip(arr):
    v=True
    for i,no in enumerate(arr):
        n=int(no)
        if not(len(arr)==4 and ((n>=1 and n<=126) or (n>=128 and n<=191) or (n>=192 and n<=223) or (n>=224 and n<=239) or (n>=240 and n<=254))):
            v=False
    if v:
        sort.append(valid(arr[0]))
    else:
        sort.append('Invalid')


for i in range(tc):
    validip(raw_input("Enter the ip of "+str(i+1)+ " test case: ").split('.'))
        
for s in sort:
    print s



