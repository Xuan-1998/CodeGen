n, m = map(int, input().split())
print(min((n+1)//i * (m+1)//j for i in range(1, n+2) for j in range(1, m+2)))
