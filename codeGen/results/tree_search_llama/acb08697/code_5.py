def min_stones(n, operations):
    stones = 1  # Initialize the pile with one stone
    for op in operations:
        if op == "+":
            stones += 1
        else:  # If the operation is "-",
            stones = max(0, stones - 1)  # Remove a stone if possible
    return stones

n = int(input())
operations = input()
print(min_stones(n, operations))
