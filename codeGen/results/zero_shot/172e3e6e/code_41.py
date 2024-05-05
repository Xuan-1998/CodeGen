n = int(input())
a = list(map(int, input().split()))

count = 0
for k in range(1, n+1):
    for i in range(n-k+1):
        subseq = a[i:i+k]
        is_good = True
        for j in range(k):
            if subseq[j] % (j+1) != 0:
                is_good = False
                break
        if is_good:
            count += 1

print(count % (10**9 + 7))
