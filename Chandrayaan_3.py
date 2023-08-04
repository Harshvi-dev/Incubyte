def translate_commands(initial_position, initial_direction, commands):
    direction_changes = {
        "N": (0, 1, 0),
        "S": (0, -1, 0),
        "E": (1, 0, 0),
        "W": (-1, 0, 0),
        "Up": (0, 0, 1),
        "Down": (0, 0, -1)
    }
    
    current_position = initial_position
    current_direction = initial_direction
    
    for command in commands:
        if command == "f" or command == "b":
            change = direction_changes[current_direction]
            if command == "b":
                change = tuple(-x for x in change)
            current_position = tuple((old + new) for old, new in zip(current_position, change))
        elif command == "l" or command == "r":
            directions = ["N", "E", "S", "W", "Up", "Down"]
            current_index = directions.index(current_direction)
            if command == "l":
                current_index = (current_index - 1) % 4
            else:
                current_index = (current_index + 1) % 4
            current_direction = directions[current_index]
        elif command == "u" or command == "d":
            if current_direction in ["N", "E", "W", "S"]:
                if command == "u":
                    current_direction = "Up"
                else:
                    current_direction = "Down"
    return current_position, current_direction

if __name__ == "__main__":
    initial_position = (0, 0, 0)
    initial_direction = "N"
    commands = ["f", "r", "u", "b", "l"]
    # commands = ["f", "r", "u", "b", "l", "d", "f"]
    # commands = ["f", "u", "d", "r", "u", "l"]
    final_position, final_direction = translate_commands(initial_position, initial_direction, commands)
    print("Final Position:", final_position)
    print("Final Direction:", final_direction)
