input_year = int(input())

output = "Ordinary"

if input_year % 4 == 0 and input_year % 100 != 0:
    output = "Leap"
elif input_year % 400 == 0:
    output = "Leap"

print(output)