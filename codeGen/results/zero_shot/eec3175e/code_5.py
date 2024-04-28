n, m = map(int, input().split())
nums = list(map(int, input().split()))

if sum(1 for i in nums if i % m == 0) >= (n + 1) // 2:
    print(1)
else:
    print(0)
