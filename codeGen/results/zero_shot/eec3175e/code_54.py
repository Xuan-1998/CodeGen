n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(1 if sum(i for i in nums if i % m == 0) % m == 0 else 0)
