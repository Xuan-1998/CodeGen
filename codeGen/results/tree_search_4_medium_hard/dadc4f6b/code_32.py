def solve():
    n, q, c = map(int, input().split())
    
    # Initialize a 2D table with zeros to represent unknown values.
    dp = [[0] * (q + 1) for _ in range(101)]

    # Read the stars' information and store them in a list of lists.
    stars = []
    for _ in range(n):
        x, y, s = map(int, input().split())
        stars.append((x, y, s))

    # Iterate over each view and update the dynamic programming table accordingly.
    for t in range(1, q + 1):
        x1, y1, x2, y2 = map(int, input().split())

        # Calculate the total brightness for the current view by iterating over all stars that fall within the viewed rectangle.
        for i in range(len(stars)):
            if (stars[i][0] >= x1 and stars[i][0] <= x2) and (stars[i][1] >= y1 and stars[i][1] <= y2):
                dp[t][t] += stars[i][2]

    # Print the total brightness of stars in each view.
    for i in range(1, q + 1):
        print(dp[i][i])

if __name__ == "__main__":
    solve()
