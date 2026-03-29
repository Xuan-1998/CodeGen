def min_cuts(s):
    n = len(s)
    cuts = 0
    for i in range(n-1):
        left = s[:i+1]
        right = s[i+1:][::-1]  # Reverse the substring
        if left != right:  # If the substrings are not palindromes
            cuts += 1
    return cuts

if __name__ == "__main__":
    n = int(input())  # Read the length of the string from stdin
    s = input().strip()  # Read the string itself from stdin
    print(min_cuts(s))  # Print the minimum number of cuts required
