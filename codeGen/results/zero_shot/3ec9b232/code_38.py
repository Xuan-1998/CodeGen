n = int(input())
m = list(map(int, input().split()))

count = {}
for i in m:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

total_ways = 1
for i in count.values():
    total_ways *= (i + 1)

print(total_ways % (10**9 + 7))
