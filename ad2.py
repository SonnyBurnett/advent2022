with open('rockpaper.txt') as f:
    input_list = [line.strip() for line in f]
scores1 = {"A X": 4, "A Y": 8, "A Z": 3, "B X" : 1, "B Y" : 5, "B Z" : 9, "C X": 7, "C Y": 2, "C Z": 6}
scores2 = {"A X": 3, "A Y": 4, "A Z": 8, "B X" : 1, "B Y" : 5, "B Z" : 9, "C X": 2, "C Y": 6, "C Z": 7}
print(sum([scores1.get(i) for i in input_list]), sum([scores2.get(i) for i in input_list]))
