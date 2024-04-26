def read_input():
    n, m = map(int, input().split())
    universe = [input().strip() for _ in range(n)]
    return n, m, universe

def preprocess_grid(n, m, universe):
    # Implement preprocessing here
    pass

def calculate_lifespan(n, m, universe):
    # Implement lifespan calculation here
    pass

def main():
    n, m, universe = read_input()
    preprocess_grid(n, m, universe)
    lifespan = calculate_lifespan(n, m, universe)
    print("{:.6f}".format(lifespan))

if __name__ == "__main__":
    main()
