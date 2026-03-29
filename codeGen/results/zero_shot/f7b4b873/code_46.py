def partition(s):
    if len(s) == 0:  # base case: empty string has one partition (the empty string)
        return [[]]
    partitions = []
    for i in range(1, len(s)+1):  # iterate over possible partitions
        prefix = s[:i]  # get the prefix of the current partition
        suffix = s[i:]  # get the suffix of the current partition
        if prefix == prefix[::-1]:  # check if the prefix is a palindrome
            for p in partition(suffix):  # recursively generate partitions of the suffix
                partitions.append([prefix] + p)  # add the prefix to each partition
    return partitions

def palindromic_partitions(S):
    partitions = partition(S)
    palindromic_partitions = []
    for partition in partitions:
        if all(p == p[::-1] for p in partition):  # check if each partition is a palindrome
            palindromic_partitions.append(partition)
    return palindromic_partitions

if __name__ == "__main__":
    S = input()  # read the input string from stdin
    partitions = palindromic_partitions(S)
    for partition in partitions:
        print(partition)  # print each partition to stdout
