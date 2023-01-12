import math


class Monkey:
    def __init__(self, number, items, operation, op_num, test, test_true, test_false, item_numbers):
        self.number = number
        self.items = items
        self.operation = operation
        self.op_num = op_num
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.number_of_inspections = 0
        self.item_numbers = item_numbers

    def inspect_item(self, item_num):
        if self.operation == "*":
            new_num = item_num * self.op_num
        elif self.operation == "**":
            new_num = item_num * item_num
        elif self.operation == "+":
            new_num = item_num + self.op_num
        else:
            new_num = item_num
        item_index = self.items.index(item_num)
        self.items[item_index] = new_num
        self.number_of_inspections+=1
        return new_num

    def get_bored(self, item_num, bored_index):
        new_num = int(item_num / bored_index)
        item_index = self.items.index(item_num)
        self.items[item_index] = new_num
        return new_num

    def test_item(self, item_num):
        if item_num % self.test == 0:
            return self.test_true
        else:
            return self.test_false

    def throw_item(self, item_number):
        self.items.remove(item_number)

    def catch_item(self, item_number, item_id):
        self.items.append(item_number)
        self.item_numbers.append(item_id)

    def get_items(self):
        return self.items

    def get_monkey_num(self):
        return self.number

    def throw_items_from_list(self, items_to_throw):
        for item in items_to_throw:
            self.throw_item(item)

    def print_monkey(self):
        print("number   : ", self.number)
        print("items    : ", self.items)
        print("item nums: ", self.item_numbers)
        print("operation: ", self.operation)
        print("op number: ", self.op_num)
        print("test     : ", self.test)
        print("true     : ", self.test_true)
        print("false    : ", self.test_false)
        print()

    def print_short_monkey(self):
        print("Monkey   : ", self.number, ":", self.number_of_inspections)

    def get_number_of_inspections(self):
        return self.number_of_inspections

    def get_index_of_item_num(self, item_num):
        return self.items.index(item_num)

    def get_item_id_on_index(self, item_index):
        return self.item_numbers[item_index]

    def divide_item(self, item, divisor):
        item_index = self.items.index(item)
        value = self.items[item_index]
        self.items[item_index] = value % divisor

    def get_division_num(self):
        return self.test


#***************************************** part 1 ***************************************************************

def create_monkeys():
    monkey_list = []
    monkey_list.append(Monkey(0,[93, 54, 69, 66, 71],"*",3,7,7,1,[1,2,3,4,5]))
    monkey_list.append((Monkey(1,[89, 51, 80, 66],"*",17,19,5,7,[6,7,8,9])))
    monkey_list.append(Monkey(2,[90, 92, 63, 91, 96, 63, 64],"+",1,13,4,3,[10,11,12,13,14,15,16]))
    monkey_list.append(Monkey(3,[65, 77],"+",2,3,4,6,[17,18]))
    monkey_list.append(Monkey(4, [76, 68, 94],"**",2,2,0,6,[19,20,21]))
    monkey_list.append(Monkey(5,[86, 65, 66, 97, 73, 83],"+",8,11,2,3,[22,23,24,25,26,27]))
    monkey_list.append(Monkey(6,[78],"+",6,17,0,1,[28]))
    monkey_list.append(Monkey(7,[89, 57, 59, 61, 87, 55, 55, 88],"+",7,5,2,5,[29,30,31,32,33,34,35,36]))
    return monkey_list


def create_test_monkeys():
    monkey_list = []
    monkey_list.append(Monkey(0,[79,98],"*",19,23,2,3,[1,2]))
    monkey_list.append(Monkey(1,[54, 65, 75, 74],"+",6,19,2,0,[3,4,5,6]))
    monkey_list.append(Monkey(2,[79, 60, 97],"**",2,13,1,3, [7,8,9]))
    monkey_list.append(Monkey(3,[74],"+",3,17,0,1,[10]))
    return monkey_list


def play_round(monkey_list, bored_index):
    for monkey in monkey_list:
        monkey_item_list = monkey.get_items()
        throw_items = []
        throw_indexes = []
        for item in monkey_item_list:
            item_num_after_inspect = monkey.inspect_item(item)
            if bored_index == 3:
                item_num_after_bored = monkey.get_bored(item_num_after_inspect, bored_index)
            else:
                item_num_after_bored = item_num_after_inspect
            throw_to_monkey = monkey.test_item(item_num_after_bored)
            item_index = monkey.get_index_of_item_num(item_num_after_bored)
            item_id = monkey.get_item_id_on_index(item_index)
            throw_items.append(item_num_after_bored)
            throw_indexes.append(item_index)
            monkey_list[throw_to_monkey].catch_item(item_num_after_bored, item_id)
        monkey.throw_items_from_list(throw_items)


def print_all_monkeys(monkey_list, report_type):
    for monkey in monkey_list:
        if report_type == "short":
            monkey.print_short_monkey()
        else:
            monkey.print_monkey()
    print()


def calculate_level_of_monkey_business(monkey_list):
    business_list = []
    for monkey in monkey_list:
        business_list.append(monkey.get_number_of_inspections())
    business_list.sort(reverse=True)
    print(business_list[0],business_list[1])
    return business_list[0]*business_list[1]

#************************* Part 2 *******************************************************************


def multiply_all_division_numbers(monkey_list):
    result = 1
    for monkey in monkey_list:
        result*=monkey.get_division_num()
    return result


def divide_all_items(monkey_list, divisor):
    for monkey in monkey_list:
        item_list = monkey.get_items()
        for item in item_list:
            monkey.divide_item(item, divisor)


#************************* Main *******************************************************************


def main():

    #monkey_list = create_test_monkeys()
    monkey_list = create_monkeys()
    bored_index = 3
    for round in range(1,21):
        play_round(monkey_list, bored_index)
    print("************ part 1 ************")
    print()
    print_all_monkeys(monkey_list, "short")
    print("Level of monkey business after 20 rounds:", calculate_level_of_monkey_business(monkey_list))
    print()

    print("************ part 2 ************")
    print()
    bored_index = 1
    monkey_list = create_monkeys()

    modulo_num = multiply_all_division_numbers(monkey_list)
    print("modulo num", modulo_num)
    print()
    for round in range(1, 10001):
        play_round(monkey_list, bored_index)
        divide_all_items(monkey_list, modulo_num)

    print_all_monkeys(monkey_list, "short")
    print("Level of monkey business after 10000 rounds:", calculate_level_of_monkey_business(monkey_list))


if __name__ == '__main__':
    main()
