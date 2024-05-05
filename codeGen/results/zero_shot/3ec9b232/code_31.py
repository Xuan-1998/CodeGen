import sys

def count_ways(M):
    n = len(M)
    MOD = 10**9 + 7
    
    # Initialize a dictionary to store the counts of each possible value in M
    val_count = {}
    for m in M:
        if m not in val_count:
            val_count[m] = 0
        val_count[m] += 1
    
    # Calculate the total number of ways to create V
    total_ways = 1
    for count in val_count.values():
        total_ways *= (count + 1)  # Add 1 because we can have empty arrays
    total_ways %= MOD
    
    return total_ways

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    M = list(map(int, sys.stdin.readline().split()))
    
    print(count_ways(M))
