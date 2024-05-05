# Define a function to perform one operation: replace each digit with d + 1
def next_state(length, value):
    new_value = ""
    for d in str(value):
        new_value += str(int(d) + 1)
    return (len(new_value), int(new_value))

# Initialize an empty dictionary for memoization
memo = {}

def solve(n, m):
    # Base case: if the initial number has less than or equal to 1 digit, return it as the final result
    if n <= 9:
        return n

    # Perform operations and store intermediate results in the memo dictionary
    current_state = (len(str(n)), n)
    for _ in range(m):
        if current_state not in memo:
            memo[current_state] = next_state(*current_state)
        current_state = memo[current_state]

    # Return the final result as the length of the resulting number modulo 10^9+7
    return len(str(current_state[1])) % (10**9 + 7)

# Read input from stdin and print the answer to stdout
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(solve(n, m))
