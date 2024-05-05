def partition_palindromes(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    # Initialize base case: single characters are palindromic
    for i in range(n + 1):
        dp[i][i] = True

    # Fill up the dp table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i] == s[j - 1]:
                dp[i][j - 1] = dp[i + 1][j - 2] or True
            else:
                dp[i][j - 1] = False

    def is_palindromic_partition(partition):
        # Check if the partition is palindromic by checking if the first and last characters are equal
        # and the middle characters form a palindrome
        return partition[0] == partition[-1] and ''.join(partition).lower() == ''.join(partition)[::-1].lower()

    partitions = []
    for i in range(n):
        for j in range(i, n):
            if dp[i][j]:
                partition = [s[i:j + 1]]
                while len(s) > j + 1:
                    j += 1
                    partition.append(s[j])
                    if ''.join(partition).lower() == ''.join(partition)[::-1].lower():
                        break
                if is_palindromic_partition(partition):
                    partitions.append(partition)

    return partitions

# Read input from stdin
s = input()

# Print the output to stdout
print(partition_palindromes(s))
