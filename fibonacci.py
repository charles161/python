d=int(input("Enter a number for fibonacci series "))
f=d
a=0
b=1
print('Recursive: ')
print(a)
print(b)
def fib(a,b,d):
    c=a+b;
    print(c)
    if(d==0):
        return
    d-=1
    a=b
    b=c
    fib(a,b,d)
    
        
fib(a,b,d)

print('\nIterative')

def fibi(d):
    a=0
    b=1
    print(0)
    print(1)
    while d>=0:
        c=a+b
        print(c)
        a=b
        b=c
        d-=1
        
fibi(f)
