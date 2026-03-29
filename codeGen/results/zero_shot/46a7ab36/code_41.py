def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        result = count_words(n, m)
        print(result)

if __name__ == "__main__":
    main()
