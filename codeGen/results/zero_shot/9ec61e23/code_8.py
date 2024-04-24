def calculate_mex_sum(n, top_row, bottom_row):
    mex_sum = 0
    i = 0
    while i < n:
        if top_row[i] == '0' and bottom_row[i] == '0':
            mex_sum += 1
            i += 1
        elif top_row[i] == '1' and bottom_row[i] == '1':
            while i < n and (top_row[i] != '0' or bottom_row[i] != '0'):
                i += 1
            mex_sum += 2
        else:
            mex_sum += 2
            i += 1
    return mex_sum

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        top_row = input().strip()
        bottom_row = input().strip()
        result = calculate_mex_sum(n, top_row, bottom_row)
        print(result)

if __name__ == "__main__":
    main()
