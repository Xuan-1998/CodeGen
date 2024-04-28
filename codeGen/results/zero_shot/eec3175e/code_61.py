n = int(input())
m = int(input())
nums = list(map(int, input().split()))
print(1 if sum([num for num in nums if num % m == 0]) % m == 0 else 0)
