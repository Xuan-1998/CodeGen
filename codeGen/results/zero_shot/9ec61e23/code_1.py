def calculate_mex(piece):
    has_zero = '00' in piece
    has_one = '01' in piece or '10' in piece
    has_two = '11' in piece
    if has_zero and has_one and has_two:
        return 2
    if (has_zero and has_one) or (has_zero and has_two) or (has_one and has_two):
        return 1
    return 0

def solve(n, top, bottom):
    pieces = []
    current_piece = set()
    for i in range(n):
        column = top[i] + bottom[i]
        # If adding this column to the current piece will complete the set of all four combinations
        if ('00' in current_piece and column == '11') or ('11' in current_piece and column == '00'):
            pieces.append(current_piece)
            current_piece = set()
        current_piece.add(column)
    pieces.append(current_piece)  # Add the last piece
    return sum(calculate_mex(piece) for piece in pieces)

# Read number of test cases
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    top = input().strip()
    bottom = input().strip()
    result = solve(n, top, bottom)
    print(result)
