a=[]
for i in range(2000,4000):
    if i%7==0 and i%5!=0:
        a.append(i)
for i,n in enumerate(a):
    if i!=len(a)-1:
        print str(n)+',',
    else:
        print n,
