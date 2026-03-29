def solve():
    t = int(input())  # read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # read the initial number and operations
        digits = str(n)  # convert the number to a string
        for _ in range(m):
            new_digits = ''
            for d in digits:
                if int(d) == 9:  # special case when digit is 9
                    new_digits += '0'
                else:
                    new_digits += str(int(d) + 1)
            digits = new_digits
        print(len(digits))  # print the length of the resulting string

if __name__ == '__main__':
    solve()
