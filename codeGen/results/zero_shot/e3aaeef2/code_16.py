import sys

def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        res = n  # initialize result with original value
        while m:
            new_val = 0
            digit_count = 0
            while res:  # iterate through each digit of the current value
                digit = res % 10
                new_val = (new_val * 10) + (digit + 1)
                digit_count += 1
                res //= 10
            m -= digit_count  # reduce operation count by the number of digits updated
            res = new_val
        print(len(str(res)) % (10**9 + 7))  # print length of final result modulo 10^9+7

if __name__ == "__main__":
    solve()
