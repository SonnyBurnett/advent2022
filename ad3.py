with open('ad3.txt') as f:
    input_list = [line.strip() for line in f]

common_list = [ord(''.join(set(x[:len(x)//2]).intersection(x[len(x)//2:]))) for x in input_list]
priority_list = [x-96 if x > 90 else x-38 for x in common_list]
print(sum(priority_list))

badge_list = []
counter = 0
while counter < len(input_list)-2:
    badge_num = set.intersection(*map(set,[input_list[counter],input_list[counter+1],input_list[counter+2]]))
    badge_list.append(ord(str(list(badge_num))[2]))
    counter+=3
new_priority_list = [x-96 if x > 90 else x-38 for x in badge_list]
print(sum(new_priority_list))