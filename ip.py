ip=input('Enter the ip address : ')
nos=ip.split('.')
firstClass = ''
valid=True
for n in nos:
    
    if(int(n) >=1 and int(n) <= 127):
        if firstClass == '':
            firstClass='Class A'
    elif(int(n) >=128 and int(n) <= 191):
        if firstClass == '':
            firstClass='Class B'
    elif(int(n) >=192 and int(n) <= 223):
        if firstClass == '':
            firstClass='Class C'
    elif(int(n) >=224 and int(n) <= 239):
        if firstClass == '':
            firstClass='Class D'
    elif(int(n) >=240 and int(n) <= 254):
        if firstClass == '':
            firstClass='Class E'
    else :
        valid=False
        break
if valid:
    print(firstClass)
else :
    print('Invalid')
                                
