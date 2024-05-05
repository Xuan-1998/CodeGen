n = int(input())
sequence = list(map(int, input().split()))
x = 1
y = 0
result = []
while True:
    if x <= 0 or x > n:
        break
    y += sequence[x-1]
    x += sequence[x-1]

for i in range(1, n):
    if x <= 0 or x > n:
        print(-1)
    else:
        y += sequence[i]
        x += sequence[i]
    print(y)
