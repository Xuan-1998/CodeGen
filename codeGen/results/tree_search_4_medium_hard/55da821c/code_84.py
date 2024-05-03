import sys
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    plant_info = []
    for _ in range(n):
        s, x = map(float, input().split())
        plant_info.append((int(s), x))

    # Sort the plants by their positions
    plant_info.sort(key=lambda x: x[1])

    dp = [[0] * (m + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(i):
            left_plants = sum(1 for k in range(j) if plant_info[k][0] == i)
            right_plants = n - left_plants
            dp[i][j] = min(dp[i-1][j-1] + left_plants, dp[i-1][j] + right_plants)

    # Calculate the minimum number of plants that need to be replanted
    ans = dp[m][0]
    for i in range(m):
        if plant_info[0].species != i + 1:
            ans += 1

    print(ans)

if __name__ == "__main__":
    main()
