import random

list = ['python', 'java', 'swift', 'javascript']  #Append any words in this list
word = random.choice(list)
score = {"won": 0, "lost": 0}

print('  --  --- Razmakhnin codes ---  --\n github.com/Razmakhninoff/Razmakhnin_Codes\n')

def play():
    print()
    print("-" * len(word))
    letters = []
    cword = word
    counter = 8
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    while counter > 0:
        x = input("Input a letter: ")
        if x in letters:
            if x in alphabet:
                print("You've already guessed this letter.")
        if x not in word:
            if x in alphabet:
                if x not in letters:
                    print("That letter doesn't appear in the word.")
                    counter -= 1
        print()
        letters.append(x)
        for i in cword:
            if i not in letters:
                cword = cword.replace(i, "-")
        if cword == word:
            print(f"You guessed the word {word}!\nYou survived!")
            score['won'] += 1
            break
        if counter > 0:
            print(cword)
        if counter == 0 and cword != word:
            print("You lost!")
            score['lost'] += 1
            break

        if x not in alphabet:
            if len(x) > 1 or len(x) < 1:
                print("Please, input a single letter.")
            elif x not in alphabet:
                print("Please, enter a lowercase letter from the English alphabet.")
            print()
        cword = word
    main()


def results():
    print(f"You won: {score['won']} times")
    print(f"You lost: {score['lost']} times")
    main()


def main():
    print('H A N G M A N')
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    choice = input()
    if choice == "play":
        play()
    if choice == "results":
        results()
    if choice == "exit":
        exit()


main()