n = [int(i) for i in input().split(',')]
k = int(input())
print(max(sum(n[i-k:i+1]) for i in range(k, len(n))))
