def longest_palindrome(s):
    n = len(s)
    res = ""

    for i in range(n):
        for j in range(i+1, n+1):
            if s[i:j] == s[i:j][::-1]:
                if len(s[i:j]) > len(res):
                    res = s[i:j]

    print(res)
