class Phrase:
    def __init__(self, wisdom):
        self.wisdoms = wisdom.lower()
    
    def display(self, guesses):
        for letters in self.wisdoms:
            if letters in guesses:
                print(f"{letters}", end=" ")
            else: 
                print("_", end=" ")
        print("\n")
    
    def check_guess(self, guess):
        if guess in self.wisdoms:
            return True
        else:
            return False

    def check_complete(self, guesses):
        for letter in self.wisdoms:
            if letter in guesses:
                continue
            else:
                return False
        return True

            
