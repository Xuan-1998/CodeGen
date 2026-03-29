import sys

n = int(input())
roads = []
for _ in range(n - 1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

min_edges_to_reverse = float('inf')
capital_index = None

for i in range(1, n):
    edges_to_reverse = 0
    for j in range(i + 1, n):
        if roads[j - 1][0] != i and roads[j - 1][1] != i:
            edges_to_reverse += 1
    if edges_to_reverse < min_edges_to_reverse:
        min_edges_to_reverse = edges_to_reverse
        capital_index = i

capital = [i for i in range(1, n + 1) if i != capital_index]

print(min_edges_to_reverse)
print(*capital, sep='\n')
