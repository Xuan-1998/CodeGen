def main():
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        arr = list(map(lambda x: 1 if x == "+" else -1, input()))
        prefix_sum = preprocess_array(arr)
        for _ in range(q):
            l, r = map(int, input().split())
            print(handle_query(prefix_sum, l - 1, r))

if __name__ == "__main__":
    main()
