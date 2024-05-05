import sys

t = int(input())  # number of test cases
for _ in range(t):
    n, m = map(int, input().split())
    result = str(n)  # initialize the result with the initial number
    for _ in range(m):
        new_result = ''
        carry = 0
        for digit in result:
            if int(digit) + 1 + carry >= 10:  # add 1 and check for carry
                new_result += '0' + str((int(digit) + 1 + carry) % 10)
                carry = 1
            else:  # no carry, just increment the digit
                new_result += str(int(digit) + 1 + carry)
                carry = 0
        result = new_result if carry == 0 else '1' + new_result[:-1]  # append a leading 1 for the carry
    print(len(result) % (10**9 + 7))  # print the length of the resulting number modulo 10^9+7
