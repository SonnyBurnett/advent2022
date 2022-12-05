with open('advent1.txt') as f:
    input_list = [line.strip() for line in f]
result = []
tmp_num = 0
for x in input_list:
    if x != "":
        tmp_num+=int(x)
    else:
        result.append(tmp_num)
        tmp = 0
result.sort(reverse=True)
print(result[0])
print(result[0]+result[1]+result[2])
