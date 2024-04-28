n = int(input())
m = int(input())
nums = list(map(int, input().split()))
print(1 if sum(x % m for x in nums) == 0 else 0)
