def can_cross_stones(stone_positions):
    for i in range(1, len(stone_positions)):
        if abs(stone_positions[i] - stone_positions[i-1]) not in [k-1, k, k+1]:
            return False
    return True

stone_positions = list(map(int, input().split()))
if can_cross_stones(stone_positions):
    print("True")
else:
    print("False")
