import random





def main():

    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    #append_random_numbers(numbers)
    print(numbers)
    #append_random_numbers(numbers, 3)
    buuuuuut(numbers, 5)
    print(numbers)


()

def append_random_numbers(numbers_list, quantity=1):
    randomnumbers = [round(random.uniform(0, 101), 1) for _ in range(quantity)]
    numbers_list.extend(randomnumbers)
    
    ()

def buuuuuut(numbers_list, quantity=1):

    for _ in range(quantity):
        randomnumbers = round(random.uniform(0, 101), 1)
        numbers_list.append(randomnumbers)
        print(_)
        ()



main()
