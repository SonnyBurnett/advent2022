def read_input():
    with open('ad8.txt') as f:
        input_list = [line.strip() for line in f]
    return input_list


def find_highest_neighbours(hor,ver, input_list):
    up_list = [int(x[hor]) for x in input_list][0:ver]
    down_list = [int(x[hor]) for x in input_list][ver+1:]
    left_list = [int(x) for x in input_list[ver][0:hor]]
    right_list = [int(x) for x in input_list[ver][hor+1:]]
    up_list.sort(reverse=True)
    down_list.sort(reverse=True)
    left_list.sort(reverse=True)
    right_list.sort(reverse=True)
    return [up_list[0], down_list[0], left_list[0], right_list[0]]


def parse_matrix(input_list, matrix_size):
    counter_hor = 1
    counter_ver = 1
    counter_visible = 0
    while counter_ver < matrix_size-1:
        tree_line = input_list[counter_ver]
        while counter_hor < matrix_size - 1:
            tree_to_check = tree_line[counter_hor]
            neighbours = find_highest_neighbours(counter_hor, counter_ver, input_list)
            neighbours.sort()
            if int(tree_to_check) > neighbours[0]:
                counter_visible += 1
            counter_hor += 1
        counter_hor = 1
        counter_ver+=1
    return counter_visible


def find_visible_trees(input_list):
    matrix_size = len(input_list)
    visible_trees_from_outside = (4 * matrix_size) - 4
    visible_trees_from_inside = parse_matrix(input_list, matrix_size)
    return visible_trees_from_inside + visible_trees_from_outside


#************************* Part 2 *******************************************************************

def find_trees_in_view(input_list, num):
    index_first_match = next((index for index, item in enumerate(input_list) if item >= num),None)
    if index_first_match is not None:
        return input_list[0:index_first_match+1]
    else:
        return input_list


def find_tree_scenic_score(hor,ver, input_list):
    num = int(input_list[ver][hor])
    up_list = [int(x[hor]) for x in input_list][0:ver]
    up_list.reverse()
    down_list = [int(x[hor]) for x in input_list][ver+1:]
    left_list = [int(x) for x in input_list[ver][0:hor]]
    left_list.reverse()
    right_list = [int(x) for x in input_list[ver][hor+1:]]
    u_view_list = find_trees_in_view(up_list, num)
    d_view_list = find_trees_in_view(down_list, num)
    l_view_list = find_trees_in_view(left_list, num)
    r_view_list = find_trees_in_view(right_list, num)
    scenic_score = len(u_view_list)*len(d_view_list)*len(l_view_list)*len(r_view_list)
    return scenic_score


def parse_for_scenic_score(input_list):
    matrix_size = len(input_list)
    counter_hor = 1
    counter_ver = 1
    highest_scenic_score = 0
    while counter_ver < matrix_size-1:
        while counter_hor < matrix_size - 1:
            scenic_score = find_tree_scenic_score(counter_hor, counter_ver, input_list)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score
            counter_hor += 1
        counter_hor = 1
        counter_ver+=1
    return highest_scenic_score


#************************* Test *******************************************************************


def test_ad8():
    expected_outcome_1 = 21
    expected_outcome_2 = 8
    input_list = ["30373","25512","65332","33549","35390"]
    calculated_outcome = find_visible_trees(input_list)
    highest_scenic_score = parse_for_scenic_score(input_list)
    if calculated_outcome == expected_outcome_1 and highest_scenic_score == expected_outcome_2:
        return True
    else:
        print("test failed")
        return False


#************************* Main *******************************************************************


def main():
    if test_ad8():
        input_list = read_input()
        print("visible trees:", find_visible_trees(input_list))
        print("highest scenic score:", parse_for_scenic_score(input_list))


if __name__ == '__main__':
    main()

