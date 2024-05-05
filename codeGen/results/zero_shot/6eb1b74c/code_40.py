if __name__ == "__main__":
    t = input()  # read the text from stdin
    n = int(input())  # read the number of strings
    s = [input() for _ in range(n)]  # read the set of strings

    m = min_steps(t, s)

    if m == -1:
        print(-1)
    else:
        print(m)
        for j in range(m):
            w_j = j + 1  # string index
            p_j = last_index - len(s[w_j-1]) + 1  # starting position of the used string
            print(f"{w_j} {p_j}")
