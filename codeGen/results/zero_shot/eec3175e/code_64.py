n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(1 if sum(i % m == 0 for i in arr) > 0 else 0)
