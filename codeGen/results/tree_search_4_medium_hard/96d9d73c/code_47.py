from sys import stdin

def solve():
    n, k, m = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))

    memo = {(0, 1): True}

    for i in range(1, n):
        for j in range(1, min(i+1, k)+1):
            if (j == 1 or memo[(i-1, j-1)] and abs(a[i] - a[i-j]) <= m):
                memo[(i, j)] = True
            else:
                memo[(i, j)] = False

    return memo.get((n-1, k-1), False)

if __name__ == "__main__":
    print(solve())
