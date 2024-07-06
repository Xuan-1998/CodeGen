def calculate_probability():
    T = int(input())  # Number of test cases
    for _ in range(T):
        n = int(input())  # Number of tickets
        probabilities = []
        numbers = []
        for _ in range(n):
            p, a, b = map(int, input().split())
            probabilities.append(p)
            numbers.append((a, b))
        
        # Calculate the probability of correct numbering
        # Here we'll use the formula for the probability of k distinct elements out of n:
        # (n! / (k! * (n-k)!)) * p^k * (1-p)^(n-k)
        # We'll iterate through all possible combinations and calculate the probability
        total_probability = 0
        for r in range(n):
            # Calculate the numerator
            numerator = math.factorial(n) // (math.factorial(r) * math.factorial(n-r))
            
            # Calculate the denominator
            denominator = 1
            for i in range(n):
                if i < r:
                    denominator *= probabilities[i]
                else:
                    denominator *= 1 - probabilities[i]
            
            total_probability += numerator * (probabilities[r-1] ** r) * denominator
        
        print(round(total_probability, 6))  # Print the result

calculate_probability()
