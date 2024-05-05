def dp(i, k):
    if i == 0:
        return ""  # base case: empty string
    elif i < k:
        return s[i-1] + dp(i-1, k)  # duplicate the last character and recurse
    else:
        # we've reached or exceeded the desired length; try to delete the last char
        if s[:i-k+1].endswith(s[i-1]):  # if the string ends with the same char as the last one
            return dp(i-k, k)  # delete and recurse
        else:  # otherwise, duplicate the string and recurse
            return s + dp(k, k)

n, k = map(int, input().split())
s = input()
print(dp(n, k))
