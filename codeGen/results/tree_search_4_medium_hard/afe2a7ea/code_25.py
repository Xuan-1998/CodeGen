def prob_towers(n):
    MOD = 998244353

    dp = [0] * (1 << n)  # Initialize a list to store probabilities for each state
    dp[0] = 1  # Base case: all towers unused has probability 1/2^n

    for i in range(1 << n):  # Iterate over all possible states
        for j in range(n):
            if (i & (1 << j)) != 0:  # If the jth bit is set (tower used)
                next_state = i ^ (1 << j)  # Calculate the next state by flipping the jth bit
                dp[i] = (dp[i] * (2 ** n)) % MOD  # Update the probability for the current state

    return sum(dp) % MOD  # Return the total probability, modulo the prime number

# Read input from stdin and print the result to stdout
n = int(input())
print(prob_towers(n))
