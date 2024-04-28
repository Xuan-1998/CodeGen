n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    good_sequence = [i]
    for j in range(k-1):
        next_num = (good_sequence[-1] // (good_sequence[-2] if len(good_sequence) > 1 else 1))
        if next_num > 0 and next_num <= n:
            good_sequence.append(next_num)
        else:
            break
    else:
        count += 1
print(count % 1000000007)
