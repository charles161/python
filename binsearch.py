def binSearch(nos,q):
    if nos[len(nos)-1] == q:
        return 'found'
    elif nos[len(nos)-1] < q :
        return 'not found'
    else :
        nu = 0
        if len(nos)%2 == 0 :
            nu = int(len(nos)/2)
        else:
            nu = int(round(len(nos)/2)-1) 
        if nos[nu-1]==q:
            return 'found'
        elif nos[nu-1] < q:
            return binSearch(nos[nu:],q)
        else :
            return binSearch(nos[:nu],q)
                   
   
for i in range(int(input('Enter the no. of test cases : '))):
    nos=sorted([int(j) for j in input('Enter space separated nos : ').split(' ')])
    query=int(input('Enter the number u want to search : '))
    print(binSearch(nos,query))
