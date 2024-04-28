n = int(input())
m = int(input())
arr = list(map(int, input().split()))
print(1 if sum(arr) % m == 0 else 0)
