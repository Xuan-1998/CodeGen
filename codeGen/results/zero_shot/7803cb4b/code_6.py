def reduce_array(a):
    stack = []
    for num in a:
        if stack and stack[-1] == num:
            # Increment the last element in the stack
            stack[-1] += 1
            # If the stack has more than one element and the last two are equal, pop them
            while len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack[-1] += 1
        else:
            stack.append(num)
    return len(stack)

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    result = reduce_array(a)
    print(result)

if __name__ == "__main__":
    main()
