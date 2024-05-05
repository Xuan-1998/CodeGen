def palindromic_partitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    partitions = [[]]
    for char in s:
        new_partitions = []
        for partition in partitions:
            new_partition = partition + [char]
            if is_palindrome(''.join(new_partition)):
                new_partitions.append(new_partition)
            for i in range(1, len(partition) + 1):
                new_partition = partition[:i] + [char] + partition[i:]
                if is_palindrome(''.join(new_partition)):
                    new_partitions.append(new_partition)
        partitions.extend(new_partitions)

    return [partition for partition in partitions if ''.join(partition) == s]
