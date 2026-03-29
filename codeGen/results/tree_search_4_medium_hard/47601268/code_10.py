import sys

def main():
    n = int(sys.stdin.readline().strip())

    dp = [False for _ in range(n + 1)]
    dp[0] = True

    for i in range(1, n + 1):
        binary_i = bin(i)[2:]
        consecutive_ones = False
        prev_bit_was_one = False

        for bit in binary_i:
            if bit == '0':
                consecutive_ones = False
            elif bit == '1' and not prev_bit_was_one:
                consecutive_ones = True
            prev_bit_was_one = (bit == '1')

        dp[i] = not consecutive_ones

    count = sum(1 for i in range(n + 1) if dp[i])
    print(count)

if __name__ == "__main__":
    main()
