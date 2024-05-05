T = int(input())
for _ in range(T):
    N = int(input())
    memo = {}
    total_diamonds = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            total_diamonds += f(i, j)
    print(total_diamonds)
