import math

def solve():
    T = int(input())
    
    for _ in range(T):
        n = int(input())
        
        # Initialize the state and mask
        p1, p2 = map(float, input().split())
        p = 1.0
        
        # Iterate through each ticket
        mask = 0
        for i in range(n):
            first, second = map(int, input().split())
            
            # Transition function: update the probabilities based on the two possible numbers and their corresponding probabilities
            if (mask & (1 << (first - 1))) == 0:
                p *= p1 / (1 - p1)
            if (mask & (1 << (second - 1))) == 0:
                p *= p2 / (1 - p2)
            
            # Update the state and mask
            mask |= 1 << (first - 1) | 1 << (second - 1)
        
        print(math.floor(p + 0.000001))

if __name__ == "__main__":
    solve()
