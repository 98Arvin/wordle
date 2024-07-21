import random

def wordle():
    random_words = ["snake", "slave", "catch", "match", "binge", "blown", "black", "music", "dance", "query", "funny", "slash", "names", "users", "parts", "paths", "plank", "clark", "power", "flown", "clown", "shows", "shown", "sword", "grass", "grape", "petty", "lower", "sweet"]
    counter = 0
    chosen_word = random.choice(random_words)
    guessed = []

    # print(f"The chosen word: {chosen_word}")

    while counter < 7:
        while len(guess := input(f"Guess: ")) > 5:
            print("TOO LONG")
        for char in guess:
            if char in chosen_word:
                if char not in guessed:
                    guessed.append(char)
        joined = "".join(sorted(guessed))
        answer = "".join(sorted(chosen_word))
        print(f"GUESSED: {joined}")
        # print(f"ANSWER: {chosen_word}")
        
        if joined == answer:
            return print("WINNER!!!")
        else:
            counter += 1
    return print("LOSERRRRRRRRRR!")

wordle()
