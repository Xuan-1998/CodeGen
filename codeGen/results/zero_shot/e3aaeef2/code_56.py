def main():
    t = int(input())  # read number of test cases
    for _ in range(t):
        n, m = map(int, input().split())  # read n and m
        result = apply_m_operations(n, m)
        print(find_length(result) % (10**9 + 7))  # print the answer

if __name__ == "__main__":
    main()
