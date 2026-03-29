import sys

def get_min_inverted_roads(n, roads):
    memo = {(1, 0): 0}
    for i in range(2, n+1):
        dp_i = float('inf')
        for j in range(1, i):
            if (j, i) in memo and (i, 0) in memo:
                dp_i = min(dp_i, memo[(j, i)] + memo[(i, 0)] + 1)
        memo[(i, 0)] = dp_i
    return memo[(n, 0)]

def main():
    n = int(sys.stdin.readline())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().split())
        roads.append((si, ti))
    
    min_inverted_roads = get_min_inverted_roads(n, roads)
    print(min_inverted_roads)

if __name__ == "__main__":
    main()
