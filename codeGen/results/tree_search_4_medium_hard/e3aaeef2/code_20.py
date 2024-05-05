def solve():
    t = int(input())  # Number of test cases

    dp = {}  # Memoization dictionary with default value -1

    for _ in range(t):
        n, m = map(int, input().split())  # Initial number and operations

        res = -1  # Initialize result to -1
        state = (n.bit_length(), n)  # Initialize state as (length, value)

        for _ in range(m):
            if state[0] == 1:  # If the current number has only one digit
                res = min(res, state[0]) if res != -1 else state[0]
            else:
                next_state = ((state[0] + 1).bit_length(), int(str(state[1]).translate({str(i): str(i+1) for i in range(10)})))
                if next_state not in dp:
                    dp[next_state] = solve_helper(next_state, m)
                res = min(res, dp[next_state]) if res != -1 else dp[next_state]

        print((res + 7) % (10**9 + 7))  # Print the result modulo 10^9+7

def solve_helper(state, m):
    if state[0] == 1:  # If the current number has only one digit
        return state[0]
    else:
        next_state = ((state[0] + 1).bit_length(), int(str(state[1]).translate({str(i): str(i+1) for i in range(10)})))
        if next_state not in dp:
            dp[next_state] = solve_helper(next_state, m)
        return min(solve_helper(next_state, m), state[0])

dp = {}
solve()
