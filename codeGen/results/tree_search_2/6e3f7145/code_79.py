import sys
def longest_palindrome(s):
    n = len(s)
    max_len = 0
    result = ""
    
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            
            if substr == substr[::-1]:
                if len(substr) > max_len:
                    max_len = len(substr)
                    result = substr
                    
    return result

if __name__ == "__main__":
    s = input()
    print(longest_palindrome(s))
