def palindromic_partitions(S):
    N = len(S)
    dp = [[False] * (N + 1) for _ in range(N + 1)]
    
    # Initialize dp[0][0] to True and set all other cells in the first row and column to False
    dp[0][0] = True
    
    partitions = []
    
    for i in range(1, N + 1):
        for j in range(i, -1, -1):  # Iterate over possible partitions of S[0..i]
            if S[j:i+1] == S[j:i+1][::-1]:  # Check if the substring is palindromic
                prev_i = i - 1
                for k in range(j - 1, -1, -1):  # Iterate over possible partitions of S[0..j-1]
                    left = S[:k].rstrip()
                    right = S[k:i+1].lstrip()
                    if dp[k][i] and left == left[::-1] and right == right[::-1]:  # Check if the partition is palindromic
                        partitions.append([left, right])
    
    return [partition for partition in partitions if partition[0] + partition[1] == S]

S = input()  # Read the input string from stdin
print(palindromic_partitions(S))  # Print the list of palindromic partitions to stdout
