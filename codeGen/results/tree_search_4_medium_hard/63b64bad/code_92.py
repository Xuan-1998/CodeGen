def simulate_program(n, a):
    dp = {(1, 0): 0}  # base case: when x = 1 and y = 0

    for _ in range(2, n + 1):
        new_dp = {}
        for (x, y) in list(dp.keys()):
            if x <= 0 or x > n:
                new_dp[(x, y)] = y
            else:
                new_x = x + a[x] - a[x]
                new_y = y + a[x] - a[x]
                if (new_x, new_y) not in dp:
                    dp[(new_x, new_y)] = new_y
        dp.update(new_dp)

    return dp.get((1, 0), -1)

n = int(input())
a = list(map(int, input().split()))
print(simulate_program(n, a))
