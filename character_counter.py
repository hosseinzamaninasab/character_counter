from pprint import pprint
message = input("input the text:\n")

count = {}
for character in message.upper():
    count.setdefault(character, 0)
    count[character] += 1

pprint(count)
