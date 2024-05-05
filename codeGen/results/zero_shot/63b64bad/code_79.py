n = int(input())  # read the length of the sequence

sequence = list(map(int, input().split()))  # read the sequence

for _ in range(n - 1):
    x, y = 1, 0
    while x <= n and x > 0:  # simulate the program
        x += sequence[x - 1]
        y += sequence[x - 1]
        x -= sequence[x - 1]
    print(y)  # output the final value of y
