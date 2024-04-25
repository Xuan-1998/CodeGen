def main():
    N, M, P = map(int, input().split())
    songs = [tuple(map(int, input().split())) for _ in range(N)]
    album_prices = list(map(int, input().split()))

    # Sort songs by album
    songs_by_album = [[] for _ in range(M + 1)]
    for a, p, v in songs:
        songs_by_album[a].append((p, v))

    # Initialize dp table
    dp = [[0] * (P + 1) for _ in range(M + 1)]

    # Dynamic programming
    for i in range(1, M + 1):
        for j in range(P + 1):
            dp[i][j] = dp[i - 1][j]  # Case where we don't buy the album
            for p, v in songs_by_album[i]:
                if j >= p:  # If we have enough budget to buy the song
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - p] + v)
            if j >= album_prices[i - 1]:  # If we have enough budget to buy the album
                total_greatness = sum(v for _, v in songs_by_album[i])
                dp[i][j] = max(dp[i][j], dp[i - 1][j - album_prices[i - 1]] + total_greatness)

    # Answer is the maximum value considering all albums and budget
    print(max(dp[M]))

if __name__ == "__main__":
    main()
