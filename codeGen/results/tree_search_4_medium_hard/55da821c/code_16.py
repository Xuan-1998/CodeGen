import sys

def min_replanting_operations():
    n, m = map(int, input().split())
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    species_count = [0] * (m + 1)

    for i in range(1, n + 1):
        s_i, x_i = map(int, input().split())
        section = int(x_i / 10**9)
        remaining_xi = int((x_i % (10**9)) * (10**9))

        # Calculate the minimum number of replanting operations needed
        for k in range(1, min(i + 1, m) + 1):
            if species_count[k] == s_i:
                dp[i][k] = dp[i - 1][k]
            else:
                dp[i][k] = min(dp[i - 1][k], dp[i - 1][k - 1]) + (s_i != k)

        # Update the remaining plants
        species_count[section] += s_i

    return min(dp[-1])

if __name__ == "__main__":
    print(min_replanting_operations())
