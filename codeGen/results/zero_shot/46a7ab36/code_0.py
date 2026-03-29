def count_words(n, m):
    if m == 0:  # base case: empty string has 1 possibility
        return 1

    possibilities = 0
    for i in range(1, n + 1):  # iterate over alphabet indices
        if 2 * i > n:  # place letter at any position
            possibilities += n ** (m - 1)  # n choices for each of m-1 positions
        elif 2 * i <= n:  # place letter and follow with a letter >= 2*i
            possibilities += n * count_words(n, m - 1)
    return possibilities % (10**8 + 7)  # modulo 10^8+7

t = int(input())  # read number of test cases
for _ in range(t):
    n, m = map(int, input().split())  # read n and m for each test case
    print(count_words(n, m))  # call the recursive function and print result
