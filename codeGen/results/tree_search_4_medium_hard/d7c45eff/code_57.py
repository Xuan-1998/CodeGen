def smallest_string(n, k):
    memo = {}

    def dp(i):
        if i == 0:
            return ""
        if i < n:  # If i is less than the original string length
            if s[n-i+1] <= s[n-i]:  # Consider deleting the last character
                return dp(i-1)
            else:  # Duplicate the string
                return dp(i-1) + s[n-i+1]
        else:
            # Since i >= n, we can only duplicate the original string
            if k % n == 0:
                return s * (k // n)
            elif k < n:
                return s[:k]
            else:  # k > n and not a multiple of n
                return dp(k-1) + s[k-n]

    s = input().strip()
    for _ in range(int(input())):
        n, k = map(int, input().split())
        if k < n:
            print(s[:k])
        else:
            result = dp(k)
            print(result)

