def min_cuts(s):
    n = len(s)
    min_cuts = 0

    for i in range(n):
        if not is_palindrome(s[:i+1]):
            min_cuts += 1

    return min_cuts

def is_palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    s = input()
    print(min_cuts(s))
