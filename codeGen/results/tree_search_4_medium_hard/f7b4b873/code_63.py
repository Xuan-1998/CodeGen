def partition(s):
    memo = {}

    def is_palindrome(substring):
        return substring == substring[::-1]

    def partition_recursive(remaining_substr, prev_partition):
        if not remaining_substr:
            return [prev_partition]
        
        partitions = []
        for i in range(len(remaining_substr)):
            substr = remaining_substr[:i+1]
            if is_palindrome(substr):
                new_partition = prev_partition + [substr]
                if remaining_substr[i+1:]:
                    partitions += partition_recursive(remaining_substr[i+1:], new_partition)
                else:
                    partitions.append(new_partition)
        return partitions

    result = memo.get(s, None)
    if not result:
        result = partition_recursive(s, [])
        memo[s] = result
    return result

s = input()
print(partition(s))
