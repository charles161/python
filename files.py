
file = open(input('Enter file name '),'r+')
word=0
arr=file.read().split('\n')
lines=len(arr)
for i in arr:
    word=word+len(i.split(' '))
print('Words : ',word)
print('Lines : ',lines)
file.close()
