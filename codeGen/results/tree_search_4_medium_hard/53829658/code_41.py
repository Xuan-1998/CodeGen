import sys

def main():
    n = int(sys.stdin.readline().strip())
    roads = []
    for _ in range(n-1):
        si, ti = map(int, sys.stdin.readline().strip().split())
        roads.append((si, ti))
        
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    dp[0][0] = 0
    
    for p in range(1, n+1):
        for i in range(1, n+1):
            if i == 1:
                continue
            for j, t in roads:
                if t == i and j != i:
                    dp[i][p] = min(dp[i][p], dp[j][p-1]+1)
    
    min_edges_to_invert = float('inf')
    capital_cities = []
    p = n+1
    for i in range(1, n+1):
        if dp[i][p-1] < min_edges_to_invert:
            min_edges_to_invert = dp[i][p-1]
            capital_cities = [i]
        elif dp[i][p-1] == min_edges_to_invert:
            capital_cities.append(i)
    
    print(min_edges_to_invert, *capital_cities)

if __name__ == "__main__":
    main()
