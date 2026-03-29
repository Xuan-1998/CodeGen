def partition(s):
    if len(s) == 0:
        return []
    
    result = []
    if s == s[::-1]:  # check if string is palindrome
        result.append([s])
    
    for i in range(1, len(s)):
        left = s[:i]
        right = s[i:]
        for p in partition(left):
            for q in partition(right):
                result.append([*p, *q])
    
    return result

def main():
    S = input()  # read the input string from stdin
    partitions = partition(S)
    print(partitions)  # print the results to stdout

if __name__ == "__main__":
    main()
