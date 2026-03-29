def get_probability(n):
    # Step 1: Initialize the result as the total number of ways to choose signal powers
    total_ways = 2 ** n
    
    # Step 2: Calculate the number of ways that don't meet the constraints
    wrong_ways = 0
    for i in range(2 ** n):
        signal_powers = [i & (1 << j) for j in range(n)]
        if not all(signal_powers[i] > 0 for i in range(1, n + 1)):
            wrong_ways += 1
    
    # Step 3: Calculate the probability by subtracting the number of wrong ways from the total number of ways
    probability = total_ways - wrong_ways
    
    return probability % (998244353)
