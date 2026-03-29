def maxBitwiseOR(n, s):
    dp = [0] * n  # Initialize dynamic programming array with zeros
    prev_or = 0  # Previous bitwise OR value

    for i in range(n):  # Iterate over the binary string from left to right
        prev_or |= int(s[i])  # Update previous bitwise OR value by extending it with either 0 or 1, whichever gives a larger bitwise OR value
        dp[i] = max(dp[i-1] if i > 0 else 0, prev_or)  # Calculate the maximum bitwise OR value for all substrings ending at index i

    return bin(max(dp))[2:]  # Return the maximum bitwise OR value in binary representation without leading zeroes

n = int(input())  # Read n from standard input
s = input()  # Read the binary string s of length n from standard input

print(maxBitwiseOR(n, s))  # Output the maximum possible value in binary representation without leading zeroes
