import colors


class Hill:
    def __init__(self, number, position, value, up, down, left, right, shortest, from_short):
        self.number = number
        self.position = position
        self.value = value
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.shortest = shortest
        self.from_short = from_short

    def get_value(self):
        return self.value

    def get_position(self):
        return self.position

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_up(self):
        return self.up

    def get_down(self):
        return self.down

    def get_shortest(self):
        return self.shortest

    def get_from_short(self):
        return self.from_short

    def set_shortest(self, shortest):
        self.shortest = shortest

    def set_from_short(self, from_short):
        self.from_short = from_short


def read_input():
    with open('ad12b.txt') as f:
        input_list = [line.strip() for line in f]
    return input_list


def read_test():
    return ["Sabqponm", "abcryxxl", "accszExk", "acctuvwj", "abdefghi"]


def create_num_matrix(matrix):
    result = []
    vl = len(matrix)
    hl = len(matrix[0])
    number = 0
    for v in range(0, vl):
        res_row = []
        for h in range(0, hl):
            res_row.append(number)
            number += 1
        result.append(res_row)
    return result


def find_start_position(matrix):
    ver_len = len(matrix)
    hor_len = len(matrix[0])
    number = 0
    for v in range(ver_len):
        for h in range(hor_len):
            if matrix[v][h] == "S":
                return number
            number += 1
    return -1


def find_end_position(matrix):
    vl = len(matrix)
    hl = len(matrix[0])
    number = 0
    for v in range(0, vl):
        for h in range(0, hl):
            if matrix[v][h] == "E":
                return number
            number += 1
    return -1


def find_new_left(position, num_matrix):
    ver = position[0]
    hor = position[1]
    if hor > 0:
        return num_matrix[ver][hor - 1]
    else:
        return -1


def find_new_right(position, matrix_size_hor, num_matrix):
    ver = position[0]
    hor = position[1]
    if hor < matrix_size_hor-1:
        return num_matrix[ver][hor + 1]
    else:
        return -1


def find_new_up(position, num_matrix):
    ver = position[0]
    hor = position[1]
    if ver > 0:
        return num_matrix[ver - 1][hor]
    else:
        return -1


def find_new_down(position, matrix_size_ver, num_matrix):
    ver = position[0]
    hor = position[1]
    if ver < matrix_size_ver-1:
        return num_matrix[ver + 1][hor]
    else:
        return -1


def get_value(matrix, position):
    v = position[0]
    h = position[1]
    pos_value = matrix[v][h]
    return pos_value


def fill_the_graph(matrix, num_matrix):
    graph = []
    ver_len = len(matrix)
    hor_len = len(matrix[0])
    number = 0
    for v in range(0, ver_len):
        for h in range(0, hor_len):
            position = [v, h]
            value = get_value(matrix, position)
            new_up = find_new_up(position, num_matrix)
            new_down = find_new_down(position, ver_len, num_matrix)
            new_left = find_new_left(position, num_matrix)
            new_right = find_new_right(position, hor_len, num_matrix)
            shortest = -1
            from_short = -1
            graph.append(Hill(number, position, value, new_up, new_down, new_left, new_right, shortest, from_short))
            number += 1
    return graph


def get_neighbours(node, graph):
    up = graph[node].get_up()
    down = graph[node].get_down()
    left = graph[node].get_left()
    right = graph[node].get_right()
    return [up, down, left, right]


def valid_move(value_from, value_to):
    f = ord(value_from)
    t = ord(value_to)

    result = False
    if value_to == "E" and value_from != "z":
        result = False
    elif value_from == "z" and value_to == "E":
        result = True
    elif value_from == "S" and value_to == "a":
        result = True
    elif f > t:
        result = True
    elif f == t-1:
        result = True
    elif f == t:
        result = True
    elif f < t-1:
        result = False

    return result


def valid_node(node):
    if node < 0:
        return False
    else:
        return True


def shorter_route(node, route_len, graph):
    node_len = graph[node].get_shortest()
    if node_len == -1:
        graph[node].set_shortest(route_len)
        return True
    elif route_len < node_len:
        return True
    else:
        return False


def traverse_graph(graph, start_point):
    queue = [start_point]
    graph[start_point].set_shortest(0)
    visited = []
    while queue:
        if len(queue) < 1:
            break
        current_node_num = queue[-1]
        del queue[-1]
        from_node_value = graph[current_node_num].get_value()
        neighbours_nums = get_neighbours(current_node_num, graph)
        from_len = graph[current_node_num].get_shortest()
        to_len = from_len + 1
        for to_node_num in neighbours_nums:
            if valid_node(to_node_num):
                to_node_value = graph[to_node_num].get_value()
                if valid_move(from_node_value, to_node_value):
                    if shorter_route(to_node_num, to_len, graph):
                        queue.append(to_node_num)
                        graph[to_node_num].set_shortest(to_len)
                        graph[to_node_num].set_from_short(current_node_num)
                        visited.append([current_node_num, to_node_num])
    return 0


def print_matrix(matrix):
    ver_len = len(matrix)
    hor_len = len(matrix[0])
    for v in range(ver_len):
        for h in range(hor_len):
            print(matrix[v][h], end=" ")
        print()


def print_all_route(num_matrix, graph):
    ver = len(num_matrix)
    hor = len(num_matrix[0])
    for v in range(0, ver):
        for h in range(0, hor):
            num = num_matrix[v][h]
            shortest = graph[num].get_shortest()
            value = graph[num].get_value()
            if shortest < 0:
                res = colors.colorprint(value, 5)
            elif value == "E":
                res = colors.colorprint(shortest, 4)
            else:
                res = colors.colorprint(shortest, 3)
            print(res, end=" ")
        print()
    print(colors.colorprint("", 300))


def find_way_back(graph, end, start):
    way_back = [end]
    node = end
    while node != start:
        node = graph[node].get_from_short()
        way_back.append(node)
    return way_back


def print_route(num_matrix, graph, shortest, type):
    ver = len(num_matrix)
    hor = len(num_matrix[0])
    for v in range(0, ver):
        for h in range(0, hor):
            num = num_matrix[v][h]
            value = graph[num].get_value()
            if num in shortest:
                if type == "V":
                    res = colors.colorprint(value, 5)
                else:
                    res = colors.colorprint(num, 5)
            else:
                if type == "V":
                    res = colors.colorprint(value, 3)
                else:
                    res = colors.colorprint(num, 3)
            print(res, end=" ")
        print()
    print(colors.colorprint("", 300))


def print_color_character(matrix):
    ver = len(matrix)
    hor = len(matrix[0])
    for v in range(0, ver):
        for h in range(0, hor):
            if matrix[v][h] == "a":
                print(colors.colorprint(matrix[v][h], 3), end=" ")
            elif matrix[v][h] == "b":
                print(colors.colorprint(matrix[v][h], 1), end=" ")
            elif matrix[v][h] == "f":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            elif matrix[v][h] == "g":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            elif matrix[v][h] == "h":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            elif matrix[v][h] == "i":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            elif matrix[v][h] == "j":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            elif matrix[v][h] == "k":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            elif matrix[v][h] == "c":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            elif matrix[v][h] == "b":
                print(colors.colorprint(matrix[v][h], 2), end=" ")
            else:
                print(colors.colorprint(matrix[v][h], 2), end=" ")
        print()
    print(colors.colorprint("", 300))


def print_numbers_route(matrix):
    ver = len(matrix)
    hor = len(matrix[0])
    counter = 0
    spaces=""
    for v in range(0, ver):
        for h in range(0, hor):
            if counter < 10:
                spaces = "   "
            elif counter < 100:
                spaces = "  "
            elif counter < 1000:
                spaces = " "
            else:
                spaces = ""

            res = colors.colorprint(str(counter)+spaces, 5)
            print(res, end=" ")
            counter+=1
        print()
    print(colors.colorprint("", 300))


def get_possible_start_positions(matrix):
    result = []
    ver = len(matrix)
    for v in range(0, ver):
        result.append(matrix[v][0])
    return result



def main():
    matrix = read_input()
    #matrix = read_test()
    num_matrix = create_num_matrix(matrix)
    start = find_start_position(matrix)
    end = find_end_position(matrix)
    graph = fill_the_graph(matrix, num_matrix)

    which_part = 2

    if which_part == 1:
        traverse_graph(graph, start)
        way_back = find_way_back(graph, end, start)
        print_route(num_matrix, graph, way_back, "V")
        print("Length shortest path to E", graph[end].get_shortest())

    if which_part == 2:
        #print_color_character(matrix)
        #print_numbers_route(matrix)
        starts = get_possible_start_positions(num_matrix)
        shortste = 100000
        shortest_start_node = 0
        counter = 0
        for s in starts:
            start = s
            graph = fill_the_graph(matrix, num_matrix)
            traverse_graph(graph, start)
            this_shortste = graph[end].get_shortest()
            if this_shortste < shortste:
                shortste = this_shortste
                shortest_start_node = s
            print(counter, "node", s, "Length shortest path to E", this_shortste)
            print()
            way_back = find_way_back(graph, end, start)
            print_route(num_matrix, graph, way_back, "V")
            counter+=1

        print()
        print("shortest path is", shortste, "coming from", shortest_start_node)






if __name__ == '__main__':
    main()
