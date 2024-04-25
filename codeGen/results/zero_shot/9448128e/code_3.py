MOD = 998244353

def read_input():
    N = int(input())
    sets = []
    for _ in range(N):
        _, *set_elements = map(int, input().split())
        sets.append(set_elements)
    return N, sets

def count_valid_sequences(N, sets):
    # Initialize the count with the number of elements in the first set
    count = len(sets[0])
    
    for i in range(1, N):
        current_set = sets[i]
        previous_set = sets[i - 1]
        
        # Count how many elements in the current set are different from the last element of the previous set
        different_count = len(current_set) - (previous_set[-1] in current_set)
        
        # Multiply the count of sequences so far with the number of different options for the current set
        count = (count * different_count) % MOD
    
    return count

def main():
    N, sets = read_input()
    result = count_valid_sequences(N, sets)
    print(result)

if __name__ == "__main__":
    main()
