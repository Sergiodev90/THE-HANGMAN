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
    global lives,lives_list,response

    words = list(word_list[language].keys())

    random_word = random.choice(words)
    guess_Word = ['_'] * len(random_word)
    for i,x in enumerate(random_word):
        if x == ' ':
            guess_Word[i] = ''

    meaning = word_list[language][random_word]['meaning']
    link = word_list[language][random_word]['link']
    save_guess_word = ''
    letters_guessed = []
    lives_list = []
    lives = 6
    letter = ''
    lives_Riddle = 2
    response = ''
    number_range = 1
    keys = list(ad_list[language].keys())
    random_keys = []
    random_values = []
    secuencia_2_despues_de_3 = []
    secuencia_3_despues_de_2 = []

    # print(random_word)
    
    while lives > 0 or "_" in guess_Word:
            
        lives_list.append(lives)

        if language == 'en':
            letter = input(f"\n {meaning} \n \n word: {' '.join(guess_Word)} \n \n lives left: {lives} \n \n guess the word: ")
        elif language == 'es':
            letter  = input(f"\n {meaning} \n \n palabra: {' '.join(guess_Word)}\n \n vidas restantes: {lives} \n \n adivina la palabra: ")

        if letter in letters_guessed and language == "en" :
            print(f" \n\n the letter '{letter}' is repeated")
            letter = input("please give me another letter ")
            continue

        elif letter in letters_guessed and language == "es":
            print(f"\n\n la letra '{letter} esta repetida'")
            letter = input("\n\n dame otra vez una letra que no este repetida => ")

        letters_guessed.append(letter)


        if len(letter) == 1 and letter.isalpha():
            if letter in random_word:
                for i in range(len(random_word)):
                    if letter == random_word[i]:
                        guess_Word[i] = letter

             



                            
            elif language == 'es' and letter not in random_word:
                lives -= 1
                print(f''' 
                                {stages[lives]}
                        ''')
                print("\n \n palabra incorrecta")
                
        

            else:
                lives -= 1
                print(f"\n {stages[lives]}")
                print("\n \n no match")

                
            

        elif language == 'es' and len(letter) != 1 and letter.isalpha():
            letter = input("dame de nuevo la letra porfavor solo una recuerda bien => ")
        else:
            letter = input("give me a letter again just one => ")
            
        

        if lives == 0 and language == 'es':
            print(f"\n \n PERDISTE \n \n la palabra fue => {random_word.upper()} \n \n el link de la palabra por si quiere saberlo  => {link.upper()}")
            break

        elif lives == 0 and language == "en":
            print(f"\n \n YOU LOST \n \n the word was => {random_word.upper()} \n \n the link of the word if you want to know it => {link.upper()}")
            break

        elif "_" not in guess_Word and language ==  'es':
            print("\n \n GANASTE! ")
            break

        elif "_" not in guess_Word and language ==  "en":
            print("\n \n YOU WON ")
            break
        
        while lives == 1 and True not in secuencia_2_despues_de_3:
                if language == 'es' :
                    response =  input(f"\n \n al parecer te has quedado con solo una vida, te dare una segunda oportunidad pero si logras completar mi adivinanza.te dare 2 vidas mas si adivinas , recuerda solo tienes {lives_Riddle} oportunidades (s)SI / (n)NO => ")
                if language == 'en' :
                    response = input(f"\n \n It seems you have only one life left, I'll give you a second chance, but if you manage to solve my riddle, I'll give you 2 more lives if you guess it. Remember, you only have {lives_Riddle} opportunity/opportunities. (y)YES / (n)NO => ")
                else:
                    break
                if (response == 's' or response == 'y') and len(response) == 1 and response.isalpha():

                    for _ in range(number_range):
                        random_key = random.choice(keys)
                        random_value = ad_list[language][random_key]
                        random_values.append(random_value)
                        random_keys.append(random_key)
                    for values in random_values:
                        print(f'\n {values}')
                    if language == 'es':
                        response = input("\n justo aqui la respuesta => ").lower()
                    elif language == 'en':
                        response = input("\n right here your answer => ").lower()
                    for key in random_keys:
                        if response == key:

                            if language == 'es':
                                print("\n muy bien")
                                lives = lives + 2
                                print(f"Ahora tienes 2 mas ")
                                break
                            if language == 'en':
                                print("\n very well")
                                lives = lives + 2
                                print(f"Now you've got 2 more")
                                break
                            
                            
                        else:
                            if language == 'es':
                                lives_Riddle -= 1
                                response = input(f"tu respuesta es incorrecta tienes ahora {lives_Riddle} vida , colocalo otra vez => ")
                                if response != key:
                                    lives_Riddle -= 1
                            if language == 'en':
                                lives_Riddle -= 1
                                response = input(f"you answer is wrong now you have {lives_Riddle} live, put again => ")
                                if response != key:
                                    lives_Riddle -= 1
                        if lives_Riddle == 0:
                            if language == 'es':
                                print(f"perdiste continua jugando con {lives}")
                                break
                            
                        if language == 'en':
                                print(f"you lost continue playing with {lives}")
                                break
                            
                    for i in range(len(lives_list) - 1):
                        if lives_list[i] == 3 and lives_list[i + 1] == 2:
                            secuencia_2_despues_de_3.append(True)
                        else:
                            secuencia_2_despues_de_3.append(False)

                        if lives_list[i] == 2 and lives_list[i + 1] == 3:
                            secuencia_3_despues_de_2.append(True)
                        else:
                            secuencia_3_despues_de_2.append(False)

                if True in secuencia_2_despues_de_3:
                    break

        def one_more_live(lives):
            letter_to_reveal = ''
            new_live = lives
            lives_list.append(new_live)
            

           
      
            if language == 'es':
                    if letter_to_reveal != '':
                        print("te dare la prima letra")
                    for i in range(len(guess_Word )-1 ,-1 ,-1):
                        if guess_Word[i] == '_':
                            letter_to_reveal = random_word[i]
                            guess_Word[i] = letter_to_reveal
                        
                        if new_live in lives_list:
                            break
    
                    if letter_to_reveal != '':          
                        print(f"aqui esta una pequeña pista'{letter_to_reveal.upper()}' en la palabra")

            elif language == 'en':
                if letter_to_reveal != '':
                    print("I'll give you a letter ")
                for i in range(len(guess_Word )-1 ,-1 ,-1):
                        if guess_Word[i] == '_':
                            letter_to_reveal = random_word[i]
                            guess_Word[i] = letter_to_reveal
                        
                        if new_live in lives_list:
                            break
    
                if letter_to_reveal != '':          
                        print(f"Here's a hint '{letter_to_reveal.upper()}' is in the word")
            

            
        if lives == 3:
            one_more_live(3)
        

if __name__ == "__main__":
     play_hangman()

    
