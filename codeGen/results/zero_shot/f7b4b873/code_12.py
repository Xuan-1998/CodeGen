def partition_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    result = []
    for i in range(1, len(s)):
        for j in range(i, 0, -1):
            partition = s[:j][::-1] + s[j:]
            if is_palindrome(partition):
                result.append([s[:j], partition])
    
    return result

if __name__ == "__main__":
    s = input()
    print(partition_palindromes(s))
