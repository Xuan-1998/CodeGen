def main():
    n_max = int(input())
    k_perms = int(input())
    solutions = find_solutions(n_max, k_perms)
    if len(solutions) == 3:
        print(f"{solutions[0]} {min(solutions)} {max(solutions)}")
    else:
        print([0, 0, 0])

if __name__ == "__main__":
    main()
