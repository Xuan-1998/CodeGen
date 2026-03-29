def maxScore(n, k, z, arr):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i > n or j < 0:
            return -1

        if j == 0:
            return arr[i-1]

        if i <= z and k - j + i - 1 >= 0:
            return max(dp(i-1, j-1) + arr[i-1], dp(i+1, j-1) + arr[i])
        else:
            return dp(i-1, j-1) + arr[i]

    return dp(n, k)

def main():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        print(maxScore(n, k, z, arr))

if __name__ == "__main__":
    main()
