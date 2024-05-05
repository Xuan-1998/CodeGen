n = int(input())
sequence = list(map(int, input().split()))
y_values = []

for i in range(1, n+1):
    x, y = 1, 0
    while True:
        if x <= 0 or x > n:
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    
    if x > 0 and y < 10**9:  # If x > 0 at termination, it means the program didn't terminate.
        y_values.append(-1)
    else:
        y_values.append(y)

for i in range(n-1):
    print(y_values[i])
