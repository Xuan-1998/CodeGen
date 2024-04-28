# Read input
K = int(input())
N = int(input())
arr = [[int(x) for x in line.split()] for line in stdin.readlines()]

# Call the function
result = count_paths(K, N, arr)
print(result)
