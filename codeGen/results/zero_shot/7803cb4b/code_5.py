def min_length_array(a):
    stack = []
    for element in a:
        while stack and stack[-1] == element:
            stack.pop()
            element += 1
        stack.append(element)
    return len(stack)

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    result = min_length_array(a)
    print(result)

if __name__ == "__main__":
    main()
