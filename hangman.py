import random
import string

answer = input('Type "play" to play the game, "exit" to quit: ')

while answer != "exit":
    if answer == "play":
        print("H A N G M A N")
        print()
        words = ['python', 'java', 'kotlin', 'javascript']
        alphabet = set(string.ascii_lowercase)

        word = words[int(random.randint(0, len(words) - 1))]
        letters_left = set(word)
        used_letters = set()
        hint = "-" * len(word)
        print(hint)
        lives = 8
        while lives > 0:
            print()
            print(hint)

            guess = input("Input a letter: ")
            if guess in used_letters:
                print("You already typed this letter")
            elif len(guess) != 1:
                print("You should input a single letter")
                continue;
            elif guess not in alphabet:
                print("It is not an ASCII lowercase letter")
                continue;
            elif guess in letters_left:
                temp = list(hint)
                for j in range(len(word)):
                    if word[j] == guess:
                        temp[j] = guess
                hint = "".join(temp)
                letters_left.discard(guess)
            else:
                print("No such letter in the word")
                lives -= 1
            if len(letters_left) == 0:
                print("You guessed the word!")
                print("You survived!")
                break
            used_letters.add(guess)
        else:
            print("You are hanged!")
        answer = input('Type "play" to play the game, "exit" to quit: ')
    else:
        answer = input('Type "play" to play the game, "exit" to quit: ')
