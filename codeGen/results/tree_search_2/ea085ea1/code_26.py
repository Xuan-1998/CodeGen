def common_substrings(str1, str2):
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(str1) or j == len(str2):
            return 0

        same_chars = set(str1[i:j+1]) & set(str2[0:(j-i)+1])

        if not same_chars:
            result = dp(i+1, j+1)
        else:
            max_length = min(j-i+1, len(same_chars))
            for k in range(1, max_length):
                if str1[i:i+k] == str2[0:k]:
                    result = 1 + dp(i+k, j)
                    break
            else:
                result = 0

        memo[(i, j)] = result
        return result

    return dp(0, len(str1)-1)

# Example usage
str1 = input()
str2 = input()

print(common_substrings(str1, str2))
