p = int(input())
n = int(input())
count = 0
room = 1
while room <= n+1:
    if room == n+1:
        break
    crosses = (room - 1) % 2
    if crosses % 2 != 0:
        room = p
    else:
        room += 1
    count += 1
print(count % (10**9 + 7))
