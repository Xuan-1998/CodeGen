def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        num_str = str(n)
        length = len(num_str)
        carry = 0
        for i in range(len(num_str)):
            digit = int(num_str[i]) + 1 + carry
            if digit >= 10:
                carry = 1
                digit %= 10
            else:
                carry = 0
            num_str = str(digit) + num_str[:i]
        length += carry
        print(length % (10**9 + 7))

if __name__ == "__main__":
    solve()
