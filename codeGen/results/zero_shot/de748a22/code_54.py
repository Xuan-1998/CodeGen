def solve():
    n, q = map(int, input().split())
    signs = list(input())

    for _ in range(q):
        l, r = map(int, input().split())
        ones = sum(1 if sign == '+' else 0 for sign in signs[l:r+1])
        
        # Calculate the minimum number of elements that can be removed
        min_to_remove = abs(ones)
        print(min_to_remove)

if __name__ == "__main__":
    solve()
