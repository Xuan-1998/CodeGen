def main():
    n = int(input())
    p = list(map(int, input().split()))
    pairs = generate_pairs(n)
    if is_permutation_equal_to_merge(pairs):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
