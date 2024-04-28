n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    sequence = [i]
    for j in range(k-1):
        if sequence[-1] % (sequence[-2] + 1) == 0:
            sequence.append(sequence[-1] + 1)
        else:
            break
    if len(sequence) == k:
        count += 1
print(count % 1000000007)
