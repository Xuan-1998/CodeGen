python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_permutations(num):
    """Count the permutations of a number"""
    num_str = str(num)
    num_permutations = 1
    for digit in set(num_str):
        num_permutations *= len(str(int(digit)))
    return num_permutations

def main():
    n_max, k_perms = map(int, input().split())
    
    count = 0
    smallest = float('inf')
    largest = -float('inf')
    
    for i in range(2, n_max):
        if is_prime(i) and count_permutations(i) == k_perms:
            count += 1
            smallest = min(smallest, i)
            largest = max(largest, i)

    print([count, smallest, largest])

if __name__ == "__main__":
    main()
