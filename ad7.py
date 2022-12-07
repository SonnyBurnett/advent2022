TOTAL_COUNTS = []


def read_input():
    with open('ad7.txt') as f:
        input_list = [line.strip() for line in f]
    return input_list


def parse_command(input_string):
    if input_string == '$ cd ..':
        return -1
    elif input_string[0:4] == '$ cd':
        return 0
    elif input_string[0:4] == '$ ls':
        return -2
    elif input_string[0:4] == 'dir ':
        return -2
    else:
        num = input_string.split(' ')
        return int(num[0])


def parse_queue(input_queue, total_bytes):
    result = 0
    while result != -1 and len(input_queue) > 0:
        result = parse_command(input_queue[0])
        if result == 0:
            node_naam_list = input_queue[0].split(' ')
            node_naam_name = node_naam_list[2]
            if node_naam_name != '/':
                output_process = parse_queue(input_queue[1:], 0)
                total_bytes = total_bytes + output_process[0]
                input_queue = input_queue[-1*output_process[1]-1:]
        elif result > 0:
            total_bytes = total_bytes + result
        input_queue.pop(0)
    TOTAL_COUNTS.append(total_bytes)
    return [total_bytes, len(input_queue)]


def find_smallest_directory_to_delete(input_list):
    update_size = 30000000
    total_disk_size = 70000000
    disk_usage = sum([parse_command(x) for x in input_list if parse_command(x) > 0])
    total_free = total_disk_size - disk_usage
    minimal_delete = update_size - total_free
    candidate_list = [x for x in TOTAL_COUNTS if x >= minimal_delete]
    candidate_list.sort()
    return candidate_list[0]


def main():
    input_list = read_input()
    parse_queue(input_list, 0)
    print("part 1:", sum([x for x in TOTAL_COUNTS if x <= 100000]))
    print("part 2:", find_smallest_directory_to_delete(input_list))


if __name__ == '__main__':
    main()
