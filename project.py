# Simulate maze escape
# " " - walkable path; "#" - wall
# "S"/"E" - start/end
# 
# orientation Enum represented as an integer (named direction):
# 0 = up
# 1 = right
# 2 = down
# 3 = left

maze = [
    list("##########"),
    list("#S #     #"),
    list("#  # ### #"),
    list("#  # #   #"),
    list("#  ### # #"),
    list("#      # #"),
    list("###### # #"),
    list("#    # # #"),
    list("# ##   #E#"),
    list("##########"),
]

direction = 2 # facing down by default
operations = 0
maze_complete = False
x, y = 0, 0

direction_forward = [
    (0, -1), # index = 0 -> facing up
    (1, 0), # index = 1 -> facing right
    (0, 1), # index = 2 -> facing down
    (-1, 0), # index = 3 -> facing left
]
direction_right = [
    (1, 0), # facing up, right tile relative to current pos is offset by -1 on x axis
    (0, 1), # similar here and following
    (-1, 0), 
    (0, -1),
]
direction_string = ["⬆️","➡️","⬇️","⬅️"]

def turn_right():
    global operations, direction
    operations += 1
    direction = (direction + 1) % 4
def turn_left():
    global operations, direction
    operations += 1
    direction = (direction - 1) % 4
def move_forward():
    global operations, x, y, maze_complete
    new_x = x + direction_forward[direction][0]
    new_y = y + direction_forward[direction][1]

    wall_in_front = False
    if new_y > len(maze) or new_y < 0: # out of bounds - cosider a wall
        wall_in_front = True
    if not wall_in_front:
        if new_x > len(maze[new_y]) or new_x < 0: # out of bounds - cosider a wall
            wall_in_front = True
    if not wall_in_front:
        wall_in_front = maze[new_y][new_x] == "#"
    
    if wall_in_front:
        return False
    
    operations += 1
    x, y = new_x, new_y
    if maze[new_y][new_x] == "E":
        maze_complete = True
    return True
def get_right_tile():
    global x, y

    right_tile_x = x + direction_right[direction][0]
    right_tile_y = y + direction_right[direction][1]

    if right_tile_y > len(maze) or right_tile_y < 0: # out of bounds - consider a wall
        return "#"
    if right_tile_x > len(maze[right_tile_y]) or right_tile_x < 0: # out of bounds - consider a wall
        return "#"
    return maze[right_tile_y][right_tile_x]

# define starting position
for row in range(len(maze)):
    for column in range(len(maze[row])):
        if maze[row][column] == "S":
            x, y = column, row
            break

while not maze_complete and operations < 1e6: # limit up to 1 million operations (1e6 = 1000000 = Million)
    # if there's a wall to the right, move forward
    # if moving forward isn't an option, turn right
    # if there's no wall to the right, keep turning right

    wall_on_right = get_right_tile() == "#"
    forward_success = True

    #print(wall_on_right, x, y, direction)
    if wall_on_right:
        forward_success = move_forward() # False means moving forward didn't happen because there's a wall!
        if not (get_right_tile() == "#"):
            turn_right()
            move_forward()
    if not wall_on_right or not forward_success:
        turn_right()

    # print the maze
    print(operations)
    for row in range(len(maze)):
        row_string = ""
        for column in range(len(maze[row])):
            if column == x and row == y:
                row_string += " " + direction_string[direction] + " "
                continue
            row_string += " " + maze[row][column] + " "
        print(row_string)
    print("\n\n\n")
if maze_complete:
    print(f"Maze complete after {operations} steps")
else:
    print(f"Step limit of {operations} reached; Maze was not solved.")