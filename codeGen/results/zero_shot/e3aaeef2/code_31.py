def solve():
    t = int(input())  # read the number of test cases

    for _ in range(t):
        n, m = map(int, input().split())  # read n and m
        length = len(str(n))  # initial length of n
        for _ in range(m):
            if '9' in str(n):  # check if any digits are 9
                length += 1  # increment the length by 1
            else:
                length -= 1  # decrement the length by 1 (since all digits increase by 1)
        print(length % (10**9 + 7))  # print the final length modulo 10^9+7

solve()
