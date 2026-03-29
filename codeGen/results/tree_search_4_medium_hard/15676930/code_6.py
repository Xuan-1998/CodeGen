from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return 0
    elif j == 0:
        return sum(a_k for a_k in a_1:i+1) - i
    else:
        # Feed the current hare and make its adjacent hares full
        feed = c_i + dp(i-1, j-1)
        # Don't feed the current hare
        not_feed = b_i + dp(i-1, j)
        return max(feed, not_feed)

n = int(input())
a_1:n+1 = list(map(int, input().split()))
b_1:n+1 = list(map(int, input().split()))
c_1:n+1 = list(map(int, input().split()))

print(dp(n, 0))
