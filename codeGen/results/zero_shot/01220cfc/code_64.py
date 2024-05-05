# Test case 1: Reaches last index
jumps = [2, 3, 1, 1, 4]
print(can_reach_last_index(jumps))  # Should print True

# Test case 2: Doesn't reach last index
jumps = [1, 2, 0, 1, 4]
print(can_reach_last_index(jumps))  # Should print False

# Test case 3: Reaches last index with a single jump
jumps = [5]
print(can_reach_last_index(jumps))  # Should print True
