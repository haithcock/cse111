import os
import sys

class SpellingHelper:
    def __init__(self, words):
        self.words = words
        self.current_word = None
        self.display_word = []

    def set_word(self, word):
        self.current_word = word
        self.display_word = ['_'] * len(word)

    def reveal_letters(self):
        import random
        indices = [i for i, letter in enumerate(self.display_word) if letter == '_']
        if indices:
            idx = random.choice(indices)
            self.display_word[idx] = self.current_word[idx]

    def clear_screen(self):
        if os.name == 'nt':  # for Windows
            os.system('cls')
        else:  # for macOS and Linux
            os.system('clear')

    def play(self):
        print("Welcome to the Spelling Helper!\n")
        while True:
            print("Here is the list of words to practice:")
            for idx, word in enumerate(self.words):
                print(f"{idx + 1}. {word}")
            choice = input("Enter a number to choose a word from the list, or type a new word: ").strip()
            self.clear_screen()
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.words):
                    self.set_word(self.words[index])
                else:
                    print("Invalid number, try again.")
                    continue
            else:
                if not choice:
                    print("No input detected, exiting.")
                    sys.exit(0)
                self.set_word(choice)
                if choice not in self.words:
                    print("Adding new word to practice list.")
                    self.words.append(choice)
            
            tries = 0
            while '_' in self.display_word:
                print("Current word: " + ''.join(self.display_word))
                input("Press enter to reveal a letter...")
                self.reveal_letters()
                tries += 1
            print("\nGreat! The word is: " + self.current_word)
            print(f"It took you {tries} tries to reveal the full word.\n")
            cont = input("Do you want to continue? (yes/no): ").lower()
            self.clear_screen()
            if cont != "yes":
                print("Thanks for using the Spelling Helper!")
                break

# Example usage:
if __name__ == "__main__":
    words_list = ["accommodate", "definitely", "separate", "occasionally", "necessary", "privilege", 
                  "conscience", "rhythm", "embarrass", "maintenance", "permanent"]
    game = SpellingHelper(words_list)
    game.play()
