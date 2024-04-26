def combine_elements(arr):
    stack = []
    for elem in arr:
        if stack and stack[-1] == elem:
            stack.pop()
            elem += 1
        while stack and elem == stack[-1] + 1:
            stack.pop()
            elem += 1
        stack.append(elem)
    return len(stack)

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    result = combine_elements(a)
    print(result)

if __name__ == "__main__":
    main()
