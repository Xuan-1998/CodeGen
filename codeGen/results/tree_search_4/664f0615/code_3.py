if __name__ == "__main__":
    initial_speed, final_speed, allowed_change, time = [int(x) for x in input().split()]
    print(max_path_length(initial_speed, final_speed, allowed_change, time))
