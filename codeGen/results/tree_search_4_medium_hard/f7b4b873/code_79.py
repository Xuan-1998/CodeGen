def partition_palindromic(s):
    N = len(s)
    dp = [[[] for _ in range(N+1)] for _ in range(N+1)]

    def is_palindrome(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def partition(i, j):
        if i >= j or not is_palindrome(i, j):
            return []
        result = [[s[i:j+1]]]
        for k in range(i, j):
            left = s[i:k+1]
            right = s[k+1:j+1]
            if is_palindrome(0, len(left)-1) and is_palindrome(0, len(right)-1):
                result += [[left] + partition(k+1, j)] + [[right] + partition(i, k)]
        return [part for part in result if part]

    return partition(0, N-1)

if __name__ == "__main__":
    S = input()
    print(partition_palindromic(S))
