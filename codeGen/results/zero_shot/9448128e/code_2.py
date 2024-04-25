MOD = 998244353

# Function to read the input
def read_input():
    N = int(input().strip())
    sets = [list(map(int, input().strip().split()))[1:] for _ in range(N)]
    return N, sets

# Function to calculate the number of ways to choose elements from sets
def calculate_ways(N, sets):
    total_ways = len(sets[0])  # All elements can be chosen from the first set
    for i in range(1, N):
        prev_set = sets[i - 1]
        current_set = sets[i]
        prev_set_count = len(prev_set)
        current_set_count = len(current_set)
        common_elements_count = len(set(prev_set) & set(current_set))
        
        # Calculate ways excluding the previous element
        ways_excluding_prev = (total_ways * (current_set_count - common_elements_count)) % MOD
        
        # Calculate ways including the previous element (if there are common elements)
        ways_including_prev = (total_ways * common_elements_count) % MOD
        
        # Update total ways for the current set
        total_ways = (ways_excluding_prev + ways_including_prev) % MOD
    
    return total_ways

# Main function to execute the program
def main():
    N, sets = read_input()
    result = calculate_ways(N, sets)
    print(result)

if __name__ == "__main__":
    main()
