def main():
    n = int(input())
    
    # Check if n is within the allowed range (1 <= n <= 2 * 10^5)
    if not 1 <= n <= 2 * 10**5:
        print("Invalid input")
        return

    dp = [0] * (1 << n)  # Initialize a list of size 2^n to store the probabilities
    dp[0] = 1  # Base case: all zeros has a probability of 1/2^n

    for state in range(1 << n):  # Iterate over all possible states
        next_state = 0
        used_towers = 0  # Count the number of used towers in the current state
        for i in range(n):
            if (state >> i) & 1:  # Check if the ith tower is used
                used_towers += 1
                next_state |= 1 << i  # Add the ith tower to the next state

        dp[state] = dp[next_state] * (2 ** (n - used_towers))  # Calculate the probability using the transition relationship

    print(dp[-1])  # The final answer is stored in the last element of the list, which represents all ones

main()
