import sys

def is_palindrome(s):
    return s == s[::-1]

def partition(s):
    if len(s) == 0:
        return [[]]
    partitions = []
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        if is_palindrome(left + right):
            partitions.extend([left] + p for p in partition(right))
    return partitions

def main():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    palindromic_partitions = []
    for i in range(N+1):
        for j in range(i, 0, -1):
            left = S[:j]
            right = S[j:]
            if is_palindrome(left + right):
                palindromic_partitions.append([left] + p for p in partition(right))
    print(palindromic_partitions)

if __name__ == "__main__":
    main()
