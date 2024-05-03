===BEGIN CODE===
def prob_correct_numbering(tickets):
    memo = {}

    def recursive_prob(state, remaining_tickets):
        if (state, len(remaining_tickets)) in memo:
            return memo[(state, len(remaining_tickets))]
        
        if not remaining_tickets:
            return 1
        elif len(set(remaining_tickets[0])) == 1: 
            # If all tickets have the same number, return 0
            return 0
        
        prob = recursive_prob(set(), remaining_tickets[1:])
        # Calculate probability of correct numbering for this ticket
        # For simplicity, assume it's the product of probabilities of distinct numbers
        prob *= len(state) / (len(state) + 2)
        
        memo[(state, len(remaining_tickets))] = prob
        
        return prob

    result = []
    while tickets:
        n, p1, p2 = map(int, input().split())
        state = set()
        for _ in range(n):
            state.add(p1 if random.random() < p1 / (p1 + p2) else p2)
        
        result.append(recursive_prob(state, tickets[1:]))
    
    print("\n".join(map(str, result)))
===END CODE===
