def get_palindromic_partitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    partitions = []
    if len(s) == 0:
        return [[]]
    elif len(s) == 1:
        return [[s]]

    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        if is_palindrome(left + right):
            for p in get_palindromic_partitions(right):
                partitions.append([left] + p)

    return partitions

if __name__ == "__main__":
    n = int(input())
    s = input()
    result = get_palindromic_partitions(s)
    print(result)
