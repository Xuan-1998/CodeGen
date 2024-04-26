def perform_operations(arr):
    stack = []
    for num in arr:
        # If the stack is not empty and the top of the stack is equal to the current number
        if stack and stack[-1] == num:
            # Pop the top of the stack and increase the current number by 1
            stack.pop()
            num += 1
            # If the stack becomes empty or the new number is not equal to the new top of the stack, push it
            if not stack or stack[-1] != num:
                stack.append(num)
        else:
            # If the current number is not equal to the top of the stack, push it
            stack.append(num)
    return len(stack)

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = perform_operations(arr)
    print(result)

if __name__ == "__main__":
    main()
