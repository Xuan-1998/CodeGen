def solve():
    T = int(input())
    for _ in range(T):
        N, M, C = map(int, input().split())
        U = list(map(int, input().split()))
        L = list(map(int, input().split()))

        # Sort the upper and lower hemispheres by their radii
        U.sort()
        L.sort()

        # Initialize the counts of spheres for each possible X-sequence
        count = [0] * (C + 1)

        # Count the number of spheres that can be used to build each possible X-sequence
        for i in range(C + 1):
            count[i] = sum(1 for j in U if j >= i) + sum(1 for k in L if k <= i)

        # Calculate the number of ways to build each i-sequence
        ans = [0] * (C + 1)
        for i in range(C, -1, -1):
            ans[i] = count[i] * ((count[i] + 1) // 2) % (10**9 + 7)

        print(*ans, sep=' ')

if __name__ == '__main__':
    solve()
