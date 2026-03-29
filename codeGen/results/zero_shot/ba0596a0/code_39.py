def can_cross(stones):
    k = 1
    i = j = stones[0]
    
    while i < stones[-1]:
        max_jump = min(j - i, k + 1)
        if i + max_jump <= stones[j]:
            i += max_jump
        else:
            return False
        k = max_jump
        j += 1
    
    return True

# Example usage:
stones = [0, 2, 5, 10, 13]
print(can_cross(stones))  # Output: True
