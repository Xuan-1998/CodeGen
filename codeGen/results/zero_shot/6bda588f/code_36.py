def min_function_value():
    t = int(input())  # Read the number of test cases
    for _ in range(t):
        n, s = map(int, input().split())  # Read the number of integers and the value 's'
        a = list(map(int, input().split()))  # Read the sequence of integers

        # Calculate the minimum possible value of F
        min_value = float('inf')
        for x in range(s + 1):
            y = s - x
            current_value = sum([x * (a[i] - y) for i in range(n)])
            if current_value < min_value:
                min_value = current_value

        print(min_value)

min_function_value()
