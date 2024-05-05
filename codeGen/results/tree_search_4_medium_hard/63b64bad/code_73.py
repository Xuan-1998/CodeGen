n = int(input())  # sequence length
sequence = list(map(int, input().split()))  # sequence values

dp_table = [[-1] * 2 for _ in range(n + 1)]  # initialize DP table with base cases
dp_table[0][0] = 0  # initial state (1, 0)
dp_table[0][1] = 0

for i in range(1, n + 1):  # iterate through the sequence
    if i <= 0 or i > n:  # terminate if x <= 0 or x > n
        dp_table[i][0] = -1
        dp_table[i][1] = -1
    else:
        a_x = sequence[i - 1]  # current sequence value
        x, y = dp_table[i - 1][0], dp_table[i - 1][1]
        if x <= 0 or x > n:  # terminate if x <= 0 or x > n
            dp_table[i][0] = -1
            dp_table[i][1] = -1
        else:
            x += a_x  # update x and y based on transition rules
            y += a_x
            x -= a_x
            dp_table[i][0] = max(dp_table[i - 1][0], dp_table[i - 1][1])
            dp_table[i][1] = dp_table[i - 1][0]

print(dp_table[n][1])  # print the final value of y
