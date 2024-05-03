def max_distance(commands, n):
    m = len(commands)
    memo = {}

    def dp(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        if i > 0:
            if commands[i-1] == 'F':
                res = max(dp(i-1, j, k), dp(i-1, min(j-1, n), k))
            else:  # commands[i-1] == 'T'
                res = dp(i-1, j, k-1) if k > 0 else 0
        else:
            res = 0

        memo[(i, j, k)] = res
        return res

    return max(dp(m, n, k) for k in range(n+1))

def read_input():
    commands = input().strip()
    n = int(input())
    return commands, n

if __name__ == "__main__":
    commands, n = read_input()
    print(max_distance(commands, n))
