import sys

def partition_palindromes(s):
    def is_palindrome(s):
        return s == s[::-1]

    dp = {}
    partitions = []
    rev_index = len(s) - 1

    for i in range(len(s)):
        if s[i] == s[rev_index]:
            rev_index -= 1
        else:
            if (s[:i+1] in dp or is_palindrome(s[:i+1])):
                dp[s[:i+1]] = True
                partitions.append([s[:i+1]])
            rev_index = len(s) - 1

    return partitions

# Read input from stdin and write output to stdout
if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(partition_palindromes(s))
