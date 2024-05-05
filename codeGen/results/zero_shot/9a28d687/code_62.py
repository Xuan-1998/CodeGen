n = int(input())
costs = list(map(int, input().split()))
strings = [input() for _ in range(n)]

sorted_strings = sorted(strings, key=lambda s: (len(s), s))
reversed_counts = [0] * n

for i in range(1, n):
    if sorted_strings[i-1] > sorted_strings[i]:
        for j in range(i):
            if strings[j] == sorted_strings[i]:
                reversed_counts[j] += 1
                break

min_total_cost = sum(cost * rev_count for cost, rev_count in zip(costs, reversed_counts))

if min_total_cost == -1:
    print(-1)
else:
    print(min_total_cost)
