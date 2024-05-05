import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

state = {}
for i in range(n):
    for j in range(m):
        if (j,) not in state:
            state[(j,)] = []
        state[(j,)].append(table[i][j])

for i in range(1, n):
    for j in range(m):
        if state.get((j,), [])[i-1] > state.get((j,), [])[i]:
            state[(j,)] = "unsorted"
            break
    else:
        continue
    break

def is_sorted(subtable):
    for i in range(1, len(subtable)):
        for j in range(m):
            if subtable[i][j] < subtable[i-1][j]:
                return False
    return True

for l, r in [tuple(map(int, input().split())) for _ in range(k)]:
    for i in range(min(l-1, m), max(r, 0)):
        if is_sorted([row[i] for row in table[l-1:r+1]]):
            print("Yes")
            sys.exit()

print("No")
