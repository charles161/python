import math
def binary_sort(sortedlist,n,x):
 
 start = 0
 end = n - 1

 while(start <= end):
  mid1 = (start + end)/2
  mid= math.floor(mid1)
  if (x == sortedlist[mid]):
   return mid
  elif(x < sortedlist[mid]):
    end = mid - 1
  else:
   start = mid + 1 
 
 return -1

n = int(input("Enter the size of the list: "))

sortedlist = []

for i in range(n):
 sortedlist.append(input("Enter %dth element: "%i))

x = input("Enter the number to search: ")
position = binary_sort(sortedlist, n, x)

if(position != -1):
 print("Entered number %s is present at position: %d"%(x,position))
else:
 print("Entered number %s is not present in the list"%x)
