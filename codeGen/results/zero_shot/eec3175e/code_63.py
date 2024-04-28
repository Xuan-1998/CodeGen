n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0 if any(sum(subset(arr)) % m == 0 for r in range(1 << len(arr))) else 1
print(ans)
