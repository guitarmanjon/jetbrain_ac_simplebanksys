dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]

word = input()
output = "Incorrect"
for x in dictionary:
    if word == x:
        output = "Correct"
        break

print(output)