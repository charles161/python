def magic(st,lim):
    return st[lim+1:]+st[:lim]

for i in range(int(input('Testcases : '))):
    a=input('enter ur name : ')
    b=input('enter ur crush name : ')
    s=0
    f='FLAMES'
    while True:
        if len(list(set(a)&set(b)))>0:
            for i in list(set(a)&set(b)):
                a=a[:a.find(i)]+a[a.find(i)+1:]
                b=b[:b.find(i)]+b[b.find(i)+1:]
        else:
            s=len(a)+len(b)
            break

    while True:
        if len(f)==1 or s<1:
            print(f)
            break;
        l=len(f)
        if s<=l :
            f=magic(f,s-1)
        else:
            if s%l==0:
                f=magic(f,l-1)
            else:
                f=magic(f,s%l-1)




