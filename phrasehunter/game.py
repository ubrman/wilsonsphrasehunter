from phrasehunter.phrase import Phrase
import random

class Game:
    def __init__(self):
        self.missed = 0
        self.guesses = [" "]
        self.phrases = self.phrases = [
            Phrase("Vancouver Canucks"),
            Phrase("Calgary Flames"),
            Phrase("Winnipeg Jets"),
            Phrase("Toronto Maple Leafs"),
            Phrase("Montreal Canadians")
        ]
        self.active_phrase = None

    def get_random_phrase(self):
        return random.choice(self.phrases)
    
    def welcome(self):
        print("\n\n     =====================\n     Wilson's Phrase Hunter \n     ===================== \n Guess Between 5 Canadian Hockey Teams\n\n")
    
    def get_guess(self):
        user_input = input("Guess a letter: ")
        return user_input
    
    def start(self):
        self.welcome()
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
    
    def reset(self):
        """Resets game with current list of phrases."""
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
            
