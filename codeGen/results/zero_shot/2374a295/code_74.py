n, k = map(int, input().split())
count = 1
for i in range(1, k):
    if n % (i + 1) != 0:
        count = 0
        break
print(count)
