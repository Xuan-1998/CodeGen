def max_score(array):
    n, k, z = array[0], array[1], array[2]
    dp = [0] * (n + 1)
    dp[0] = array[3]

    for i in range(1, n):
        score = dp[i-1] if i < z else dp[i-z-1]
        dp[i] = max(score + array[i], dp[i-1] + array[i-1])

    return dp[-1]

def main():
    t = int(input())
    for _ in range(t):
        n, k, z = map(int, input().split())
        array = list(map(int, input().split()))
        print(max_score(array))

if __name__ == "__main__":
    main()
