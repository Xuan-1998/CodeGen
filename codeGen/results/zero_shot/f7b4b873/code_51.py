def find_palindromic_partitions():
    s = input()  # read the string from stdin
    partitions = partition_helper(s, [])
    return partitions

print(find_palindromic_partitions())  # print the result to stdout
