n, m, arr = map(int, input().split())
print(1 if any(sum(subset) % m == 0 for r in range(2**n), subset=[arr[i] for i in r]) else 0)
