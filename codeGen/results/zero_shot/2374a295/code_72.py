n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    sequence = [i]
    for _ in range(k-1):
        next_num = sequence[-1] + 1
        while next_num % sequence[0] != 0:
            next_num += 1
        sequence.append(next_num)
    count += 1
print(count % 1000000007)
