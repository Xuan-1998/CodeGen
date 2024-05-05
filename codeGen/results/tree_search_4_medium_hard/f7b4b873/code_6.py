def partition_palindromes(s):
    memo = [[] for _ in range(len(s) + 1)]
    memo[0].append([])

    def helper(i, partition):
        if i >= len(s):
            return [partition]
        partitions = []
        j = i - 1
        while j >= 0 and s[i] == s[j]:
            j -= 1
        if j >= 0:
            partitions.extend(helper(j + 1, partition + [s[i - j: i + 1]]))
        if not s[i].lower():
            partitions.extend(helper(i + 1, partition + [s[i]]))
        return partitions

    return set([p for p in helper(0, [])])
