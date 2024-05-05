def partition_palindromes(s):
    n = len(s)
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the diagonal elements
    for i in range(n + 1):
        dp[i][i] = True
    
    # Fill up the table in a bottom-up manner
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length
            if s[i] == s[j - 1]:
                dp[i][j - 1] = (length % 2 == 0 and dp[(i + 1)][(j - 1) - 1]) or \
                               ((length % 2 != 0) and dp[(i + 1)][j - 2])
            else:
                dp[i][j - 1] = False
    
    # Construct all palindromic partitions
    def construct_partition(i, j):
        if i > j:
            return [""]
        elif i == j:
            return [["" + s[i]]]
        else:
            result = []
            for k in range(i, j):
                if dp[i][k] and dp[k + 1][j]:
                    for partition1 in construct_partition(i, k):
                        for partition2 in construct_partition(k + 1, j):
                            result.append([partitions[0]] + partition1 + [""] + partition2)
            return result
    
    partitions = construct_partition(0, n - 1)
    
    return partitions

# Read the input string
s = input().strip()

# Generate all palindromic partitions and print them
partitions = partition_palindromes(s)

for p in partitions:
    print(p)
