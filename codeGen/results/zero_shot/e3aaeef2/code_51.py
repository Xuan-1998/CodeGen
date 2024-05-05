def simulate_operation(n):
    n_str = str(n)
    new_n = ''
    for d in n_str:
        new_n += str(int(d) + 1)
    return int(new_n)

def calculate_resulting_length(n, m):
    new_n = n
    for _ in range(m):
        new_n = simulate_operation(new_n)
    return len(str(new_n)) % (10**9 + 7)

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        result = calculate_resulting_length(n, m)
        print(result)

if __name__ == "__main__":
    main()
