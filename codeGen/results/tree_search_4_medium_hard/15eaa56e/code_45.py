code
import sys

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]

state = {i: [] for i in range(m)}
for row in table:
    for j, val in enumerate(row):
        state[j].append(val)
        state[j].sort()

k = int(input())
for _ in range(k):
    l, r = map(int, input().split())
    sorted_in_one_column = False
    for col in state.values():
        if all(col[l-1] <= x for x in col[r-l+1:r+1]):
            sorted_in_one_column = True
            break
    print("Yes" if sorted_in_one_column else "No")
