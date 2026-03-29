def solve():
    n, k = map(int, input().split())
    s = input()

    if k >= n:
        return s  # If length of desired string is greater than or equal to original string, just return the original string

    if k < len(s):
        return s[:k]  # If length of desired string is less than the last character in the original string, just return the substring up to the last character
    else:
        return s + s[:-1]  # If length of desired string is equal to or greater than the last character in the original string, duplicate the original string and remove the last character

if __name__ == "__main__":
    solve()
