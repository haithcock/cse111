import random



def main():
    quantity_input = input(
        "Do you want sentences with plural nouns? \n"
        "Press: 1 for plural nouns,\n"
        "Press: 2 for singular nouns.\n")
    quantity = int(quantity_input)

    tense_input = input("\nWhat is the tense? \nPress: 1 for past tense,\nPress: 2 for present tense,\nPress: 3 for future tense.\n")
    tense = int(tense_input)
()
main()


def make_sentence():
    ()

def get_determiner():
  
  def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise, this function will return
    either "some", "many", or "the".
    Parameter:
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise, this
            function will return a determiner for a plural
            noun.
    Return:
        A randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    return random.choice(words)
# Example usage
print(get_determiner(1))  # Could return "a", "one", or "the"
print(get_determiner(5))  # Could return "some", "many", or "the"

()

def get_noun(quantity):


    if quantity == 1: 
        nounwords = ["bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"]
    else:
        nounwords = ["birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"]
        
    return random.choice(nounwords)
    ()

def get_verb(quantity, tense):
    futuretense = [      "will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"]
    
    if quantity == 1:
        presenttense = ["drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"]
    else:
        pluralpresenttense = ["drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"]
    
    if tense is 1:

        pastverbs = [ "drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"]
    
    if tense is 2:()





















