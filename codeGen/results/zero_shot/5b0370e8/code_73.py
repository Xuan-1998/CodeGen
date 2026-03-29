t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count = 0
    for x in arr:
        count += count_and(x, k)
    
    print(count % (10**9 + 7))
