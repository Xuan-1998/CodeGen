if last_used_index == -1:
    print(-1)
else:
    print(min_steps)

    for start_index, _ in occurrences.values():
        if start_index > last_used_index:
            print(f'{last_used_index+1} {start_index}')
        last_used_index = start_index
