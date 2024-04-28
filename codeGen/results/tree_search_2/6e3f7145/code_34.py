def longest_palindrome(s):
    n = len(s)
    p = [0] * n

    for i in range(1, n):
        if s[i - 1] == s[i]:
            p[i] = (p[i - 2] + 1) if i >= 2 else 1
        elif i > 1 and s[i - 1] == s[i - 1 - p[i - 1]]:
            p[i] = p[i - 1]
        else:
            p[i] = 0

    max_length = 0
    center_index = 0
    for i in range(n):
        if p[i] > max_length:
            max_length = p[i]
            center_index = i

    return s[center_index - max_length: center_index + max_length]

if __name__ == "__main__":
    s = input()
    print(longest_palindrome(s))
