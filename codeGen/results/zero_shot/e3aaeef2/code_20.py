def successor_map():
    return {str(i): str(i+1) for i in range(10)}

successor_map = successor_map()

def apply_operations(initial_state, m):
    for _ in range(m):
        new_state = ""
        for char in initial_state:
            if char.isdigit():
                new_state += successor_map()[char]
            else:
                new_state += char
        initial_state = new_state
    return initial_state

def calculate_length(resulting_state):
    return len(resulting_state)

t = int(input())  # read the number of test cases
for _ in range(t):
    n, m = map(int, input().split())  # read the initial number and operations
    resulting_state = apply_operations(str(n), m)
    print(calculate_length(resulting_state) % (10**9 + 7))  # output the length modulo 10^9+7
