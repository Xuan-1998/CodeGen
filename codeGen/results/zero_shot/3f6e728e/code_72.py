def solve():
    t = int(input())
    for _ in range(t):
        n, m, c = map(int, input().split())
        u_rad = list(map(int, input().split()))
        l_rad = list(map(int, input().split()))
        
        # Calculate the counts of the radii
        # ...

        # Print the result
        print(*counts, sep=' ')
