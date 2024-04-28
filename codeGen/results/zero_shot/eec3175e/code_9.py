n = int(input())
m = int(input())
arr = [int(x) for x in input().split()]

print(1 if sum(i % m for i in arr) == 0 else 0)
