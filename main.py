#step1

word_list = ["ardvark", "baboon", "camel"]

#randomly select a word

import random

chosen_word = random.choice(word_list)

#testing code
print(f'Psst, the solution is{chosen_word}.')

#for each letter in the chosen word ass a "_" to display
display = []
word_length = len(chosen_word)
#for letter in chosen_word:
 #   display+= "_"
#print (display)

#you can use range to add the underscores to display
for i in range(word_length):
    display+= "_"
print(display)

#using a while loop
#ask user to guess a letter
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

#loop through each position in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position} \n Current letter: {letter} \n Guessed letter: {guess}")
        if letter ==guess:
            display[position] = letter  
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
  
  
    
