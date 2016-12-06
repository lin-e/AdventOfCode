# let directions :
# 0 = north
# 1 = east
# 2 = south
# 3 = west
# such that turning left implies n = (4 + (n - 1)) mod 4
# and that turning right implies n = n + 1 mod 4
#
from turtle import *
def get_movement(current_dir, new_dir):
    now_facing = 0
    if new_dir == "L":
        now_facing = (4 + (current_dir - 1)) % 4
    elif new_dir == "R":
        now_facing = (current_dir + 1) % 4
    else:
        now_facing = current_dir
    addition_matrix = {
        0: [0, 1],
        1: [1, 0],
        2: [0, -1],
        3: [-1, 0]
        }.get(now_facing, [0, 0])
    return [int(addition_matrix[0]), int(addition_matrix[1]), now_facing]
def add_matrix(operand_a, operand_b):
    return [operand_a[0] + operand_b[0], operand_a[1] + operand_b[1]]
def draw_line(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    penup()
def map_point(x1, y1, x2, y2, x_scale, y_scale, offset):
    draw_line((x1 * x_scale) + offset[0], (y1 * y_scale) + offset[1], (x2 * x_scale) + offset[0], (y2 * y_scale) + offset[1])
def simple_wall(x1, y1, x2, y2):
    map_point(x1, y1, x2, y2, 10, 10, [0, 0])
color("black")
speed(0)
current = [0, 0]
input_string = "R3, R1, R4, L4, R3, R1, R1, L3, L5, L5, L3, R1, R4, L2, L1, R3, L3, R2, R1, R1, L5, L2, L1, R2, L4, R1, L2, L4, R2, R2, L2, L4, L3, R1, R4, R3, L1, R1, L5, R4, L2, R185, L2, R4, R49, L3, L4, R5, R1, R1, L1, L1, R2, L1, L4, R4, R5, R4, L3, L5, R1, R71, L1, R1, R186, L5, L2, R5, R4, R1, L5, L2, R3, R2, R5, R5, R4, R1, R4, R2, L1, R4, L1, L4, L5, L4, R4, R5, R1, L2, L4, L1, L5, L3, L5, R2, L5, R4, L4, R3, R3, R1, R4, L1, L2, R2, L1, R4, R2, R2, R5, R2, R5, L1, R1, L4, R5, R4, R2, R4, L5, R3, R2, R5, R3, L3, L5, L4, L3, L2, L2, R3, R2, L1, L1, L5, R1, L3, R3, R4, R5, L3, L5, R1, L3, L5, L5, L2, R1, L3, L1, L3, R4, L1, R3, L2, L2, R3, R3, R4, R4, R1, L4, R1, L5,".split()
new_string = list()
for i in input_string:
    direction = i[0]
    times = int(i[1:][:-1])
    for x in range(0, times):
        if x == 0:
            new_string.append(direction)
        else:
            new_string.append("F")
input_string = new_string
print(new_string)
all_turns = list()
direction = 0
for i in input_string:
    print(i)
    all_turns.append(current)
    new = get_movement(direction, str(i))
    direction = new[2]
    old_current = current
    current = add_matrix(current, new)
    print(current)
    if current in all_turns:
        break
    simple_wall(old_current[0], old_current[1], current[0], current[1])
print(current)
