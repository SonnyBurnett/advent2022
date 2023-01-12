import colors
from operator import itemgetter
import time


class Sensor:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def get_value_x(self):
        return self.x

    def get_value_y(self):
        return self.y

    def get_position(self):
        return [self.x, self.y]

    def is_y_in_range(self, certain_y):
        if self.y-self.distance <= certain_y <= self.y+self.distance:
            return True
        else:
            return False

    def get_x_range(self, certain_y):
        lower_x = self.x - (self.distance - (abs(self.y - certain_y)))
        upper_x = self.x + (self.distance - (abs(self.y - certain_y)))
        return [lower_x, upper_x]


def read_input(input_file):
    with open(input_file) as f:
        input_list = [line.strip() for line in f]
    return input_list


def strip_coordinates(input_line):
    x1_start = 12
    x1_end = input_line.find(',')
    y1_start = input_line.find(', y=')+4
    y1_end = input_line.find(':')
    x2_start = input_line.rfind('at x=')+5
    x2_end = input_line.rfind(', y=')
    y2_start = input_line.rfind(', y=')+4
    y2_end = len(input_line)
    x1 = int(input_line[x1_start:x1_end])
    y1 = int(input_line[y1_start:y1_end])
    x2 = int(input_line[x2_start:x2_end])
    y2 = int(input_line[y2_start:y2_end])
    return [[x1, y1], [x2, y2]]


def get_corners(sensors, beacons):
    sensors = sorted(sensors, key=itemgetter(0), reverse=False)
    low_x = sensors[0][0]
    high_x = sensors[-1][0]
    sensors = sorted(sensors, key=itemgetter(1), reverse=False)
    low_y = sensors[0][1]
    high_y = sensors[-1][1]

    beacons = sorted(beacons, key=itemgetter(0), reverse=False)
    if beacons[0][0] < low_x:
        low_x = beacons[0][0]
    if beacons[-1][0] > high_x:
        high_x = beacons[-1][0]
    beacons = sorted(beacons, key=itemgetter(1), reverse=False)
    if beacons[0][1] < low_y:
        low_y = beacons[0][1]
    if beacons[-1][1] > high_y:
        high_y = beacons[-1][1]

    return [low_x, high_x, low_y, high_y]


def get_sensors(locations):
    sensors = []
    for x in locations:
        sensors.append(x[0])
    return sensors


def get_beacons(locations):
    beacons = []
    for x in locations:
        beacons.append(x[1])
    return beacons


def draw_sensors_and_beacons(locations, positions):
    sensor = colors.colorprint("S", 5)
    beacon = colors.colorprint("B", 1)
    air = colors.colorprint(".", 3)
    position = colors.colorprint("#", 10)
    sensors = get_sensors(locations)
    beacons = get_beacons(locations)
    corners = [-5, 25, -5, 25]
    for y in range(corners[2], corners[3] + 1):
        for x in range(corners[0], corners[1] + 1):
            if [x, y] in sensors:
                print(sensor, end="")
            elif [x, y] in beacons:
                print(beacon, end="")
            elif [x, y] in positions:
                print(position, end="")
            else:
                print(air, end="")
        print()
    print()
    print(colors.colorprint("", 300))


def get_distance(sensor, beacon):
    x = abs(sensor[0]-beacon[0])
    y = abs(sensor[1]-beacon[1])
    return x+y


def get_all_positions(sensor, sensor_distance, the_row):
    sensor_x = sensor[0]
    sensor_y = sensor[1]
    the_row_distance = abs(sensor_y-the_row)
    if the_row_distance <= sensor_distance:
        one_way_distance = abs(the_row_distance-sensor_distance)
        lower_bound = sensor_x-one_way_distance
        upper_bound = sensor_x+one_way_distance
        total_range = get_range_of_positions(lower_bound, upper_bound)
        return total_range
    else:
        return []


def get_range_of_positions(lower_bound, upper_bound):
    return [d for d in range(lower_bound, upper_bound+1)]


def get_unique_beacons(beacons, the_row):
    beacons_on_the_row = 0
    unique_beacons = []
    [unique_beacons.append(x) for x in beacons if x not in unique_beacons]
    for b in unique_beacons:
        if b[1] == the_row:
            beacons_on_the_row += 1
    return beacons_on_the_row


def get_all_ranges(y, sensors):
    ranges = []
    for s in sensors:
        if s.is_y_in_range(y):
            ranges.append(s.get_x_range(y))
    return ranges


def merge_ranges(ranges, limit):
    result = -1
    sensors = sorted(ranges, key=itemgetter(0), reverse=False)
    high_x = sensors[0][1]
    for r in sensors[1:]:
        next_low_x = r[0]
        next_high_x = r[1]
        if next_low_x > high_x+1:
            if -1 < high_x+1 < limit:
                result = high_x+1
                break
        elif next_high_x > high_x:
            high_x = next_high_x
    return result


def get_locations(input_strings):
    locations = []
    for x in input_strings:
        locations.append(strip_coordinates(x))
    return locations


def find_beacon_positions(locations, the_row):
    beacons = get_beacons(locations)
    beacons_on_the_row = get_unique_beacons(beacons, the_row)
    positions = []
    for d in locations:
        sensor = d[0]
        beacon = d[1]
        distance = get_distance(sensor, beacon)
        this_positions = get_all_positions(sensor, distance, the_row)
        if len(this_positions) > 0:
            positions += this_positions
            positions = list(set(positions))
    return len(positions) - beacons_on_the_row


def find_only_possible_point(locations, upper_limit, start):
    sensors = []
    for d in locations:
        sensor = d[0]
        beacon = d[1]
        distance = get_distance(sensor, beacon)
        sensors.append(Sensor(sensor[0], sensor[1], distance))
    sx = sy = 0
    for y in range(upper_limit + 1):
        ranges = get_all_ranges(y, sensors)
        range_result = merge_ranges(ranges, upper_limit)
        if range_result > -1:
            sx = range_result
            sy = y
            print(range_result, y)
            break
        if y % 100000 == 0:
            print(y, time.time() - start)
    tuning_frequency = 4000000 * sx + sy
    return tuning_frequency


def main():
    which_part = 2
    is_it_test = False

    if not is_it_test:
        input_file = "ad15.txt"
        the_row = 2000000
        upper_limit = 4000000
    else:
        input_file = "ad15-test.txt"
        the_row = 10
        upper_limit = 20

    input_strings = read_input(input_file)
    locations = get_locations(input_strings)

    if which_part == 1:
        result = find_beacon_positions(locations, the_row)
        print("y=", the_row, "on", result, "positions no beacon can exist")
    else:
        start = time.time()
        tuning_frequency = find_only_possible_point(locations, upper_limit, start)
        print("tuning frequency", tuning_frequency)
        end = time.time()
        print("it took me", end - start)


if __name__ == '__main__':
    main()
