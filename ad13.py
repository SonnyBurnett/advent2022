
def read_input(input_file):
    with open(input_file) as f:
        input_list = [line.strip() for line in f]
    return input_list


def find_sub_lists(input_string):
    text = input_string
    istart = []  # stack of indices of opening parentheses
    d = {}
    for i, c in enumerate(text):
        if c == '[':
            istart.append(i)
        if c == ']':
            try:
                d[istart.pop()] = i
            except IndexError:
                print('Too many closing parentheses')
    if istart:  # check if stack is empty afterwards
        print('Too many opening parentheses')
    #print(d)
    return d


def what_type_is_it(character):
    result = "unknown"
    if character in ["0","1","2","3","4","5","6","7","8","9"]:
        result = "integer"
    elif character == ",":
        result = "comma"
    elif character == "[":
        result = "open_parentheses"
    elif character == "]":
        result = "close_parentheses"
    else:
        result = "unknown"
    return result


def parse_string(input_string):
    parent_lists = find_sub_lists(input_string)
    counter = 1
    number = ""
    this_list = []
    while counter < len(input_string):
        character = input_string[counter]
        type_of_char = what_type_is_it(character)
        if type_of_char == "integer":
            number+=character
        elif type_of_char == "comma":
            this_list.append(int(number))
            number = ""
        elif type_of_char == "open_parentheses":
            open_parent_index = counter
            close_parent_index = parent_lists[open_parent_index]
            new_list_string = input_string[open_parent_index:close_parent_index+1]
            new_list = parse_string(new_list_string)
            this_list.append(new_list)
            counter = close_parent_index+1
        elif type_of_char == "close_parentheses":
            if len(number) > 0:
                this_list.append(int(number))
            break
        else:
            print("something went terribly wrong somewhere")
        counter+=1
    return this_list


def what_type(input_var):
    if type(input_var) == list:
        result = "list"
    elif type(input_var) == int:
        result = "int"
    else:
        result = "none"
    return result


def get_type_or_none(counter, list):
    if counter < len(list):
        var = list[counter]
        result = what_type(var)
    else:
        result = "none"
    return result


def compare_packet_lists(left_list, right_list):
    right_order = "undetermined"
    counter = 0
    while (counter < len(left_list) or counter < len(right_list)) and right_order == "undetermined":
        left_type = get_type_or_none(counter, left_list)
        right_type = get_type_or_none(counter, right_list)
        if left_type == "int" and right_type == "int":
            left_value = left_list[counter]
            right_value = right_list[counter]
            if left_value < right_value:
                right_order = "true"
                #print("right order, left", left_value, "is smaller than right", right_value)
            elif left_value > right_value:
                right_order = "false"
                #print("wrong order, left", left_value, "is greater than right", right_value)
            elif left_value == right_value:
                right_order = "undetermined"
        elif left_type == "list" and right_type == "list":
            right_order = "undetermined"
            right_order = compare_packet_lists(left_list[counter], right_list[counter])
        elif left_type == "list" and right_type == "int":
            right_order = "undetermined"
            right_order = compare_packet_lists(left_list[counter], [right_list[counter]])
        elif left_type == "int" and right_type == "list":
            right_order = "undetermined"
            right_order = compare_packet_lists([left_list[counter]], right_list[counter])
        elif (left_type == "int" or left_type == "list") and right_type == "none":
            #print("Wrong order, right ran out of items before we could make a decision")
            right_order = "false"
        elif left_type == "none" and (right_type == "int" or right_type == "list"):
            #print("Right order. left ran out of items before we could make a decision")
            right_order = "true"
        elif left_type == "none" and right_type == "none":
            print("Nothing to compare")
        counter+=1
    return right_order


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def sort_packages(input_list):
    counter = 0
    result = [input_list[0]]
    for right_item in input_list[1:]:
        pos_found = False
        for left_item in result:
            compare_result = compare_packet_lists(left_item, right_item)
            if compare_result == "false":
                result.insert(result.index(left_item), right_item)
                pos_found = True
                break
        if not pos_found:
            result.append(right_item)
    return result


def main():
    input_file = "ad13.txt"
    input_test = "ad13-test.txt"
    input_strings = read_input(input_file)
    expected_outcomes_test = {1: "true", 2: "true", 3: "false", 4: "true", 5: "false", 6: "true", 7: "false", 8: "false"}

    counter = 0
    index_counter = 1
    right_indexes = []
    while counter < len(input_strings):
        left_string = parse_string(input_strings[counter])
        right_string = parse_string(input_strings[counter+1])
        print("left ", left_string)
        print("right", right_string)
        result = compare_packet_lists(left_string, right_string)
        if result == "true":
            right_indexes.append(index_counter)
        print()
        counter+=3
        index_counter +=1

    print("The sum of the right indices is", sum(right_indexes))

    # part 2
    # put all packages in the right order
    # meaning sorting
    # and I need to add 2 divider packages

    counter = 0
    new_input = [[[2]], [[6]]]
    while counter < len(input_strings):
        left_string = parse_string(input_strings[counter])
        right_string = parse_string(input_strings[counter + 1])
        new_input.append(left_string)
        new_input.append(right_string)
        counter += 3

    result = sort_packages(new_input)
    divider_code1_index = result.index([[2]])+1
    divider_code2_index = result.index([[6]])+1


    for r in result:
        print(r)
    print()

    print("decoder key is", divider_code1_index, "*", divider_code2_index, "=", divider_code1_index*divider_code2_index)





if __name__ == '__main__':
    main()