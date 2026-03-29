def can_cross_stones(stones):
    start = 0
    for end in range(1, len(stones)):
        while stones[end] - stones[start] > end - start:
            start += min(end - start + 2, stones[end] - stones[start])
    return start == len(stones) - 1

# Example usage:
stones = [0, 3, 5, 10, 15]
print(can_cross_stones(stones))  # Output: True
