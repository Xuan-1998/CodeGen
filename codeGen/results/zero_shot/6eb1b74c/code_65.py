def solve():
    # ... (same as above)
    
    if min_steps == 0:
        return -1
    
    for i in range(min_steps):
        for j, string_index in enumerate(problem_state):
            if problem_state[j]:
                print(i + 1, string_index)
                problem_state[string_index].pop(0)

if __name__ == "__main__":
    while True:
        # ... (same as above)
        
        min_steps = solve()
        print(min_steps) if min_steps != -1 else print(-1)
