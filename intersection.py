list1=input('Enter the space separated elements for list 1 : ').split(' ')
list2=input('Enter the space separated elements for list 2 : ').split(' ')

print(list(set(list1).intersection(list2)))
