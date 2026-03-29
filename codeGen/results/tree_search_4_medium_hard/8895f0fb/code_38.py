from collections import defaultdict

def read_input():
    T = int(input())
    for _ in range(T):
        N = int(input())
        yield N

def get_expected_carry(n):
    dp = defaultdict(float)
    def dfs(n, carry):
        if n == 0:
            return 1.0
        if (n, carry) in dp:
            return dp[(n, carry)]
        
        total = 0
        for i in range(10):
            total += dfs(n-1, (i + carry) >= 10)
        dp[(n, carry)] = total / 10.0
        return dp[(n, carry)]

    expected_carry = 0
    for _ in range(2**N):
        n = N - 1
        carry = 0
        num_str = ''
        while n >= 0:
            bit = (_ >> (n * 4)) & 3
            if bit == 1:
                num_str += '9'
                carry = 1
            else:
                num_str += '0' if carry else str(bit)
                carry = 0
            n -= 1
        expected_carry += dfs(N, carry)

    return expected_carry / (2**N)


if __name__ == "__main__":
    for N in read_input():
        print(get_expected_carry(N))
