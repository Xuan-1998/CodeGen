from itertools import combinations

def read_input():
    n = int(input().strip())
    juices = [tuple(input().strip().split()) for _ in range(n)]
    return n, juices

def preprocess(juices):
    # Convert prices to integers and vitamin strings to sets
    return [(int(price), set(vitamins)) for price, vitamins in juices]

def find_min_price(juices):
    all_vitamins = {'A', 'B', 'C'}
    min_price = float('inf')
    found = False

    # Check all juices and combinations of two and three juices
    for k in range(1, 4):
        for combo in combinations(juices, k):
            combo_price = sum(juice[0] for juice in combo)
            vitamins_combined = set().union(*(juice[1] for juice in combo))
            if vitamins_combined == all_vitamins:
                found = True
                min_price = min(min_price, combo_price)

    return min_price if found else -1

def main():
    n, juices = read_input()
    juices = preprocess(juices)
    min_price = find_min_price(juices)
    print(min_price)

if __name__ == "__main__":
    main()
