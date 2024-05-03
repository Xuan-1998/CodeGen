import sys

n, m = map(int, input().split())
count = [0] * m

for _ in range(n):
    s, x = map(float, input().split())
    count[s-1] += 1

min_replants = 0
prev_species = None

for i in range(m-1):
    if count[i+1] > 0 and prev_species != i+1:
        min_replants += 1
    prev_species = i+1

print(min_replants)
