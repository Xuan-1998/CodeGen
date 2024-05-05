# Read input
T = int(input())

for _ in range(T):
    M, X = map(int, input().split())
    
    # Initialize the winners array with zeros
    winners = [0] * (X + 1)
    
    # Iterate over each number of players from 1 to X
    for i in range(1, X + 1):
        # Calculate the position where the coin will stop
        pos = (i - 1) % i
        
        # Update the winner index
        winners[i] = pos
        
        # Print the winner index
        print(winners[i])
