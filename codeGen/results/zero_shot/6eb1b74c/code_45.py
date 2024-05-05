if min_steps == float('inf'):
    print(-1)
else:
    for i in range(min_steps):
        print(i+1, used_strings[i])
