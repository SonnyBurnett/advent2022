
class Monkey:
    def __init__(self, number, items, operation, op_num, test, test_true, test_false):
        self.number = number
        self.items = items
        self.operation = operation
        self.op_num = op_num
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.number_of_inspections = 0

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

    def get_bored(self, item_num):
        new_num = int(item_num / 3)
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

    def catch_item(self, item_number):
        self.items.append(item_number)

    def get_items(self):
        return self.items

    def throw_items_from_list(self, items_to_throw):
        for item in items_to_throw:
            self.throw_item(item)

    def print_monkey(self):
        print("number   : ", self.number)
        print("items    : ", self.items)
        print("operation: ", self.operation)
        print("op number: ", self.op_num)
        print("test     : ", self.test)
        print("true     : ", self.test_true)
        print("false    : ", self.test_false)
        print()

    def print_short_monkey(self):
        print("Monkey   : ", self.number, ":", self.items, "inspections:", self.number_of_inspections)

    def get_number_of_inspections(self):
        return self.number_of_inspections


#***************************************** part 1 ***************************************************************

def create_monkeys():
    monkey_list = []
    monkey_list.append(Monkey(0,[93, 54, 69, 66, 71],"*",3,7,7,1))
    monkey_list.append((Monkey(1,[89, 51, 80, 66],"*",17,19,5,7)))
    monkey_list.append(Monkey(2,[90, 92, 63, 91, 96, 63, 64],"+",1,13,4,3))
    monkey_list.append(Monkey(3,[65, 77],"+",2,3,4,6))
    monkey_list.append(Monkey(4, [76, 68, 94],"**",2,2,0,6))
    monkey_list.append(Monkey(5,[86, 65, 66, 97, 73, 83],"+",8,11,2,3))
    monkey_list.append(Monkey(6,[78],"+",6,17,0,1))
    monkey_list.append(Monkey(7,[89, 57, 59, 61, 87, 55, 55, 88],"+",7,5,2,5))
    return monkey_list


def create_test_monkeys():
    monkey_list = []
    monkey_list.append(Monkey(0,[79,98],"*",19,23,2,3))
    monkey_list.append((Monkey(1,[54, 65, 75, 74],"+",6,19,2,0)))
    monkey_list.append(Monkey(2,[79, 60, 97],"**",2,13,1,3))
    monkey_list.append(Monkey(3,[74],"+",3,17,0,1))
    return monkey_list


def play_round(monkey_list):
    for monkey in monkey_list:
        monkey_item_list = monkey.get_items()
        throw_items = []
        for item in monkey_item_list:
            item_num_after_inspect = monkey.inspect_item(item)
            item_num_after_bored = monkey.get_bored(item_num_after_inspect)
            throw_to_monkey = monkey.test_item(item_num_after_bored)
            throw_items.append(item_num_after_bored)
            monkey_list[throw_to_monkey].catch_item(item_num_after_bored)
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
    return business_list[0]*business_list[1]




#************************* Part 2 *******************************************************************

#************************* Main *******************************************************************


def main():

    #monkey_list = create_test_monkeys()
    monkey_list = create_monkeys()
    for round in range(1,21):
        play_round(monkey_list)
    print_all_monkeys(monkey_list, "short")
    print("Level of monkey business after 20 rounds:", calculate_level_of_monkey_business(monkey_list))


if __name__ == '__main__':
    main()

