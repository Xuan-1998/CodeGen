from collections import defaultdict

def coin_game(X, M):
    dp = defaultdict(int)
    result = []

    for i in range(1, X+1):
        if i % 2 == 0:
            j = (X - (i // 2)) % M + 1
        else:
            j = (i - 1) % M + 1

        dp[i] = j
        result.append(j)

    return result


T = int(input())
for _ in range(T):
    X, M = map(int, input().split())
    print(*coin_game(X, M), sep='\n')
