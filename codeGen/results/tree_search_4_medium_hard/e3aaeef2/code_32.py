def get_length(n, m):
    dp = {}
    for i in range(1, n + 1):
        if len(str(i)) == 1:
            dp[i] = [i]
        else:
            temp = []
            for d in str(i):
                j = int(d) + 1
                temp.append(j)
            dp[i] = get_length(int(''.join(map(str, temp))), m - 1)
    return len(str(n)) + sum([len(str(x)) - 1 if isinstance(x, list) else 0 for x in dp[n][m % (len(str(n)))].split('.')])

# Read input from stdin
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(get_length(n, m) % (10**9 + 7))
