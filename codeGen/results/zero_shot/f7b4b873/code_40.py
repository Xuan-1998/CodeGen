def partition(s):
    def is_palindrome(sub_s):
        return sub_s == sub_s[::-1]

    n = len(s)
    result = []

    for i in range(n):
        for j in range(i+1, n+1):
            if is_palindrome(s[i:j]):
                result.append([s[i:j]])

    return result

n = int(input())
s = input()
print(partition(s))
