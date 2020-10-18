from phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.guesses = [" "]
        self.phrases = []
        self.active_phrase = None
    
    # Game gets set up by user entering phrases  
    def create_phrases(self):
        while len(self.phrases) < 5:
            try:
                entered = input("Please enter your phrase: ")
                if " " in entered and entered != " " and any(str.isdigit(l) for l in entered) == False:
                    object_var = Phrase(entered)
                    self.phrases.append(object_var)
                    continue
                else:
                    print("Invalid input. Try Again!")
                    continue
            except ValueError:
                continue

    
    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("\n\n =====================\n Wilson's Phrase Hunter \n ===================== \n\n")
    
    def get_guess(self):
        user_input = input("Take a guess: ")
        return user_input
    
    def start(self):
        self.welcome()
        self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"\nNumber of tries = {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            if len(user_guess) == 1 and user_guess.isdigit() == False:
                self.guesses.append(user_guess)
                if not self.active_phrase.check_guess(user_guess):
                    print("Bummer!")
                    self.missed += 1
                else:
                    print("Yay!")
            else:
                print("Invalid input (and wasted a turn). Try again!")
                self.missed += 1
                continue
        self.active_phrase.display(self.guesses)
        self.game_over()
    
    def game_over(self):
        if self.missed == 5:
            print("5 guesses maximum. You've lost!")
        else:
            print("Congratulations. You won!")
        self.play_again()
    
    # Resetting attributes so game can start again
    def reset(self):
        self.missed = 0
        self.guesses = [" "]
        self.active_phrase = None
        
    # Asking user if they want to play again or to quit. Resetting active phrase and attributes if they do, or exiting if they want to quit. 
    def play_again(self):
        self.ask_user = None
        while self.ask_user != "y" and self.ask_user != "n":
            self.ask_user = input("Do you want to play again? (Y/N) ")
            if self.ask_user.lower() == "y":
                self.reset()
                self.active_phrase = self.get_random_phrase()
                while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
                    print(f"\nNumber of tries = {self.missed}")
                    self.active_phrase.display(self.guesses)
                    user_guess = self.get_guess()
                    if len(user_guess) == 1 and user_guess.isdigit() == False:
                        self.guesses.append(user_guess)
                        if not self.active_phrase.check_guess(user_guess):
                            print("Bummer!")
                            self.missed += 1
                        else:
                            print("Yay!")
                    else:
                        print("Invalid input (and wasted a turn). Try again!")
                        self.missed += 1
                        continue
                self.active_phrase.display(self.guesses)
                self.game_over()
            elif self.ask_user.lower() == "n":
                print("Thanks for playing!")
            
