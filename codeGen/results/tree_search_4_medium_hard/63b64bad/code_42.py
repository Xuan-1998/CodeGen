# Read input from stdin
n = int(input())
sequence = list(map(int, input().split()))

# Initialize a dictionary to store calculated values for memoization
memo = {(1, 0): sequence[1]}

def simulate_program(x, y):
    while x <= n:
        new_x = x + sequence[x]
        new_y = y + sequence[x] - (x % sequence[x])
        if new_x > n or new_x < 1:
            return -1
        if (new_x, new_y) in memo:
            return new_y
        x, y = new_x, new_y
    return y

# Read number of test cases from stdin
t = int(input())

for _ in range(t):
    # Initialize x and y for each test case
    x, y = 1, 0
    
    while True:
        if (x, y) in memo:
            print(memo[(x, y)])
            break
        else:
            new_x = x + sequence[x]
            new_y = y + sequence[x] - (x % sequence[x])
            if new_x > n or new_x < 1:
                print(-1)
                break
            x, y = new_x, new_y
