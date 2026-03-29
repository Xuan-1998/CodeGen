def main():
    n = int(input())
    w = [int(input()) for _ in range(n)]
    roads = []
    for _ in range(n-1):
        u, v, c = map(int, input().split())
        roads.append((u, v, c))
    
    start_city = 0
    max_gas = dfs(start_city, w[start_city], 0)
    print(max_gas)
