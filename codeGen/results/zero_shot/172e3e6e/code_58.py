n = int(input())
a = [int(x) for x in input().split()]
count = 0
for i in range(n):
    if i < a[i]:
        break
    count += 1
print(count % (10**9 + 7))
