with open('ad4.txt') as f:
    inputlist = [line.strip() for line in f]
new_list = [x.replace("-", ",").split(',') for x in inputlist]
print(sum([1 for y in new_list if int(y[2]) >= int(y[0]) and int(y[3]) <= int(y[1]) or
           int(y[0]) >= int(y[2]) and int(y[1]) <= int(y[3]) ]))

print(sum([1 for y in new_list if
           int(y[0]) >= int(y[2]) and int(y[0]) <= int(y[3]) or
           int(y[1]) <= int(y[3]) and int(y[1]) >= int(y[2]) or
           int(y[2]) >= int(y[0]) and int(y[2]) <= int(y[1]) or
           int(y[3]) >= int(y[0]) and int(y[3]) <= int(y[1])
           ]))