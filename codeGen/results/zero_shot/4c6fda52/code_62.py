def main():
    while True:
        n, k = map(int, input().split())
        if not n:  # Check if we've reached the end of queries
            break

        s = input()

        changes = count_changes(s, k)
        print(changes)

if __name__ == "__main__":
    main()
