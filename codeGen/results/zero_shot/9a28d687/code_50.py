import sys

n = int(input())
costs = [int(input()) for _ in range(n)]
strings = [input() for _ in range(n)]

char_counts = {}
for s in strings:
    for c in s:
        if c not in char_counts:
            char_counts[c] = [0, []]
        char_counts[c][0] += 1
        char_counts[c][1].append(s)

strings.sort(key=lambda s: len(s))

def try_sort(strings):
    cost = 0
    for i in range(len(strings)):
        if len(strings[i]) != 1:
            while True:
                rev_cost = sum(costs[j] for j in range(i, -1, -1) if strings[j] < strings[i])
                if rev_cost <= cost:
                    break
                cost = rev_cost
                strings[i] = strings[i][::-1]
    return cost

if len(strings) > 0 and try_sort(strings) == -1:
    print(-1)
else:
    print(try_sort(strings))
