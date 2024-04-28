n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(any(sum(emap(i % m)) for _ in range(2**n)))
