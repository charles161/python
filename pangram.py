def is_pangram(s):
     return not set('abcdefghijklmnopqrstuvwxyz') - set(s.lower())

ip = input("Enter a string : ")
if is_pangram(ip):
    print('It is a pangram')
else :
    print('It is not a pangram')
