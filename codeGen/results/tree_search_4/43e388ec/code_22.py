import sys

def solve():
    a, b = map(int, input().split())
    memo = {0: 0}
    for i in range(1, 315161):
        if i % 2 == 0:
            memo[i] = memo.get(i-1, 0) + b
        else:
            memo[i] = memo.get(i-1, 0) + (b << 1)
    print(memo[314159] % (10**9+7))

if __name__ == "__main__":
    solve()
