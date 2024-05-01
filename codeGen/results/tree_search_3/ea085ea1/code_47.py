import sys

def find_max_common_substrings():
    N = int(input())
    str1 = input().strip()
    str2 = input().strip()

    max_length = 0
    for length in range(1, N + 1):
        for i in range(N - length + 1):
            substr1 = str1[i:i+length]
            if substr1 in str2:
                max_length = length
                break

    return max_length

print(find_max_common_substrings())
