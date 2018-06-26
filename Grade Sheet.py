a=[]
b=[]
credit=[]

for i in range(5):
    a.append(input("Enter the marks of subject "+str(i+1)+" : "))
for i in range(5):
    credit.append(input("Enter the credit of subject "+str(i+1)+" : "))
def grade(n):
    if n>=90:
        b.append(10)
        return 'O'
    elif n>=80:
        b.append(9)
        return 'A+'
    elif n>=70:
        b.append(8)
        return 'A'
    elif n>=60:
        b.append(7)
        return 'B+'
    elif n>=50:
        b.append(6)
        return 'B'
    else:
        return 'RA'
def cgpa(x):
    s=0
    div=0
    if len(a)!=len(b):
        return 0
    for i,n in enumerate(x):
        s+=n*credit[i]        
        div+=credit[i]
    return float(s/div)
print 'Grades: '
for m in a:
   print(grade(m))
print 'CGPA: '+str(cgpa(b))
