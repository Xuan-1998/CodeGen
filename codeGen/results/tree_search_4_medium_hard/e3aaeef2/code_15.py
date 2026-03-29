def solve():
    t = int(input())
    memo = {}
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        # Initialize the state with the initial length and value of n
        state = (n.bit_length(), list(map(int, str(n))))
        
        # Apply the operations to get the final length of n
        result = apply_operations(state, m)
        
        print(result[0] % 1000000007)

def apply_operations(state, m):
    if state in memo:
        return memo[state]
    
    if state[0] == 1:  # Base case: single digit number
        return state
    
    result = None
    
    for i, d in enumerate(state[1]):
        # Apply the operation to each digit and update the state
        new_state = (state[0], list(map(lambda x: str((int(x) + 1) % 10), state[1])))
        
        if len(new_state[1]) == 1:
            result = new_state
            break
        
        # Update the memoization dictionary with the result for the current state
        memo[new_state] = apply_operations(new_state, m - 1)
    
    return result

solve()
