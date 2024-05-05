def solve(n, sequence):
    memo = {}
    for x in range(1, n+1):
        y = 0
        while True:
            if x <= 0 or x > n:
                return -1
            new_x = (x + sequence[x-1]) % n
            new_y = y + sequence[x-1]
            if (new_x, new_y) in memo:
                return memo[(new_x, new_y)]
            y = new_y - sequence[new_x-1]
            x = new_x
    return y

n = int(input())
sequence = list(map(int, input().split()))
for i in range(n):
    print(solve(i+2, [0]+sequence))
