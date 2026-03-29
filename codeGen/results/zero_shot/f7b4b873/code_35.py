def find_palindromic_partitions(S):
    def is_palindrome(s):
        return s == s[::-1]

    def partition(s, path):
        if not s:
            partitions.append(path)
            return
        for i in range(1, len(s) + 1):
            if is_palindrome(s[:i]):
                partition(s[i:], path + [s[:i]])

    partitions = []
    partition(S, [])
    return partitions

S = input()  # receive input from stdin
partitions = find_palindromic_partitions(S)
print(partitions)  # print the result to stdout
