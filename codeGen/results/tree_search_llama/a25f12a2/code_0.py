def count_creatures(heads, tails):
    orthus_heads = 2
    hydra_heads = 1
    
    # Calculate the maximum possible number of Orthus creatures
    max_orthus = heads // orthus_heads

    # If there are not enough heads for all Orthus, we can't have any Hydra
    if heads < max_orthus * orthus_heads:
        return ["No solutions"]

    # Calculate the remaining heads after accounting for all Orthus
    remaining_heads = heads - max_orthus * orthus_heads

    # Calculate the maximum possible number of Hydra creatures
    max_hydra = remaining_heads // hydra_heads
    
    # Return the counts as a list
    return [max_orthus, max_hydra]
