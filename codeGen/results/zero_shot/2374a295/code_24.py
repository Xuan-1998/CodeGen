n, k = map(int, input().split())
count = 0
for i in range(1, n+1):
    if all(i % j == 0 for j in range(2, i)):
        temp = [i]
        for _ in range(k-1):
            temp.append(temp[-1] // len(temp))
        count += 1
print(count % 1000000007)
