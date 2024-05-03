from collections import deque

n = int(input())  # number of commands that can be modified
cmds = input()    # sequence of turtle commands (T/F)

# Initialize DP table and memoization dictionary
dp = [[0] * (n + 1) for _ in range(len(cmds) + 1)]
memo = {}

def solve():
    queue = deque([(0, 0)])  # initialize queue with starting state (0 'T's, 0 commands)
    while queue:
        i, j = queue.popleft()
        if i > len(cmds):
            continue
        if (i, j) in memo:
            dp[i][j] = memo[(i, j)]
            continue
        cmd = cmds[i - 1]
        if cmd == 'T':
            queue.append((i + 1, j + 1))  # turn around and add one more 'T'
        else:
            queue.append((i + 1, j))
        dp[i][j] = max(dp[i-1][j-1] + (cmd == 'F'), dp[i-1][j])
    return max(dp[-1])

print(solve())
