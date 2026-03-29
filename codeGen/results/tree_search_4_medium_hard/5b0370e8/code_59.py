t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    bits = list(map(int, input().split()))
    
    print(count_arrays(n, k, bits))
