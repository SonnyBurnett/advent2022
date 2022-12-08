def read_input():
    with open('ad9.txt') as f:
        input_list = [line.strip() for line in f]
    return input_list

#************************* Part 1 *******************************************************************


#************************* Part 2 *******************************************************************


#************************* Test *******************************************************************


def test_ad9():
    expected_outcome_1 = 0
    expected_outcome_2 = 0
    input_list = ["30373","25512","65332","33549","35390"]
    calculated_outcome = 0
    highest_scenic_score = 0
    if calculated_outcome == expected_outcome_1 and highest_scenic_score == expected_outcome_2:
        return True
    else:
        print("test failed")
        return False


#************************* Main *******************************************************************


def main():
    if test_ad9():
        input_list = read_input()


if __name__ == '__main__':
    main()

