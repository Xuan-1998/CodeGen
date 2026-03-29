def solve():
    t = int(input())  # number of test cases
    for _ in range(t):
        n, m = map(int, input().split())
        result = str(n)  # initialize result with initial value of n
        for _ in range(m):
            temp = ""  # temporary string to store new digits
            for digit in result:
                if int(digit) % 10 == 4:  # special case for digit 4
                    temp += "2"
                elif int(digit) % 10 >= 5:  # for digits 5-9, increment by 1
                    temp += str((int(digit) + 1) % 10)
                else:  # for digits 0-3, increment by 1 and wrap around if necessary
                    temp += str((int(digit) + 1) % 10 if int(digit) < 3 else "1")
            result = temp  # update result with new value after each operation
        print(len(result))  # print the length of the resulting integer modulo 10^9+7

solve()
