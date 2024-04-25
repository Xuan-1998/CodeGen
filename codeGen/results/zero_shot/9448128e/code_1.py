MOD = 998244353

def read_input():
    N = int(input().strip())
    sets = []
    for _ in range(N):
        line = list(map(int, input().split()))
        sets.append(set(line[1:]))  # Convert list to set to remove duplicates
    return N, sets

def count_valid_sequences(N, sets):
    if N == 1:
        return len(sets[0])  # If there's only one set, all elements are valid sequences
    
    # Initialize count with the number of elements in the first set
    count = len(sets[0])
    
    for i in range(1, N):
        current_set_size = len(sets[i])
        
        # If the current and previous sets have the same single element, there are no valid sequences
        if current_set_size == 1 and sets[i] == sets[i-1]:
            return 0
        
        # Calculate the number of ways to pick a number from the current set
        if current_set_size > 1:
            # We can pick any number different from the last picked number
            count *= (current_set_size - 1)
        count %= MOD
    
    return count

def main():
    N, sets = read_input()
    result = count_valid_sequences(N, sets)
    print(result)

if __name__ == "__main__":
    main()
