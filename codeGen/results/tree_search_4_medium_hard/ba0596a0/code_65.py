def can_cross_stones(stones):
    for i in range(1, len(stones)):
        if stones[i] - stones[i-1] > k + 1:
            return False

    return True


# Example usage
k = int(input())  # Get the value of k from stdin
stones = list(map(int, input().split()))  # Read the positions of stones in ascending order
if can_cross_stones(stones):
    print("Yes")
else:
    print("No")

