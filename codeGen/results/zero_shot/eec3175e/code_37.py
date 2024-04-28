n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(1 if sum(x%4==0 for x in nums) %m == 0 else 0)
