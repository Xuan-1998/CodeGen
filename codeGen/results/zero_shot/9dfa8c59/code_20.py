def main():
    n_max, k_perms = map(int, input().split())
    result = solve(n_max, k_perms)
    print(*result)

if __name__ == "__main__":
    main()
