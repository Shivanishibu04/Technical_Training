# Mr. Ramesh is the manager at the  hotel. The hotel has an infinite amount of rooms.
# One fine day, a  number of tourists come to stay at the hotel.
# The tourists consist of:
# → A Captain.
# → An unknown group of families consisting of  members per group where  ≠ .
# The Captain was given a separate room, and the rest were given one room per group.
# Mr. Ramesh has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.
# Mr. Ramesh needs you to help him find the Captain's room number.


# The first line consists of an integer, , the size of each group.
# The second line contains the unordered elements of the room number list.




# Output the Captain's room number.

# 5
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

# 8

#method 1:
from collections import Counter
N = input()
rooms = list(map(int, input().split()))
C = Counter(rooms)
for room, count in C.items():
    if count == 1:
        print(room)
        break

#method2:
grp_size = int(input())
array = list(map(int,input().split()))
distinct = list(set(array))

result = ((sum(distinct)*grp_size ) - sum(array))/(grp_size-1)
print(int(result))
