#3a
max_number = int(input("Up to which number do we need to check ?"))
for number in range(max_number):
    if (number % 2 == 0):
        print(number)
#3b
for number in range(10,20):
    print(number)
#3c
for number in range(50, 101, 5):
    if(number == 75):
        continue
    print(number)
