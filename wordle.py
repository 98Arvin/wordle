import random, time

def wordle():
    random_words = ["snake", "slave", "catch", "match", "binge", "blown", "black", "music", "dance", "query", "funny", "slash", "names", "users", "parts", "paths", "plank", "clark", "power", "flown", "clown", "shows", "shown", "sword", "grass", "grape", "petty", "lower", "sweet"]
    counter = 1
    chosen_word = random.choice(random_words)
    guessed = []
    start_time = time.time()

    print("=>= =================CONTAINDLE ================== =<=")
    print("=>= YOUR STINT MUST CONTAIN ALL THE LETTERS TO WIN =<=")
    print()

    while counter < 11:
        while len(guess := input(f"→ ")) != 5:
            print("Has to be 5 chars")
        for char in guess:
            if char in chosen_word:
                if char not in guessed:
                    guessed.append(char)

        joined = "".join(sorted(guessed))
        answer = "".join(sorted(set(chosen_word)))

        print(f"GUESS {counter}/10 → {joined.upper()}")
        
        if joined == answer:
            end_time = time.time()
            elapsed_time = end_time - start_time
            return print(f">{chosen_word.upper()}< IS INDEED THE CORRECT WORD || YOU HAD {10 - counter} GUESS(ES) REMAINING || TIME USED: {elapsed_time:.2f} SECONDS")
        else:
            counter += 1
            
    return print(f"WRONG ❌ The answer was {chosen_word.upper()}!")

wordle()
