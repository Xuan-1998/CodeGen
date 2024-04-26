def calculate_cost(s, l, r):
    cost = 0
    for i in range(l, r):
        if s[i] == s[i - 1]:  # Adjacent identical letters
            cost += 1
        elif i > l and s[i] == s[i - 2]:  # Pattern like "aba"
            cost += 1
    return cost

def main():
    n, m = map(int, input().split())  # Read n and m
    s = input()  # Read the string s
    for _ in range(m):
        l, r = map(int, input().split())  # Read the l_i and r_i for each query
        l -= 1  # Convert to 0-based index
        r -= 1  # Convert to 0-based index
        print(calculate_cost(s, l, r))

if __name__ == "__main__":
    main()
