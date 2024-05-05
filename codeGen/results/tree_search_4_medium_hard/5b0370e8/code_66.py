def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [0] * (1 << k)
        dp[-1] = 1  # Base case: all arrays with bitwise AND results exceeding 2**k - 1
        for i in range(1 << k):  # Iterate over each possible state s from 0 to 2**k - 1
            next_and_result = (i >> 1) & ((1 << k) - 1)  # Next bitwise AND result after flipping the current bit
            xor_result = i ^ (1 << k) - 1  # XOR result of all bits being flipped
            if xor_result < (1 << k) - 1:  # If XOR result is less than 2**k - 1, update dp[i]
                dp[i] = sum(dp[j] for j in range(next_and_result.bit_length() + 1))  # Count the number of arrays that satisfy the condition
            if i < (1 << k) - 1:  # If current state is not the last one, update dp[i ^ 2**(k-1)]
                dp[i ^ (1 << k) - 1] = sum(dp[j] for j in range(i.bit_length() + 1))  # Count the number of arrays that satisfy the condition
        print(dp[0] % (10**9 + 7))  # Print the final answer

solve()
