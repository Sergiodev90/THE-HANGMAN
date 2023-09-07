import random 

from hangman_art import logo,stages 
from Hangman_words import word_list,ad_list

print(logo)



# hacer una funcion que valide cual idioma desea el usuario y de ahi sacar las letras segun 

def select_language():
    language = input(" which lenguagues do you to choose, (es)ESPAÑOL or (en)ENGLISH => ").lower()
    while language not in ['es','en']:
        language = input("that languages isn't valid choose again => ")
    return language

language = select_language()


def play_hangman():

    words = list(word_list[language].keys())
    random_word = random.choice(words)
    guess_Word = ['_'] * len(random_word)
    meaning = word_list[language][random_word]['meaning']
    link = word_list[language][random_word]['link']
    letters_guessed = []
    lives_list = []
    lives = 6
    container = 0


    letter = ''

       
    print(random_word)
    
    while lives > 0 or "_" in guess_Word:
            
        lives_list.append(lives)
        print(lives_list)

        if language == 'en':
            letter = input(f"\n word: {' '.join(guess_Word)} \n \n lives left: {lives} \n \n guess the word: ")
        elif language == 'es':
            letter  = input(f" \npalabra: {' '.join(guess_Word)}\n \n vidas restantes: {lives} \n \n adivina la palabra: ")

        if letter in letters_guessed and language == "en" :
            print(f" \n\n the letter '{letter}' is repeated")
            letter = input("please give me another letter ")
            continue

        elif letter in letters_guessed and language == "es":
            print(f"\n\n la letra '{letter} esta repetida'")
            letter = input("\n\n dame otra vez una letra que no este repetida => ")

        letters_guessed.append(letter)

        print(letters_guessed)

        if len(letter) == 1 and letter.isalpha():
            if letter in random_word:
                for i in range(len(random_word)):
                    if letter == random_word[i]:
                        guess_Word[i] = letter    
                    
                       


                            
            elif language == 'es' and letter not in random_word:
                lives -= 1
                print(stages[lives])
                print("palabra incorrecta")
                
        

            else:
                lives -= 1
                print(stages[lives])
                print("\n \n no match")

                
            

        elif language == 'es' and len(letter) != 1 and letter.isalpha():
            letter = input("dame de nuevo la letra porfavor solo una recuerda bien => ")
        else:
            letter = input("give me a letter again just one => ")
            
        if lives == 0 and language == 'es':
            end_game = True
            print("\n \n PERDISTE")
            print(f"\n\n la palabra fue => {random_word.upper()}")
            break

        elif lives == 0 and language == "en":
            print("\n \n YOU LOST")
            print(f"\n \n the word was => {random_word.upper()}")
            break

        elif "_" not in guess_Word and language ==  'es':
            end_game = True
            print("\n \n GANASTE! ")
            break

        elif "_" not in guess_Word and language ==  "en":
            print("\n \n YOU WON ")
            break
        
        # def one_more_live(letter_to_reveal):
        #     lives_list_onemore= []
        #     letter_to_reveal = ''
        #     lives_list_onemore.append(lives)
        #     print(lives_list_onemore)

           
      
        #     if language == 'es':
        #             if letter_to_reveal != '':
        #                 print("te dare la prima letra")
        #             for i in range(len(guess_Word )-1 ,-1 ,-1):
        #                 if guess_Word[i] == '_':
        #                     letter_to_reveal = chosen_word[i]
        #                     guess_Word[i] = letter_to_reveal
                        
        #                 if lives in lives_list_onemore:
        #                     print("hola")
    
        #             if letter_to_reveal != '':          
        #                 print(f"Here's a hint '{letter_to_reveal.upper()}' is in the word")
            
        def selection_sort():
            n = len(lives_list)
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    if lives_list[j] < lives_list[min_idx]:
                        min_idx = j
                lives_list[i], lives_list[min_idx] = lives_list[min_idx], lives_list[i]

            print(lives_list)

        def tracks(lives):
            new_live = lives

        
            if language == 'es':
                if First_letter_to_reveal != '':
                    print("te dare la prima letra")

                    for item in lives_list:
                        if item == new_live:
                            count = count + 1

                    for i in range(len(guess_Word )-1 ,-1 ,-1):
                        if guess_Word[i] == '_':
                            First_letter_to_reveal = random_word[i]
                            guess_Word[i] = First_letter_to_reveal
                        if  new_live in lives_list:
                            break

                    
                    if First_letter_to_reveal != '':          
                        print(f"Here's a hint '{First_letter_to_reveal.upper()}' is in the word")

        if lives == 3:
            tracks(3)

            # if lives == 3 :
            #     Second_letter_to_reveal = ''
            #     lives_list.append(lives)
            #     if language == "es":
            #         print("te dare otra pista ")
            #         for y in range(len(guess_Word) -1 -1 -1):
            #             if guess_Word[y] == '_':
            #                 Second_letter_to_reveal = chosen_word[y]
            #                 guess_Word[y] = Second_letter_to_reveal

            #                 if lives == lives_list:
            #                     break

            #         print(f"aqui esta una letra '{Second_letter_to_reveal.upper()}' en la palabra secreta ")

            # if lives == 2: 
            #             Third_letter_to_reveal = ''
            #             lives_list.append(lives)
            #             if language == "es":
            #                 print("te dare la ultima pista ")
            #             for y in range(len(guess_Word) -1 -1 -1):
            #                 if guess_Word[i] == '_':
            #                     Third_letter_to_reveal = chosen_word[i]
            #                     guess_Word[i] = Third_letter_to_reveal
                                
            #                     if lives == lives_list:
            #                         break
                                

            #             print(f"aqui esta una letra '{Third_letter_to_reveal.upper()}' en la palabra secreta ")


        def AnotherChange():
            lives_Riddle = 2
            response_word = ''
            chosen_word_riddle = random.choice(list(ad_list[language].items()))
            print(chosen_word_riddle)
            if lives == 1 :
                response =  input(f"al parecer te has quedado con solo una vida, te dare una segunda oportunidad pero si logras completar mi adivinanza, recuerda solo tienes {lives_Riddle} (s)SI / (n)NO => ")
                if response == 's' and len(response) == 1 and response.isalpha():
                    for x,y in chosen_word_riddle:
                        print(y)
                        response_word = input("justo aqui la respuesta")
                        if response_word == x:
                            print("lo haz logrado ok te dare otra letra")




        AnotherChange()

        selection_sort()

    

if __name__ == "__main__":
     play_hangman()
