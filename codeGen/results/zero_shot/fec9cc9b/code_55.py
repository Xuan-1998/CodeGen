import sys

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = []

for _ in range(m):
    l, r = map(int, input().split())
    subarr = arr[l:r+1]

    is_ladder = True

    for i in range(1, len(subarr)):
        if (subarr[i-1] <= subarr[i] and subarr[i] >= subarr[i+1]) or (subarr[i-1] >= subarr[i] and subarr[i] <= subarr[i+1]):
            is_ladder = False
            break

    result.append("Yes" if is_ladder else "No")

for answer in result:
    print(answer)
