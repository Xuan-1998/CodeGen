def all_palindromic_partitions(S):
    memo = {}
    def helper(i, partition):
        if (i, tuple(partition)) in memo:
            return memo[(i, tuple(partition))]
        if i >= len(S):
            return [partition]
        result = []
        for j in range(i, -1, -1):
            if S[j] == S[i]:
                new_partition = partition + [S[j:i+1]]
                result.extend(helper(j-1, new_partition))
        memo[(i, tuple(partition))] = result
        return result

    return helper(0, [])

# Receive input from stdin and print the output to stdout
S = input()
print(all_palindromic_partitions(S))
