lcc_word = input()

temp = []

for i in lcc_word:
    if i.isupper():
        temp.append("_" + i.lower())
    else:
        temp.append(i)

print(''.join(temp))
