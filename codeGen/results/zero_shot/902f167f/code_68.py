n, m = map(int, input().split())
print(min(n//i*m//j if i*j<=n*m else float('inf') for i in range(1, int(min(n,m)**0.5)+1) for j in range(i, min(n,m)//i+1)))
