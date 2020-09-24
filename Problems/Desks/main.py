class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

total = class_1 + class_2 + class_3

if class_1 % 2 == 1:
    class_1 += 1
if class_2 % 2 == 1:
    class_2 += 1
if class_3 % 2 == 1:
    class_3 += 1

print(int(class_1 / 2) + int(class_2 / 2) + int(class_3 / 2))
