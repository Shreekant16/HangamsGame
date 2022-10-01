from data import names
from arts import stages, logo
import random

print(logo)
lives = 6
chosen_name = random.choice(names)
word_length = len(chosen_name)
display = []
for i in range(word_length):
    display += '_'
print("YOU HAVE 6 LIVES ONLY")
print(display)
end = False
while not end:
    guess = input("Guess the letter : ")
    for position in range(word_length):
        letter = chosen_name[position]
        if guess == letter:
            display[position] = letter
    if '_' not in display:
        print("You won the game")
        end = True
    if guess not in chosen_name:
        print(f"that's incorrect you have {lives} lives")
        lives -= 1
        if lives == 0:
            end = True
            print("You are out of lives")
    print(f'{"".join(display)}')
    print(stages[lives])

    