n, k = map(int, input().split())
good_sequences_count = 0
for i in range(1, n+1):
    sequence = [i]
    for _ in range(k-1):
        next_num = 1
        for j in range(len(sequence)):
            if not sequence[j] % (next_num := next_num * sequence[j]):
                break
        if next_num > 1:
            good_sequences_count += 1
            break
print(good_sequences_count % 100000007)
