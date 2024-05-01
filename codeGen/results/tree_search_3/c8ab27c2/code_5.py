from collections import defaultdict

def minUncommonLength(S, T):
    # Create a hashmap to store the frequency of each prefix in both strings
    prefix_freq = defaultdict(int)
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            prefix = S[i:j]
            if prefix in T:
                prefix_freq[prefix] += 1

    # Initialize the dp array with a value indicating that there are no uncommon subsequences
    dp = [[-1]*(len(T)+1) for _ in range(len(S)+1)]

    # Initialize the state as (prefix, i)
    state = {"prefix": "", "index": 0}

    # Fill up the dp array using dynamic programming
    for i in range(1, len(S)+1):
        for j in range(1, len(T)+1):
            if S[i-1] == T[j-1]:
                state["prefix"] += S[i-1]
                state["index"] = j
                dp[i][j] = dp[state["index"]-1][state["index"]-1]
            else:
                # If the current prefix is not common, update the length of the uncommon subsequence
                if prefix_freq.get(state["prefix"], 0) == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Return the length of the shortest uncommon subsequence
    return -min([dp[i][len(T)] for i in range(len(S)+1)])

if __name__ == "__main__":
    S, T = input().split()
    print(minUncommonLength(S, T))
