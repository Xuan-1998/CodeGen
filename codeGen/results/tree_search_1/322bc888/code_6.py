def precompute_operations(s, n):
    operations = [0] * n
    count = 0
    
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
        operations[i] = count
    
    return operations

def main():
    # Read input
    n, m = map(int, input().split())
    s = input().strip()
    
    # Precompute the operations required for the entire string
    operations = precompute_operations(s, n)
    
    # Process each query
    for _ in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        # Calculate the cost for the substring [l, r]
        cost = operations[r] - operations[l]
        print(cost)

if __name__ == "__main__":
    main()
