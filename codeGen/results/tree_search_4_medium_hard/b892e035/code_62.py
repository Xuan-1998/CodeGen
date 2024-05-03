import sys

def calculate_probability(n):
    memo = {}
    def recursive_calculate(i, p1, p2):
        key = (i, p1, p2)
        if key in memo:
            return memo[key]
        
        if i == n:
            # Base case: all tickets processed
            return 1.0 if len(set([t[1], t[2]])) == n else 0.0
        
        prev_num1 = ticket[i-1][1] if i > 0 else None
        unique_num2 = set([ticket[j][2] for j in range(i)]) & set([t[2] for t in ticket[:i]])
        
        # Case 1: first number matches, second number does not match any previous tickets' numbers
        p1_new = p1 * (ticket[i-1][0] if i > 0 else 1.0)
        p2_new = 0.0
        
        # Case 2: first number does not match the previous ticket's first number
        p1_new_alt = (1 - p1) if prev_num1 is None or prev_num1 != ticket[i-1][1] else p1
        p2_new_alt = (1 - p2) if unique_num2 == set([t[2] for t in ticket[:i]]) else p2
        
        prob1 = recursive_calculate(i+1, p1_new, p2_new)
        prob2 = recursive_calculate(i+1, p1_new_alt, p2_new_alt)
        
        memo[key] = max(prob1, prob2)
        return memo[key]
    
    ticket = []
    for _ in range(n):
        ticket.append([int(x) for x in sys.stdin.readline().split()])
    
    result = recursive_calculate(0, 1.0, 1.0)
    print(result)

calculate_probability(int(sys.stdin.readline()))
