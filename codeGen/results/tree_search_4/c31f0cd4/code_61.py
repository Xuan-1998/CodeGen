import sys

def subset_sum_sums(a):
    N = len(a)
    max_val = max(a)
    
    # Create the 2D table dp where rows represent the subsets and columns represent the sums.
    dp = [[-1] * (sum(a) + 1) for _ in range(1 << N)]
    
    # Initialize all values to -1, except for dp({set()}, {0}) which is set to 0.
    dp[0][0] = 0
    
    # For each subset s in subsets:
    for s in range(1 << N):
        for i in range(sum(a) + 1):
            if i == 0: 
                # If i == 0, then dp_state = (s, i) means that no elements have been added yet, so we can add any element from the original set and calculate its sum with current_sum. 
                continue
            elif i > 0:
                for e in a:
                    if (1 << N - 1) & s: 
                        # For each element e in s:
                            if e <= i: 
                                # If e <= i, add e to s' and calculate its sum with current_sum. 
                                dp[s][i] = max(dp[s][i], dp[s ^ (1 << N - 1)][i - e])
    
    return [i for i in range(sum(a) + 1) if dp[-1][i] != -1]

a = list(map(int, input().split()))
print(" ".join(map(str, subset_sum_sums(a))))
