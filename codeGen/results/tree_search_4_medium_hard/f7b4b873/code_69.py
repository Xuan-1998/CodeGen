def palindromic_partitions(s):
    memo = {}

    def recursive_partition(s, current_partition):
        if s == "":
            return [current_partition]
        result = []
        for i in range(1, len(s) + 1):
            left = s[:i]
            right = s[i:][::-1]
            if left == right:
                new_partition = current_partition + [left]
                result.extend(recursive_partition(s[i:], new_partition))
        return result

    return recursive_partition(s, [])

print(palindromic_partitions(input()))
