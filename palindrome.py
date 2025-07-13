# Check whether the input string can be rearranged to form a palindrome.
# method 1:
s = input("Enter the string: ")
check = 0

for ch in set(s): 
    cnt = s.count(ch)
    if cnt % 2 != 0:
        check += 1

if check <= 1:
    print("True")
else:
    print("False")


# method 2:
from collections import Counter
N = input()
C = Counter(N)
oddChar = 0

for i in C.values():
    if i%2 == 1:
        oddChar+=1
if oddChar > 1:
    print('False')
else :
    print('True')
