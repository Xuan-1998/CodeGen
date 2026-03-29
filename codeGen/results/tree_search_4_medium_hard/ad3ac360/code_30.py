def is_palindrome(s):
    return s == s[::-1]

def min_cuts_to_partition_palindromes(s):
    n = len(s)
    memo = {0: True}
    cuts = 0

    for i in range(1, n + 1):
        if i not in memo:
            left = right = 0
            while left < i and right >= 0 and s[left] == s[right]:
                left += 1
                right -= 1
            if is_palindrome(s[left:right+1]):
                memo[i] = True
            else:
                cuts += 1
        if memo.get(i, False):
            continue
        for j in range(i - 1, 0, -1):
            while left < j and right >= 0 and s[left] == s[right]:
                left += 1
                right -= 1
            if is_palindrome(s[left:right+1]):
                memo[i] = True
                break

    return cuts

if __name__ == "__main__":
    n = int(input())
    s = input()
    print(min_cuts_to_partition_palindromes(s))
