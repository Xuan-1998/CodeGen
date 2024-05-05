def main():
    n, q = map(int, input().split())
    arr = list(input())

    prefix_sum, suffix_sum = preprocess(arr)

    for _ in range(q):
        l, r = map(int, input().split())
        print(query(prefix_sum, suffix_sum, l - 1, r - 1))

if __name__ == "__main__":
    main()
