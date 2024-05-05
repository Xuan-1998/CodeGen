def partition_palindromic(s):
    def helper(s, p):
        if s == '':
            return [p]
        dp = {}
        for i in range(len(s)):
            if s[i] == s[~i]:
                if i == 0:
                    # odd-length palindrome
                    res = helper(s[1:], p + [s[:2]])
                elif i > 0 and s[:i+1] == s[:i+1][::-1]:
                    # even-length palindrome
                    res = helper(s[i+1:], p + [s[:i+1]])
                dp[s[:i+1]] = res
        return dp.get('','')

    return [p for p in partition_palindromic(input()).split('\n') if p]
