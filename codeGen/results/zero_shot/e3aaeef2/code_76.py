def solve():
    t = int(input())  # read the number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # read the initial number and operations
        result = str(n)  # initialize the result as a string representation of n
        for _ in range(m):
            new_result = ""  # initialize the new result string
            for digit in result:
                if int(digit) % 10 == 9:  # handle carry-over from last operation
                    new_result += "0"
                else:
                    new_result += str((int(digit) + 1) % 10)
            result = new_result  # update the result string
        print(len(result) % (10**9 + 7))  # print the length of the resulting number modulo 10^9+7

if __name__ == "__main__":
    solve()
