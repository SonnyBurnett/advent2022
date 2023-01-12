import colors
from operator import itemgetter
import datetime

def what_type_is_it(character):
    result = "unknown"
    if character in ["0","1","2","3","4","5","6","7","8","9"]:
        result = "integer"
    elif character == ",":
        result = "comma"
    elif character == "-":
        result = "dash"
    elif character == " ":
        result = "space"
    elif character == ">":
        result = "greater_than"
    else:
        result = "unknown"
    return result


def parse_input_scan(input_string):
    counter = 0
    number = ""
    result = []
    this_list = []
    while counter < len(input_string):
        character = input_string[counter]
        type_of_char = what_type_is_it(character)
        if type_of_char == "integer":
            number += character
        elif type_of_char == "comma":
            this_list.append(int(number))
            number = ""
        elif type_of_char == "space":
            if what_type_is_it(input_string[counter-1]) == "integer":
                this_list.append(int(number))
                result.append(this_list)
                this_list = []
                number = ""
        counter += 1
    this_list.append(int(number))
    result.append(this_list)
    return result


def get_in_between_positions(num1, num2, num3, type_of_move):
    result = []
    if num1 > num2:
        pos = list(range(num2, num1+1))
    else:
        pos = list(range(num1, num2+1))
    if type_of_move == "vertical":
        for x in pos:
            result.append([x,num3])
    else:
        for x in pos:
            result.append([num3, x])
    return result


def find_rock_positions(input_list):
    result = []
    counter = 0
    ver_prev = -1
    hor_prev = -1
    ver = -1
    hor = -1
    while counter < len(input_list):
        if ver != -1:
            ver_prev = ver
            hor_prev = hor
        ver = input_list[counter][1]
        hor = input_list[counter][0]
        if ver_prev != -1:
            if abs(ver - ver_prev) > 0:
                ver_positions = get_in_between_positions(ver, ver_prev, hor, "horizontal")
                for x in ver_positions:
                    result.append(x)
            else:
                hor_positions = get_in_between_positions(hor, hor_prev, ver, "vertical")
                for x in hor_positions:
                    result.append(x)
        counter+=1
    return result


def make_cave_visualization(rock_positions, boundaries, sand_positions):
    rock = colors.colorprint("#", 8)
    air = colors.colorprint(".", 3)
    sand = colors.colorprint("o", 0)
    sand_start = colors.colorprint("+", 5)
    low_ver = boundaries[0]
    high_ver = boundaries[1]
    low_hor = boundaries[2]
    high_hor = boundaries[3]
    for h in range(low_hor, high_hor + 1):
        if h < 10:
            print(colors.colorprint("  "+str(h), 5), end="")
        elif h < 100:
            print(colors.colorprint(" "+str(h), 5), end="")
        else:
            print(colors.colorprint(str(h), 5), end="")
        for v in range(low_ver, high_ver + 1):
            if [v, h] == [500, 0]:
                print(sand_start, end="")
            elif [v, h] in rock_positions:
                print(rock, end="")
            elif [v, h] in sand_positions:
                print(sand, end="")
            else:
                print(air, end="")
        print()
    print(colors.colorprint("", 300))


def move_sand_down(sand_pos, rock_positions, sand_positions, oblivion):
    no_air = rock_positions+sand_positions
    hor = sand_pos[0]
    ver = sand_pos[1]+1

    if ver > oblivion:
        sand_pos = [-100, -100]
    elif [hor,ver] not in no_air:
        sand_pos[1]+=1
    else:
        sand_pos = [-1,-1]

    return sand_pos


def move_sand_diagonal_left(sand_pos, rock_positions, sand_positions, oblivion):
    no_air = rock_positions+sand_positions
    hor_next = sand_pos[0]-1
    ver_next = sand_pos[1]+1

    if ver_next > oblivion:
        sand_pos = [-100, -100]
    elif [hor_next, ver_next] not in no_air:
        sand_pos[0]-=1
        sand_pos[1]+=1
    else:
        sand_pos = [-1,-1]
    return sand_pos


def move_sand_diagonal_right(sand_pos, rock_positions, sand_positions, oblivion):
    no_air = rock_positions+sand_positions
    hor_next = sand_pos[0] + 1
    ver_next = sand_pos[1] + 1

    if ver_next > oblivion:
        sand_pos = [-100, -100]
    elif [hor_next, ver_next] not in no_air:
        sand_pos[0]+=1
        sand_pos[1]+=1
    else:
        sand_pos = [-1,-1]

    return sand_pos


def let_the_sand_flow(rock_positions, sand_positions, oblivion, boundaries, total_rock):
    sand_still_flows = True
    counter = 0
    start_time = datetime.datetime.now()
    while sand_still_flows:
        sand_pos = [500, 0]
        this_sand_flows = True
        while this_sand_flows:
            tmp_pos_down = move_sand_down(sand_pos, rock_positions, sand_positions, oblivion)
            if tmp_pos_down == [-100, -100]:
                sand_still_flows = False
                break
            elif tmp_pos_down != [-1, -1]:
                sand_pos = tmp_pos_down
            else:
                tmp_pos_left = move_sand_diagonal_left(sand_pos, rock_positions, sand_positions, oblivion)
                if tmp_pos_left == [-100, -100]:
                    sand_still_flows = False
                    break
                elif tmp_pos_left != [-1, -1]:
                    sand_pos = tmp_pos_left
                else:
                    tmp_pos_right = move_sand_diagonal_right(sand_pos, rock_positions, sand_positions, oblivion)
                    if tmp_pos_right == [-100, -100]:
                        sand_still_flows = False
                        break
                    elif tmp_pos_right != [-1, -1]:
                        sand_pos = tmp_pos_right
                    else:
                        this_sand_flows = False

        if sand_still_flows:
            #make_cave_visualization(rock_positions, boundaries, sand_positions)
            sand_positions.append(sand_pos)
            counter += 1
            if counter%500 == 0:
                now = datetime.datetime.now()
                print("time elapsed", now-start_time)
                get_statistics(rock_positions, sand_positions, boundaries, oblivion, total_rock)
            if counter%10000 == 0:
                make_cave_visualization(rock_positions, boundaries, sand_positions)



        if sand_pos == [500, 0]:
            sand_still_flows = False
            break

    get_statistics(rock_positions, sand_positions, boundaries, oblivion, total_rock)

    return counter


def make_test():
    input1_test = "498,4 -> 498,6 -> 496,6"
    input2_test = "503,4 -> 502,4 -> 502,9 -> 494,9"
    parse1 = parse_input_scan(input1_test)
    parse2 = parse_input_scan(input2_test)
    rock_positions = find_rock_positions(parse1) + find_rock_positions(parse2)
    return rock_positions


def read_input(input_file):
    with open(input_file) as f:
        input_list = [line.strip() for line in f]
    return input_list


def read_the_cave():
    input_list = read_input("ad14.txt")
    input_list = sorted(input_list)
    rock_positions = []
    for x in input_list:
        tmp = find_rock_positions(parse_input_scan(x))
        for t in tmp:
            if not t in rock_positions:
                rock_positions.append(t)
    res = []
    [res.append(x) for x in rock_positions if x not in res]
    return res


def get_statistics(rock_positions, sand_positions, boundaries, oblivion, total_rock):
    pyramid = [(x * 2) + 1 for x in range(oblivion)]
    width_bottom = pyramid[-1]
    one_side_width = int((width_bottom - 1) / 2)
    new_boundary_left = 500 - one_side_width
    new_boundary_right = 500 + one_side_width
    total_pyramid = sum(pyramid)
    num_rock = len(rock_positions)
    num_sand = len(sand_positions)
    total_wide = new_boundary_right -new_boundary_left
    total_high = oblivion
    total_num = total_high * total_wide
    sand_positions = sorted(sand_positions, key=itemgetter(0), reverse=False)
    most_left_sand = sand_positions[0][0]
    most_right_sand = sand_positions[-1][0]


    print("*************** statistics report ***************")
    print()
    print("total sand           ", num_sand)
    print("area left boundary   ", boundaries[0])
    print("area right boundary  ", boundaries[1])
    print("sand most left       ", most_left_sand)
    print("sand most right      ", most_right_sand)
    print("new boundary left    ", new_boundary_left)
    print("new boundary right   ", new_boundary_right)
    print("total area square    ", total_num)
    print("expected area pyramid", total_pyramid)
    print("total rock           ", num_rock)
    print("actual rock          ", total_rock)
    print("total hight          ", boundaries[3])
    print("oblivion             ", oblivion)
    print("expected width bottom", width_bottom)









#************************* Main *******************************************************************


def main():

    test = False
    part_two = True


    if test:
        rock_positions = make_test()
        total_rock = len(rock_positions)
        high_ver = 9
        boundaries = [490, 510, 0, 12]
        oblivion = 11
    else:
        rock_positions = read_the_cave()
        total_rock = len(rock_positions)
        rock_positions = sorted(rock_positions, key=itemgetter(0), reverse=False)
        low_hor = rock_positions[0][0]
        high_hor = rock_positions[-1][0]
        rock_positions = sorted(rock_positions, key=itemgetter(1), reverse=False)
        low_ver = 0
        high_ver = rock_positions[-1][1]
        boundaries = [323, 677, low_ver, high_ver]
        oblivion = high_ver+2



    if part_two:
        for b in range(1000):
            rock_positions.append([b, oblivion])

    sand_positions = []
    make_cave_visualization(rock_positions, boundaries, sand_positions)

    units_of_sand = let_the_sand_flow(rock_positions, sand_positions, oblivion, boundaries, total_rock)
    make_cave_visualization(rock_positions, boundaries, sand_positions)
    print()
    print("units of sand", units_of_sand)
    print()
    print("expected 29805")











if __name__ == '__main__':
    main()

