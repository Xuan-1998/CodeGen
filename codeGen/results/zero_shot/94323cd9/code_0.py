# Step 1: Parse Input
N, M, P = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(N)]  # (album_id, price, greatness)
album_prices = list(map(int, input().split()))

# Step 2: Preprocess Data
albums = {i: [] for i in range(1, M + 1)}
for album_id, price, greatness in songs:
    albums[album_id].append((price, greatness))

album_total = []
for i in range(1, M + 1):
    total_price = sum(song[0] for song in albums[i])
    total_greatness = sum(song[1] for song in albums[i])
    album_total.append((total_price, total_greatness, album_prices[i-1]))

# Step 3: Dynamic Programming (DP)
# Initialize the DP table where dp[i] is the max greatness with i budget
dp = [0] * (P + 1)

# Step 4: DP Transition
# First, consider buying songs individually
for album_id, price, greatness in songs:
    for budget in range(P, price - 1, -1):
        dp[budget] = max(dp[budget], dp[budget - price] + greatness)

# Then, consider buying albums
for total_price, total_greatness, album_price in album_total:
    if total_price > album_price:  # Optimization step
        for budget in range(P, album_price - 1, -1):
            dp[budget] = max(dp[budget], dp[budget - album_price] + total_greatness)

# Step 7: Output the Result
print(dp[P])
