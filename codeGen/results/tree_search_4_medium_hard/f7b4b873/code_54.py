def partition_palindromes(s):
    memo = {}

    def is_palindrome(s):
        return s == s[::-1]

    def partition(s):
        if s in memo:
            return memo[s]
        
        result = []
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if is_palindrome(substr):
                    if j == len(s):
                        result.append([substr])
                    else:
                        for p in partition(s[:i] + s[j:]):
                            result.append([substr] + p)
        memo[s] = result
        return result

    return partition(s)

def main():
    S = input()
    palindromic_partitions = partition_palindromes(S)
    print(palindromic_partitions)

if __name__ == "__main__":
    main()
