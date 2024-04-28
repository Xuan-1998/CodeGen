def orthus_hydra(heads, tails):
    # Initialize the counts for Orthus and Hydra
    o_heads = 0
    h_heads = 0

    # Greedily assign heads and tails based on the parity of head count
    while heads > 0:
        if heads % 2 == 1:  # Odd number of heads, add to Orthus
            o_heads += 1
            heads -= 1
        else:  # Even number of heads, add to Hydra
            h_heads += 1
            heads -= 1

    # Adjust the tail count to match the head count
    tails = max(0, tails - (o_heads + h_heads))

    # Return the counts for Orthus and Hydra
    return [o_heads, h_heads]

# Read input from stdin
heads, tails = map(int, input().split())

# Call the function with the input values
result = orthus_hydra(heads, tails)

# Print the result to stdout
print(result)
