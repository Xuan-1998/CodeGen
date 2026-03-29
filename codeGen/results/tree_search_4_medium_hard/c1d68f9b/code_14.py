import sys

def can_form_polygon(moods):
    n = len(moods)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize dp[0][0] to 1, since one configuration always exists: an empty polygon.
    dp[0][0] = 1

    for i in range(1, n):
        for k in range(min(i + 1, n)):
            if moods[i - 1]:
                # If the mood is good (1), increment the number of valid configurations by the previous value in dp.
                dp[i][k] = dp[i - 1][max(0, k - 1)] + dp[i - 1][k]
            else:
                # If the mood is bad (0), reset the state back to 0.
                dp[i][k] = 0

    return "YES" if dp[-1][-1] > 0 else "NO"

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    moods = list(map(int, sys.stdin.readline().split()))
    print(can_form_polygon(moods))
