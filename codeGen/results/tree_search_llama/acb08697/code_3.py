def min_stones_after_operations():
    n = int(input())
    operations = input()
    
    stack = [0]  # Initialize with 0 stones
    min_stones = float('inf')  # Initialize minimum stones
    
    for op in operations:
        if op == "+":
            stack.append(1)  # Add one stone to the pile
        else:  # op is "-"
            if stack[-1] > 0:  # Remove one stone from the pile if it's not empty
                stack.pop()
        
        min_stones = min(min_stones, len(stack))  # Update minimum stones
    
    print(min_stones)

min_stones_after_operations()
