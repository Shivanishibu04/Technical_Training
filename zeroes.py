#Count number of zeores in the numbers given in a range 0 to n

n = int(input("Enter the number : "))
count = 0
digit = 1
while True:
    posVal, rem = divmod(n, digit)
    print("posVal, rem : ", posVal, rem)
    prefix , posVal = divmod(posVal, 10)
    print("prefix, posVal : ", prefix, posVal)
    
    if prefix == 0:
        break
    if posVal == 0:
        count += (prefix -1)*digit + rem + 1
    else :
        count += prefix * digit 
    digit *= 10

print("count of zeroes in n : ", count)
