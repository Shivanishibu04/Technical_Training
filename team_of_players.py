str = input()
chair = 0
av = 0
for i in range(len(str)):
    if str[i] == 'C' or str[i] == 'U':
        if av != 0:
            av -= 1
        else :
            chair += 1
    elif str[i] == 'R' or str[i] == 'L':
        av += 1
        
print(chair)
