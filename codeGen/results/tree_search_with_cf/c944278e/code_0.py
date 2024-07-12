python
def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    s = data[1]
    
    # Initial set of possible values
    possible_values = set(range(1, 2**n + 1))
    
    for bit in s:
        new_possible_values = set()
        values_list = sorted(possible_values)
        
        if bit == '0':
            # Keep the smaller value of each pair
            for i in range(0, len(values_list), 2):
                new_possible_values.add(min(values_list[i], values_list[i + 1]))
        else:
            # Keep the larger value of each pair
            for i in range(0, len(values_list), 2):
                new_possible_values.add(max(values_list[i], values_list[i + 1]))
        
        possible_values = new_possible_values
    
    # Convert the set to a sorted list
    result = sorted(possible_values)
    
    # Print the result
    print(" ".join(map(str, result)))


