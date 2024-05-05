def can_cross_stones(stone_positions):
    k = (stone_positions[-1] - stone_positions[0]) // 2
    dp = {0: True}
    
    for i in range(1, len(stone_positions)):
        dp[i] = any((i-1) <= j <= (i+k+1) and dp.get(j, False) for j in range(max(0, i-k-2), min(i, len(stone_positions)-1)))
        
    return dp[-1]

def main():
    num_stones = int(input())
    stone_positions = list(map(int, input().split()))
    print(can_cross_stones(stone_positions))

if __name__ == "__main__":
    main()
