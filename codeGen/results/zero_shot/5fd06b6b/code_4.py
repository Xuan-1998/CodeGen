n = int(input())
counts = list(map(int, input().split()))
seq = [n]*n
for i in reversed(range(n-1)):
    if counts[i] < seq[i+1]:
        seq[i] = counts[i]
    else:
        seq[i] = seq[i+1]-1
print(sum(seq))

