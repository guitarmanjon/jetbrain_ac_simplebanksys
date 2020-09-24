deposit = float(input())

count = 0

while deposit < 700000:
    deposit += (0.071 * deposit)
    count += 1

print(count)
