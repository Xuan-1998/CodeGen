def main():
    n, m = map(int, input().split())
    visited = [False]*n
    memo = {}
    max_beauty = 0
    for i in range(n):
        max_beauty = max(max_beauty, dp(i))
    print(max_beauty)
