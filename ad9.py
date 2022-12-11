def read_input():
    with open('ad9.txt') as f:
        input_list = [line.strip() for line in f]
    return input_list

#************************* Part 1 *******************************************************************


def make_flat_list(not_flat_list):
    flat_list = []
    for x in not_flat_list:
        num = int(x[2:])
        for y in range(0,num):
            flat_list.append(x[0])
    return flat_list


def move_knot(knot_coordinates, move_to_make):
    new_coordinates = knot_coordinates
    if move_to_make == 'U':
        new_coordinates = [knot_coordinates[0]-1,knot_coordinates[1]]
    elif move_to_make == 'D':
        new_coordinates = [knot_coordinates[0]+1,knot_coordinates[1]]
    elif move_to_make == 'L':
        new_coordinates = [knot_coordinates[0], knot_coordinates[1]-1]
    elif move_to_make == 'R':
        new_coordinates = [knot_coordinates[0], knot_coordinates[1]+1]
    return new_coordinates


def tail_adjacent_head(ch,ct):
    v = ch[0]
    h = ch[1]
    adjacent_list = [[v - 1, h - 1], [v - 1, h], [v - 1, h + 1],
                     [v, h - 1], [v, h], [v, h + 1],
                     [v + 1, h - 1], [v + 1, h], [v + 1, h + 1]]
    if ct in adjacent_list:
        return True
    return False


def define_next_move_tail(ch, ct):
    vh = ch[0]
    hh = ch[1]
    vt = ct[0]
    ht = ct[1]
    new_tail_ver = vt
    new_tail_hor = ht
    if vh != vt and hh != ht:
        if abs(hh - ht) > 1 and abs(vh - vt) > 1:
            new_tail_hor += int((hh - ht) / 2)
            new_tail_ver += int((vh - vt) / 2)
        elif abs(hh - ht) > 1:
            new_tail_hor += int((hh - ht) / 2)
            new_tail_ver += int(vh - vt)
        elif abs(vh - vt) > 1:
            new_tail_hor += int(hh - ht)
            new_tail_ver += int((vh - vt)/2)
    elif vh == vt and hh != ht:
        new_tail_hor+=int((hh-ht)/2)
    elif vh != vt and hh == ht:
        new_tail_ver+=int((vh-vt)/2)
    return [new_tail_ver, new_tail_hor]


def calculate_unique_positions(input_list):
    move_list = make_flat_list(input_list)
    head_position = [0, 0]
    tail_position = [0, 0]
    all_positions_tail = [[0, 0]]
    for x in move_list:
        head_position = move_knot(head_position, x)
        if not tail_adjacent_head(head_position, tail_position):
            tail_position = define_next_move_tail(head_position, tail_position)
            if tail_position not in all_positions_tail:
                 all_positions_tail.append(tail_position)
    return len(all_positions_tail)


#************************* Part 2 *******************************************************************


def unique_positions_long_rope(input_list):
    input_list2 = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]
    input_list1 = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    move_list = make_flat_list(input_list)
    position_list = [[4,0],[4,0],[4,0],[4,0],[4,0],[4,0],[4,0],[4,0],[4,0],[4,0]]
    all_positions_tail = [[4, 0]]
    for x in move_list:
        position_list[0] = move_knot(position_list[0], x)
        for y in range(1,10):
            if not tail_adjacent_head(position_list[y-1], position_list[y]):
                position_list[y] = define_next_move_tail(position_list[y-1],position_list[y])
        if position_list[9] not in all_positions_tail:
            all_positions_tail.append(position_list[9])
    return len(all_positions_tail)


def print_matrix(pos_list):
    for x in range(0,5):
        for y in range(0, 6):
            pos = -1
            if [x,y] in pos_list:
                pos = pos_list.index([x,y])
            if pos > 0:
                print(pos, end=" ")
            elif pos == 0:
                print("H", end=" ")
            else:
                print(".", end=" ")
        print()
    print()



#************************* Test *******************************************************************


def test_ad9():
    expected_outcome_1 = 14
    expected_outcome_2 = 0
    input_list = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]
    input_list2 = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]

    calculated_outcome = calculate_unique_positions(input_list)
    if calculated_outcome == expected_outcome_1:
        return True
    else:
        print("test failed")
        return False


#************************* Main *******************************************************************


def main():
    if test_ad9():
        input_list = read_input()
        print("1", calculate_unique_positions(input_list))
    print(unique_positions_long_rope(input_list = read_input()))


if __name__ == '__main__':
    main()
