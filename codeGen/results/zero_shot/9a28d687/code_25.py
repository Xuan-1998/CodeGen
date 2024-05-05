import sys

n = int(sys.stdin.readline())
cost = [int(c) for c in sys.stdin.readline().split()]
strings = [sys.stdin.readline().strip() for _ in range(n)]

total_cost = 0
lex_sort = True

for i in range(n):
    for j in range(i+1, n):
        if len(strings[i]) > len(strings[j]):
            total_cost += cost[i]
            strings[i] = strings[i][::-1]
        elif len(strings[i]) < len(strings[j]):
            total_cost += cost[j]
            strings[j] = strings[j][::-1]

if not all(s1 <= s2 for s1, s2 in zip(strings, strings[1:])):
    lex_sort = False

if lex_sort:
    print(total_cost)
else:
    print(-1)
