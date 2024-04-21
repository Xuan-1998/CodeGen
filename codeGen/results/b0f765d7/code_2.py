import sys

def vitamin_mask(vitamins):
    mask = 0
    if 'A' in vitamins:
        mask |= 1
    if 'B' in vitamins:
        mask |= 2
    if 'C' in vitamins:
        mask |= 4
    return mask

def main():
    # Read the number of juices
    n = int(input().strip())
    
    # Initialize the dp array with infinity values except dp[0] which should be 0
    dp = [float('inf')] * 8
    dp[0] = 0
    
    # Process each juice
    for _ in range(n):
        cost, vitamins = input().strip().split()
        cost = int(cost)
        mask = vitamin_mask(vitamins)
        
        # Update the dp array
        for prev_mask in range(8):
            new_mask = prev_mask | mask
            dp[new_mask] = min(dp[new_mask], dp[prev_mask] + cost)
    
    # The answer is dp[7] if it's not infinity, otherwise it's impossible to obtain all vitamins
    if dp[7] < float('inf'):
        print(dp[7])
    else:
        print(-1)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
