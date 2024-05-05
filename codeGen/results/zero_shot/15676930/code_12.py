import sys

def solve(n):
    # Read input values from stdin
    a_values = [int(x) for x in sys.stdin.readline().split()]
    b_values = [int(x) for x in sys.stdin.readline().split()]
    c_values = [int(x) for x in sys.stdin.readline().split()]

    # Initialize the state space as an empty string
    states = ""

    # Compute the optimal order and maximum total joy
    max_joy = 0
    for i in range(n):
        if i == 0:
            if n == 1 or (n > 1 and a_values[0] > b_values[0]):
                states += "H"
            else:
                states += "F"
        elif i == n - 1:
            if n == 1 or (n > 1 and c_values[n-1] > b_values[n-2]):
                states += "F"
            else:
                states += "H"
        else:
            if a_values[i] + c_values[i-1] > b_values[i]:
                states += "H"
            else:
                states += "F"

        # Update the maximum total joy
        max_joy = max(max_joy, sum([a_values[j] if (states[j] == "H" and (j == 0 or states[j-1] == "H")) else b_values[j] if (states[j] == "H" and states[j-1] != "F") else c_values[j] for j in range(n)]))

    return max_joy

# Read the input value of n from stdin
n = int(sys.stdin.readline())

# Print the maximum possible total joy to stdout
print(solve(n))
