import sys

def is_palindrome(s):
    return s == s[::-1]

def palindromic_partitions(s):
    result = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if is_palindrome(substring):
                result.append([substring])
    return result

if __name__ == "__main__":
    S = sys.stdin.readline().strip()
    partitions = palindromic_partitions(S)
    for partition in partitions:
        print(partition)
