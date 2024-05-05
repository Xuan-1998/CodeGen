def generate_output(min_steps):
    if min_steps == -1:
        print(-1)
    else:
        print(min_steps)
        for i in range(min_steps):
            start, end = next(iter(used_strings))
            print(f"{w_i} {p_i}")
