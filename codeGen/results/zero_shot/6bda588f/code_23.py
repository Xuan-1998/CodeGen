def min_value_of_f(n, s):
    # Initialize the minimum value of F to infinity
    min_f = float('inf')

    # Iterate over all possible values of x_i and y_i
    for x1 in range(s + 1):
        y1 = a1 - x1
        for x2 in range(s + 1):
            y2 = a2 - x2
            # Calculate the value of F for this combination
            f = (x1 * y2) + (y1 * x2)
            # Update the minimum value of F if necessary
            min_f = min(min_f, f)

    return min_f

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(min_value_of_f(n, s))
