import sys

def min_cuts(s):
    n = len(s)
    dp = [True] * (n + 1)  # Initialize dp array with True values

    for i in range(1, n + 1):
        for j in range(i):  # Consider all substrings of length j
            if s[j:i].lower() != s[i:j].lower():  # If the substring is not a palindrome
                dp[i] = False  # Set dp[i] to False
                break  # Stop considering this substring

    cuts = 0
    for i in range(1, n):
        if not dp[i]:  # If the substring is not a palindrome
            cuts += 1  # Increment the cut count

    return cuts

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
