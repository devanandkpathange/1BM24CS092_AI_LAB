print("Enter Row and Column")
r = int(input())
c = int(input())

room = [[0 for j in range(c)] for i in range(r)]

print("0-dirty, 1-clean")

for i in range(r):
    for j in range(c):
        print(f"Room {i},{j}")
        room[i][j] = int(input())

i = 0
j = 0

tot = r * c
count = 0

top = 0
bottom = r - 1
left = 0
right = c - 1

while count < tot:

    
    while j <= right:
        if room[i][j] == 0:
            print(f"Room {i},{j} is cleaned")
            room[i][j] = 1

        count += 1
        j += 1

    j -= 1
    top += 1
    i += 1

    
    while i <= bottom:
        if room[i][j] == 0:
            print(f"Room {i},{j} is cleaned")
            room[i][j] = 1

        count += 1
        i += 1

    i -= 1
    right -= 1
    j -= 1

    
    while j >= left and count < tot:
        if room[i][j] == 0:
            print(f"Room {i},{j} is cleaned")
            room[i][j] = 1

        count += 1
        j -= 1

    j += 1
    bottom -= 1
    i -= 1

    
    while i >= top and count < tot:
        if room[i][j] == 0:
            print(f"Room {i},{j} is cleaned")
            room[i][j] = 1

        count += 1
        i -= 1

    i += 1
    left += 1
    j += 1
