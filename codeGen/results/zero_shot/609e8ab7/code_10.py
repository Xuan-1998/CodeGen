import sys

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        parents = list(map(int, input().split()))
        ranges = []
        for _ in range(n):
            l, r = map(int, input().split())
            ranges.append((l, r))
        
        operations = 0
        max_values = [r - l for l, r in ranges]
        for diff in sorted(max_values)[::-1]:
            if diff > 0:
                operations += diff
            else:
                break
        
        print(operations)

if __name__ == "__main__":
    solve()
