n = int(input())
sequence = list(map(int, input().split()))

counts = [0]*n
min_val = sequence[-1]

for i in range(n-1, -1, -1):
    if sequence[i] > min_val:
        counts[i] = min_val
    else:
        counts[i] = sequence[i]
        min_val = sequence[i]

print(sum(counts))

