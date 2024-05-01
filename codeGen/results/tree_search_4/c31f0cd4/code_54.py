def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    dp = {0: []}
    
    for num in nums:
        new_dp = {}
        for s, subsets in dp.items():
            for subset in subsets:
                new_sum = s + num
                if new_sum not in new_dp:
                    new_dp[new_sum] = []
                new_dp[new_sum].extend([subset | {num}] for _ in range(len(subset)))
                new_dp[new_sum].append(set())
        
        dp.update(new_dp)
    
    sums = sorted(dp.keys())
    print(' '.join(map(str, sums)))

if __name__ == "__main__":
    solve()
