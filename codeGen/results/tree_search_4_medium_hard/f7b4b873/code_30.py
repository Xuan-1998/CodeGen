import itertools

def find_palindromic_partitions(s):
    def is_palindrome(substring):
        return substring == substring[::-1]

    partitions = []
    for r in range(1, len(s) + 1):  # consider all possible lengths of partitions
        for partition in itertools.combinations(s, r):
            if is_palindrome(''.join(partition)):
                partitions.append(list(partition))
    return partitions

s = input()  # read the input string from stdin
print(find_palindromic_partitions(s))  # print the result to stdout
