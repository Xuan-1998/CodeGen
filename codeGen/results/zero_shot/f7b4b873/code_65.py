def palindromic_partitions(s):
    if len(s) <= 1:  # base case: empty or single-character string
        return [s] if s else []

    partitions = []
    for i in range(len(s)):
        prefix = s[:i+1]
        if prefix == prefix[::-1]:  # check if prefix is a palindrome
            suffix = s[i+1:]
            for partition in palindromic_partitions(suffix):
                partitions.append([prefix] + partition)

    return partitions

def main():
    s = input()  # read the input string from stdin
    partitions = palindromic_partitions(s)
    print(partitions)  # output the result to stdout

if __name__ == "__main__":
    main()
