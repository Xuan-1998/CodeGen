import sys

def main():
    n = int(sys.stdin.readline())
    parents = [0] * (n + 1)
    
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        parents[b] = a
    
    capital = 0
    while capital:
        capital = parents[capital]
    
    min_reversals = n - 2
    for i in range(1, n + 1):
        if parents[i] != 0:
            min_reversals -= 1
    
    print(min_reversals)
    capital_cities = [i for i in range(1, n + 1) if parents[i] == 0]
    for city in sorted(capital_cities):
        print(city, end=' ')
    print()

if __name__ == "__main__":
    main()
