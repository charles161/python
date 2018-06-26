ip = input('Enter space separated strings : ').split(' ')

#using map
def toInt(x):
    return len(x)
print('using map function ',list(map(toInt,ip)))

#using for loop
newArr=[]
for s in ip:
    newArr.append(len(s))
print('using for loop ',newArr)

#using list comprehension
print('using list comprehension ',[len(s) for s in ip])
