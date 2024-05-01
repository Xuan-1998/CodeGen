import sys

def read_input():
    N = int(sys.stdin.readline())
    str1 = sys.stdin.readline().strip()
    str2 = sys.stdin.readline().strip()
    return N, str1, str2

def solve(N, str1, str2):
    # Preprocess the input strings
    # Create a suffix tree for each string using pyucsd or implement it ourselves
    # For simplicity, let's just use the naive approach and iterate through all substrings
    max_common = 0
    for i in range(N):
        for j in range(i + 1, N):
            substring = str1[i:j]
            if substring in str2:
                # Check if this is a non-overlapping common substring
                last_occurrence = -1
                for k in range(len(str2)):
                    if str2[k:k+len(substring)] == substring:
                        last_occurrence = k
                        break
                if last_occurrence == -1 or last_occurrence + len(substring) <= N:
                    max_common += 1

    return max_common

N, str1, str2 = read_input()
print(solve(N, str1, str2))
