text_file = open("ad6.txt", "r")
message_string = text_file.read()
text_file.close()
distinct_characters = 14
c = 0
while True:
    if len(message_string[c:c+distinct_characters]) == len("".join(set(message_string[c:c+distinct_characters]))):
        print(c+distinct_characters, message_string[c:c+distinct_characters])
        break
    c+=1
