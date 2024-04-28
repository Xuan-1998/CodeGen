n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    seq = [i]
    for _ in range(k-1):
        seq.append(seq[-1]//seq[-2])
    if all(x % y == 0 for x, y in zip(seq[1:], seq[:-1])):
        count += 1
print(count % 1000000007)
