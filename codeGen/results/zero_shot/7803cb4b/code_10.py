def simulate_operations(arr):
    stack = []
    for num in arr:
        if stack and stack[-1] == num:
            # Increment the last element in the stack
            stack[-1] += 1
            # Check if this increment leads to a new combination
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack[-2] += 1
                stack.pop()
        else:
            stack.append(num)
    return len(stack)

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    result = simulate_operations(arr)
    print(result)

if __name__ == "__main__":
    main()
