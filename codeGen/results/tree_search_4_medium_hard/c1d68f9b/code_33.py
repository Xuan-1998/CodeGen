def can_form_polygon(n, moods):
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            if moods[j] != moods[j - 1]:
                dp[i][j] = (dp[i][j - 1] or not dp[i - 1][j - 1]) and all(mood == moods[0] for mood in moods[:i])
    return "YES" if dp[n][n-1] else "NO"

def main():
    n = int(input())
    moods = [int(x) for x in input().split()]
    print(can_form_polygon(n, moods))

if __name__ == "__main__":
    main()
