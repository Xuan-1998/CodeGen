if __name__ == "__main__":
    t = input().strip()
    n = int(input())
    strings = [input().strip() for _ in range(n)]
    
    print(min_steps_to_color_text(t, strings))
