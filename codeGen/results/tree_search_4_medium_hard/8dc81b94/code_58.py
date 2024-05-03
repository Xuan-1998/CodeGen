from collections import deque

def is_zero_possible(a):
    n = len(a)
    dp = [True] + [False] * n
    for i in range(1, n+1):
        if dp[i-1] and sum(a[:i]) == i:
            dp[i] = True
        elif not dp[i-1] and sum(a[i:]) == 0:
            dp[i] = True
    return dp[-1]

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        a = list(map(int, input().split()))
        print('YES' if is_zero_possible(a) else 'NO')

if __name__ == "__main__":
    main()
