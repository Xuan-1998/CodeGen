def partition_palindromes(S):
    n = len(S)
    dp = [[False] * (n+1) for _ in range(n+1)]

    # Base case: single characters are always palindromes
    for i in range(n+1):
        dp[i][i] = True

    for i in range(n-1, -1, -1):
        for j in range(i+1, n+1):
            if S[i] == S[j]:
                dp[i][j] = (j - i < 2) or (dp[i+1][j-1])
            else:
                # If the substring is not a palindrome, break
                break

    partitions = []
    for i in range(n+1):
        for j in range(i, n+1):
            if dp[i][j]:
                partition = [S[i:j+1]]
                while j < n and S[j] == S[n-j-1]:
                    j += 1
                if j < n:
                    partition.append(S[j+1:n])
                partitions.append(partition)

    return partitions

# Example usage:
S = input()  # Read the input string from stdin
print(partition_palindromes(S))  # Print the list of palindromic partitions
