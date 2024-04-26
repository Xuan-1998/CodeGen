def can_be_palindrome():
    N = int(input())
    S = input()

    left, right = 0, N-1
    while left < right:
        if S[left] != S[right]:
            print('YES')
            return
        left += 1
        right -= 1

    print('NO')

can_be_palindrome()
