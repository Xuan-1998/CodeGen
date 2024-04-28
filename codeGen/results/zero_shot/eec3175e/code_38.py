n = int(input())
m = int(input())
arr = list(map(int, input().split()))

print(1 if sum(i for i in arr if i % m == 0) % m == 0 else 0)
