import sys

def min_mana_required(input):
    n = int(input().strip())
    k = list(map(int, input().strip().split()))
    h = list(map(int, input().strip().split()))

    dp = {0: 0}

    for i in range(1, n+1):
        if i > 1:
            min_mana = sys.maxsize
            for j in range(i):
                min_mana = min(min_mana, dp.get(j, 0) + (k[i] - k[j]))
            dp[k[i]] = min_mana + 1 if min_mana != sys.maxsize else 1
        else:
            dp[k[0]] = h[0]
    return dp[max(dp.keys())]

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        print(min_mana_required(input()))
