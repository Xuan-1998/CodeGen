import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
state = [0] * n
is_ladder = True

for i in range(1, n):
    if state[i-1] > 0 and a[i-1] >= a[i]:
        continue
    elif state[i-1] == 0:
        state[i] = 1 if a[i-1] < a[i] else -1
    else:
        is_ladder = False
        break

for _ in range(m):
    l, r = map(int, input().split())
    print("Yes" if is_ladder else "No")
