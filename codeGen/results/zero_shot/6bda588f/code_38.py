def min_function_value():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Initialize the minimum value of F to infinity
        min_f = float('inf')
        
        # Iterate over all possible x_i and y_i values
        for x_y in itertools.product(*[range(a_i+1) for a_i in a]):
            f = 0
            for i, (x, y) in enumerate(zip(x_y[:-1], x_y[1:])):
                f += x * y
            if f < min_f:
                min_f = f
        
        print(min_f)

min_function_value()
