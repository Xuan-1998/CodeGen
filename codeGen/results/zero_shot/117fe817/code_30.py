code
n = int(input())
count = 0
for i in range(n+1):
    count += i // 10 + 1
print(count)
