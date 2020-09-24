test_no = int(input())
count = 2
prime = True

if test_no <= 1:
    prime = False

while prime and count < test_no:
    if test_no % count == 0:
        prime = False
        break
    count += 1

if prime:
    print("This number is prime")
else:
    print("This number is not prime")
