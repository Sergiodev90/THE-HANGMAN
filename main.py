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
    letters_guessed = []
    lives = 6
    container = 0

    letter = ''

       
    print(chosen_word)
    
    while lives > 0 or "_" in guess_Word:
        

        if language == 'english':
            letter = input(f"\n word: {' '.join(guess_Word)} \n \n lives left: {lives} \n \n guess the word: ")
        elif language == 'español':
            letter  = input(f" \npalabra: {' '.join(guess_Word)}\n \n vidas restantes: {lives} \n \n adivina la palabra: ")

        if letter in letters_guessed and language == "english" :
            print(f" \n\n the letter '{letter}' is repeated")
            letter = input("please give me another letter ")
            continue

        elif letter in letters_guessed and language == "español":
            print(f"\n\n la letra '{letter} esta repetida'")
            letter = input("\n\n dame otra vez una letra que no este repetida => ")

        letters_guessed.append(letter)

        print(letters_guessed)

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
            end_game = True
            print("\n \n PERDISTE")
            print(f"\n\n la palabra fue => {chosen_word.upper()}")
            break

        elif lives == 0 and language == "english":
            print("\n \n YOU LOST")
            print(f"\n \n the word was => {chosen_word.upper()}")
            break

        if "_" not in guess_Word and language ==  'español':
            end_game = True
            print("\n \n GANASTE! ")
            break

        elif "_" not in guess_Word and language ==  "english":
            print("\n \n YOU WON ")
            break
    
        def tracks():
            
            if lives == 3:
                letter_to_reveal = ''
                if language == 'español':
                    print("te dare unas pistas")
                    for x in range(len(guess_Word)-1 -1 -1):
                        if guess_Word[x] == '_':
                            letter_to_reveal = chosen_word[x]
                            guess_Word = letter_to_reveal
                            break
                    print(f"Here's a hint '{letter_to_reveal}' is in the word")
        tracks()

        
   
    

if __name__ == "__main__":
     play_hangman()
