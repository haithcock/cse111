# Example 1
"""
def main():
    numbers = [89, 90, 70, 90, 93, 48, 54]
    total = 0
    for x in numbers:
        total += x
    average = total / len(numbers)
    print(f"average: {average:.4f}")       #This is an example in python of how we use declarative programming to calculate the average from a set of numbers
# Call main to start this program.
if __name__ == "__main__":
    main()
"""
"""
    
CLASS NOTES:
When we use declarative programming 
to program a computer, we do not focus on the 
process or steps to accomplish a task, 
but rather we focus on what we want
 from the task, or in other words,
 we focus on the desired result.
 Continuing the example of the
   average, with declarative programming, 
 we focus on exactly what numbers we want
   averaged and tell the computer 
   to compute that average for us. 
 SQL is a declarative programming 
 language used with relational databases.
 Example 2 contains SQL code that causes the computer 
 to compute the average of a column of numbers. 
    
"""

"""
    MY NOTES:
    To me this sounds like in python we 
    will run code line by line versus as a 
    whole but I am still unsure. It seems 
    declarative programming is also within
    python but I do not know to what extent. 
    For instance declaring variables like:
    "myvariable = "fun" /a string variable
    my_2nd_variable = "2" /an int variable."
    if I had to guess is like declariative 
    programming. The notes are drawing 
    comparrisons to SQL where that is an
    entire declarative language. Which if I 
    had to infer, also makes sense. In SQL
    you are establishing relationships 
    between things in a schema between tables,
    then you are also calculating various maths
    when coloumns have their own numerical values.
"""


def main():

    

    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"{fruit_list}")
    fruit_list.append("orange")
    print(f"{fruit_list}")
    number_of_items = len(fruit_list)
    print(f"The list contains {number_of_items} items.")
    appleindex = fruit_list.index("apple")
    print(f"the location of 'apple' is {appleindex}")
    fruit_list.remove("banana")
    print(f"{fruit_list}")
    lastlistitem = fruit_list[-1]
    print(f"{lastlistitem}")
    print(f"{fruit_list}")
    #fruit_list.remove([])
    #print(f"{fruit_list}")
if __name__ == "__main__":

    main()