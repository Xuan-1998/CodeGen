import sys

def is_palindrome(s):
    return s == s[::-1]

def get_palindromic_partitions(S):
    partitions = []
    for i in range(len(S)):
        for j in range(i+1, len(S)+1):
            substring = S[i:j]
            if is_palindrome(substring):
                partitions.append([substring])
    return partitions

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    partitions = get_palindromic_partitions(S)
    print(partitions)
