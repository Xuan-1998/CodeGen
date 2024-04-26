def main():
    n = int(input())
    recruits = list(map(int, input().split()))
    available_officers = 0
    untreated_crimes = 0

    for recruit in recruits:
        available_officers += recruit
        while available_officers >= 1:
            if available_officers >= 1:
                available_officers -= 1
            else:
                break
        if available_officers < 0:
            untreated_crimes += -available_officers
            break

    print(untreated_crimes)

if __name__ == "__main__":
    main()
