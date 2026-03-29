def solve():
    t = int(input())  # read number of test cases

    MOD = 10**9 + 7
    for _ in range(t):
        n, k = map(int, input().split())  # read n and k
        arr = list(map(int, input().split()))  # read array elements

        # Initialize count to 0
        count = 0

        # Iterate over all possible combinations of bits (0s and 1s)
        for mask in range(2**k):
            # Calculate bitwise AND operation for the current combination
            and_mask = mask & ((mask << 1) - 1)

            # Calculate bitwise XOR operation for the current combination
            xor_mask = mask ^ ((mask << 1) - 1)

            # Check if the condition is satisfied (bitwise AND >= bitwise XOR)
            if bin(and_mask).count('1') >= bin(xor_mask).count('1'):
                count += 1

        print(count % MOD)  # print the count modulo 10^9+7

if __name__ == "__main__":
    solve()
