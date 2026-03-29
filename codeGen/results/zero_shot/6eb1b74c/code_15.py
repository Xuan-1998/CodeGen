if __name__ == "__main__":
    t, n, strings = read_input()
    min_steps_required = min_steps(t, strings)
    if min_steps_required == -1:
        print(-1)
    else:
        print(min_steps_required)
        print_solution(min_steps_required, strings)
