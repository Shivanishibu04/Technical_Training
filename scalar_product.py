n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr1.sort()  
arr2.sort()  

i = 0
j = 0
sum = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        x = max(arr2)
        sum += arr1[i] * x
        arr2.remove(x)
        i += 1
    else:
        x = max(arr1)
        sum += arr2[j] * x
        arr1.remove(x)
        j += 1

print(sum)
