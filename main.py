import random 
from hangman_art import logo,stages 
from Hangman_words import word_list

print(logo)



# hacer una funcion que valide cual idioma desea el usuario y de ahi sacar las letras segun 

def select_language():
    language = input(" which lenguagues do you to choose, español or english => ").lower()
    while language not in ['español','english']:
        language = input("that languages isn't valid choose again => ")
    return language

language = select_language()


def play_hangman():
    chosen_word = random.choice(word_list[language])
    guess_Word = ['_'] * len(chosen_word)
    end_game = False
    lives = 6

    letter = ''

       
    print(chosen_word)
    
    while lives > 0 or "_" in guess_Word:
        if language == 'english':
            letter = input(f"\n word: {' '.join(guess_Word)} \n \n lives left: {lives} \n \n guess the word: ")
        elif language == 'español':
            letter  = input(f" \n”palabra: {' '.join(guess_Word)}\n \n vidas restantes: {lives} \n \n adivina la palabra: ")

        if len(letter) == 1 and letter.isalpha():
            if letter in chosen_word:
                for i in range(len(chosen_word)):
                    if letter == chosen_word[i]:
                        guess_Word[i] = letter
                
            elif language == 'español' and letter not in chosen_word:
                lives -= 1
                print(stages[lives])
                print("palabra incorrecta")

            else:
                lives -= 1
                print(stages[lives])
                print("\n \n no match")
                
        elif language == 'español' and len(letter) != 1 and letter.isalpha():
            letter = input("dame de nuevo la letra porfavor solo una recuerda bien => ")
        else:
            letter = input("give me a letter again just one => ")
            
        if lives == 0 and language == 'español':
            print(chosen_word)
            end_game = True
            print("\n \n PERDISTE")
            break

        if "_" not in guess_Word and 'español':
            end_game = True
            print("\n \n GANASTE! ")
            break

def main():
    play_hangman()


if __name__ == "__main__":
    main()