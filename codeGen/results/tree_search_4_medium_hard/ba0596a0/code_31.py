def can_cross_stones(stone_positions):
    n = len(stone_positions)
    dp = [False] * n
    dp[0] = True

    for i in range(1, n):
        for j in range(max(0, i-k), min(n-1, i+k+1)):
            if abs(i-j) in (k-1, k, k+1) and dp[j]:
                dp[i] = True
                break

    return dp[-1]

def main():
    n = int(input())
    stone_positions = list(map(int, input().split()))
    k = 1 # assume the frog can jump any distance (k-1, k, k+1)
    print(can_cross_stones(stone_positions))

if __name__ == "__main__":
    main()
