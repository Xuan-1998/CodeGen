def read_input():
    n = int(input())
    x = list(map(int, input().split()))
    d = list(map(int, input().split()))
    return n, x, d

def simulate_collapse(n, x, d):
    loads = [x[i+1] - x[i] for i in range(n+1)]
    for i in range(n):
        if loads[i] > d[i]:
            # Point i collapses, redistribute the load to neighbors
            if i > 0:
                loads[i-1] += loads[i] // 2
            if i < n-1:
                loads[i+1] += (loads[i] + 1) // 2
            loads[i] = 0
    return loads

def find_min_durability(n, loads):
    # The minimum durability needed is the maximum load on any remaining point
    return max(loads)

def main():
    n, x, d = read_input()
    loads = simulate_collapse(n, x, d)
    min_durability = find_min_durability(n, loads)
    print(min_durability)

if __name__ == "__main__":
    main()
