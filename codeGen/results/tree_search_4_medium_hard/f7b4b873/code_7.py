def palindromic_partitions(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    memo = {}

    def dfs(i, partition):
        if i >= len(s):
            return [partition]
        if (i, tuple(partition)) in memo:
            return memo[(i, tuple(partition))]
        result = []
        for j in range(i-1, -1, -1):
            if is_palindrome(s[j:i+1]):
                new_partition = partition + [s[j:i+1]]
                result.extend(dfs(j, new_partition))
        if not result:
            result = [[]]
        memo[(i, tuple(partition))] = result
        return result

    return dfs(0, [])

if __name__ == "__main__":
    s = input()
    print(palindromic_partitions(s))
