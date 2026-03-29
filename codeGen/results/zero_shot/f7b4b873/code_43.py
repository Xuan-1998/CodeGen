def is_palindrome(s):
    return s == s[::-1]

def get_palindromic_partitions(s):
    partitions = []
    def recursive_partition(partition, remaining_string):
        if not remaining_string:
            partitions.append(list(partition))
            return
        for i in range(1, len(remaining_string) + 1):
            substring = remaining_string[:i]
            if is_palindrome(substring):
                recursive_partition(partition + [substring], remaining_string[i:])
    recursive_partition([], s)
    return partitions

if __name__ == "__main__":
    S = input()
    print(get_palindromic_partitions(S))
