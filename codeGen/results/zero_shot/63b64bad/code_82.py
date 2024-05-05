# Initialize variables
n = int(input())
sequence = list(map(int, input().split()))
y_values = []

for i in range(n-1):
    x = 1
    y = 0
    while True:
        if x <= 0 or x > n:
            break
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
    
    y_values.append(y)

print(*y_values, sep='\n')
