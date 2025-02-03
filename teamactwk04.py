import random

listofwords=["cat", "hat", "dog", "kite", "fight", "right", "light"]                               
    



def main():

    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)#only one argument
    print(numbers)
    append_random_numbers(numbers, 3)#has two arguments and passes 3 arguments
    #buuuuuut(numbers, 5)
    print(numbers)
    append_random_words(listofwords, 4)

    print(listofwords) # Displays the appended random word including the words list

()

def append_random_numbers(numbers_list, quantity=1): #here we have a default value. 
    randomnumbers = [round(random.uniform(0, 101), 1) for _ in range(quantity)]
    numbers_list.extend(randomnumbers)
    
    
    ()
    
def buuuuuut(numbers_list, quantity=1):


    for _ in range(quantity):
        randomnumbers = round(random.uniform(0, 101), 1)
        numbers_list.append(randomnumbers)
        print(_)
        ()







def append_random_words(words_list, quantity=1): #Has two parameters: a list named words_list and an integer named quantity. The parameter quantity has a default value of 1 
    for _ in range(quantity):
        words_length = len(words_list)
        last_index = words_length - 1
        random_index = random.randint(0, last_index)
        random_word = words_list[random_index]
        words_list.append(random_word)

    # print(words_list)

    # return words_list.append(random_word)
    #for _ range(quantity)


    ()


main()

