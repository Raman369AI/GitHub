import random
import hangman_words
import hangman_art

print(hangman_art.logo)
list=hangman_words.word_list
chosen_word = random.choice(list)
print(chosen_word)
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while display.count('_')!=0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print(f"You already guessed the letter {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"one more oppurtunity lost, lives remaining {lives-1}")
        lives -= 1
        if lives == 0:
            print("You lose.")
            print(hangman_art.stages[lives])
            break

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        print("You win.")
        break

    print(hangman_art.stages[lives])
   