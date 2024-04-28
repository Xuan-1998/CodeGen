from collections import deque

def is_circular(moves):
    moves = moves + moves  # Duplicate the moves to consider circular sequences
    last_move_index = len(moves) - 1
    
    for i in range(len(moves)):
        if moves[i:i+2] == 'FL' or moves[i:i+2] == 'FR':
            if i > 0 and moves[i-1] == 'F':  # If the robot is moving forward and then turns left/right
                start_index = i - 1
                end_index = last_move_index + 1
                while True:
                    if moves[start_index:end_index] in ['FF', 'LL', 'RR']:
                        return "Circular"
                    start_index += 1
                    end_index -= 1
            else:  # If the robot is not moving forward or already turned left/right
                return "Not Circular"
        elif moves[i:i+2] == 'BL' or moves[i:i+2] == 'BR':
            if i > 0 and moves[i-1] == 'B':  # If the robot is moving backward and then turns left/right
                start_index = i - 1
                end_index = last_move_index + 1
                while True:
                    if moves[start_index:end_index] in ['BF', 'LL', 'RR']:
                        return "Circular"
                    start_index += 1
                    end_index -= 1
            else:  # If the robot is not moving backward or already turned left/right
                return "Not Circular"

    return "Not Circular"
