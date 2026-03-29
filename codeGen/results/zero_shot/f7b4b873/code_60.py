def partition_palindrome(s, start):
    if start >= len(s):
        return [[s]]
    
    partitions = []
    for i in range(start, len(s)):
        if s[start:i+1] == s[i:start-1:-1]:  # check if substring is palindrome
            for p in partition_palindrome(s[:start], 0):  # recursive call
                partitions.append([s[start:i+1]] + p)
    return partitions

def find_palindromic_partitions():
    S = input()  # receive the input string from stdin
    partitions = []
    for p in partition_palindrome(S, 0):
        print(p)  # print each palindromic partition

find_palindromic_partitions()
