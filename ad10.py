def read_input(input_file):
    with open(input_file) as f:
        input_list = [line.strip() for line in f]
    return input_list

#************************* Part 1 *******************************************************************


def what_signal(signal):
    if signal == 'noop':
        return 'noop'
    else:
        return 'addx'


def get_add_value(signal):
    signal_lst = signal.split(" ")
    return int(signal_lst[1])


def parse_signal_list(signal_list):
    cycle = 0
    value_x_list = [1]
    all_signals = [0]
    #print(signal_list)
    for s in signal_list:
        cycle += 1
        if what_signal(s) == 'addx':
            signal_value = get_add_value(str(s))
            all_signals.append(signal_value)
            cycle += 1
            last_value = value_x_list[-1]
            value_x_list.append(last_value)
            cycle += 1
            value_x_list.append(value_x_list[-1] + all_signals[-1])
        else:
            value_x_list.append(value_x_list[-1])
    return value_x_list


#************************* Part 2 *******************************************************************

def parse_crt_row(crt_row, sprite_position):
    current_crt_row = ""
    cycle_num = 0
    for x in crt_row:
        if cycle_num in sprite_position:
            current_crt_row+="#"
        else:
            current_crt_row+="."
        sprite_position = [x-1,x,x+1]
        cycle_num+=1
    return [current_crt_row,sprite_position]


#************************* Main *******************************************************************


def main():
    #input_file = 'ad10test.txt'
    input_file = 'ad10.txt'
    #signal_list = ["noop", "addx 3", "addx -5"]
    signal_list = read_input(input_file)
    values_x_list = parse_signal_list(signal_list)
    total_result = 0
    for x in [20,60,100,140,180,220]:
        total_result+=values_x_list[x-1]*x
    print(total_result)

    #brute force
    crt_row1 = parse_crt_row(values_x_list[1:41], [0,1,2])
    crt_row2 = parse_crt_row(values_x_list[41:81], crt_row1[1])
    crt_row3 = parse_crt_row(values_x_list[81:121], crt_row2[1])
    crt_row4 = parse_crt_row(values_x_list[121:161], crt_row3[1])
    crt_row5 = parse_crt_row(values_x_list[161:201], crt_row4[1])
    crt_row6 = parse_crt_row(values_x_list[201:241], crt_row5[1])

    print(crt_row1[0])
    print(crt_row2[0])
    print(crt_row3[0])
    print(crt_row4[0])
    print(crt_row5[0])
    print(crt_row6[0])


if __name__ == '__main__':
    main()
