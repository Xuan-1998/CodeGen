n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(n):
    if arr[i] == i + 1:
        result.append(i)

print(result)
