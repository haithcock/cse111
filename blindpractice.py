numbers = list(range(1, 101))

for number in numbers:
    if number % 2  == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
'''
for number in numbers: 
    if (number % 5 == 0) and (number % 3 == 0):
        print(f"{number} is divisible by 3 and 5")
    elif number % 5 == 0:
        print(f"{number} is divisible by 5")
    elif number % 3 == 0:
        print(f"{number} is divisible by 3")
    elif number in numbers == 69:
        print("lmaooooo nice")
'''

for number in numbers:
    if number == 69:
       print("lmaoooo nice")
for number in numbers:
    if (number == 69) and (number % 3 == 0):
        print(f"{number} lmaooooo nice. Your number is also divisible by 3")
    elif (number % 5 == 0) and (number % 3 == 0):
        print(f"{number} is divisible by 3 and 5")
    elif number % 5 == 0:
        print(f"{number} is divisible by 5")
    elif number % 3 == 0:
        print(f"{number} is divisible by 3")
'''
foesmad = []
count = 1000     #<-A simple while loop
while count > 0:
    print(count)
    count -= 1
    if count % 3 == 0:
        print("hoes mad")
        foesmad.append(count)
        if count in foesmad:
            print("I don't care")
print("Liftoff")
'''