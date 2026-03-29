def find_palindromic_partitions(s):
    def is_palindrome(s):
        return s == s[::-1]

    partitions = []
    for i in range(1, len(s) + 1):
        for j in range(len(s) - i + 1):
            substring = s[j:j+i]
            if is_palindrome(substring):
                partitions.append([substring])
    return partitions

if __name__ == "__main__":
    n = int(input())
    S = input()
    result = find_palindromic_partitions(S)
    print(result)
