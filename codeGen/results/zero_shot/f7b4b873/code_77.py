def is_palindrome(part):
    return part == part[::-1]

def filter_partitions(partitions):
    palindromic_partitions = []
    for p in partitions:
        if is_palindrome(''.join(p)):
            palindromic_partitions.append(p)
    return palindromic_partitions

result = all_partitions(s)  # get the result from Step 1
palindromic_partitions = filter_partitions(result)
print(palindromic_partitions)  # print the final result to stdout
