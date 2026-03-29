import sys

n = int(input())  # number of strings
costs = []  # costs of reversing each string
strings = []  # original strings

# read input
for _ in range(n):
    c, s = input().split()
    costs.append(int(c))
    strings.append(s)

# sort by original length and then by cost
strings.sort(key=lambda x: (len(x), costs[strings.index(x)]))

ans = 0
prev_cost = 0

for i in range(1, n):
    if len(strings[i-1]) > len(strings[i]):
        ans += prev_cost
    else:
        while strings[i] != strings[i-1][::-1]:
            ans += costs[i]
            strings[i] = strings[i][::-1]

print(ans)
