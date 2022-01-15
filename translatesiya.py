# Siya Joshi
# November 28, 2020
# 501010079
# This program translates a user input about food from the dictionary 'EtoP' between English and Punjabi
# IMPROVEMENTS
# 1) Chose a domain that is simple greetings and school related
# 2) Changed the second language to punjabi
# 3) Increased the vocabulary
# 4) Added comments
# 5) Fixed the glitch where there were two periods at the end of a translation, when there was not two periods in the input
# 6) Wrote a function reverseDictionary(dictionary) that can go from EtoP and back to PtoE without having to run the entrie input and code all over again.
# 7) Introduced new Punjabi translations that are multiple words for one english word.
# 8)Added a global running
EtoP = {'I' : 'Mai', 'Hi' : 'Kiddha', 'girl' : 'Soniye', 'horkiddha' : 'how-are-you?', 'weather' : 'masum', 'sunny' : 'thop', 'rain' : 'mi', 'cloudy' : 'badal', 'taxi' : 'riksha',
    'bus':'basa' , 'car':'gaddi', 'train': 'railgaddi' , 'drive' : 'gaddi-chala', 'good' : 'vadiya','ok' : 'teek', 'am' : 'hai', 'comfortable' : 'zabardast', 'boy' : 'munda', 'Welcome' : 'Aou', 'Thank-you' : 'danyavaad', 'read' : 'paro',
        'so' : 'hor', 'what' : 'ki', 'why' : 'kyo', 'where' : 'kithey', 'who' : 'kaun', 'how' : 'kaise', 'bye' : 'changa', 'and' : 'te',
        'textbook' : 'kithab', 'computer' : 'computer', 'pen' : 'pen', 'calculator' : 'calculator', 'paper' : 'papera', 'play' : 'kedho',
        'wear' : 'pa', 'mom' : 'maa', 'dad' : 'papa', 'teacher' : 'madam', 'sir' : 'sir', 'first-name' : 'pehlanaam', 'last-name' : 'akheerlanaam', 'walk' : 'chalna', 'run' : 'jhorna',
        'have' : 'leh', 'fun' : 'muja', 'day' : 'din', 'food' : 'khana', 'drink' : 'peena', 'punishment' : 'murgaban', 'please' : 'please', 'no' : 'nai',
        'yes' : 'hain', 'homework' : 'syllabus', 'exam' : 'paper','is':'te'}

PtoE = dict([(value, key) for key, value in EtoP.items()])  # flip the EtoF dictionary

dicts = {'English to Punjabi' : EtoP ,}  # Sets the variables that the translation will pick from

def translateWord(word, dictionary):
    if word in dictionary.keys(): # Looks for word in given dictionary
        return dictionary[word]   # Returns the translated word from the dictionary
    elif word != '' :             # If the word is not in the dictionary it will return the word with quotations
        return '"' + word + '"'
    return word                   # Return whatever is done

def translate(phrase, dicts, way) :
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # Declares the upper case letters
    LCletters = 'abcdefghijklmnopqrstuvwxyz' # Declares the lower case letters
    letters = UCletters + LCletters # Combines both together
    dictionary = dicts[way] # which dictionary it will be receiving words from (line 57)
    translation = ''
    word = ''
    for character in phrase :
        if character in letters :
            word = word + character
        else :
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary)
    translation = translation.replace(translation[0], translation[0].upper())
    return translation

def printtrans(sentence ,way):
    print('Input:', sentence)
    print('Your translation is...')
    print('Output:', translate(sentence.lower(), dicts, way))

def add(start, end):
    n = int(input('How many words did you want to add? '))
    for i in range(n):
        print('Which dictionary are you adding this word too?', end='')
        if start == 'Eng':
            print('English-')
        elif end == 'Punj':
            words = EtoP
        if start == 'Punjabi':
            print('Punjabi-')
        elif end == 'Eng':
            words = PtoE

        print('Please enter the', end = ' ')
        if start == 'Eng':
            key = input('English word: ')
        elif start == 'Punj':
            key = input('Punjabi word: ')

        print('Please enter the translation to its word', end = '')
        if end == 'Eng':
            value = input('English word: ')
        elif end == 'Punj':
            value = input('Punjabi word: ')

        words.update({key: value})
        print('Word has been added successfully')
    return

def translateEnglishtoPunjabi(sentence_inenglish):
    global EtoP
    global PtoE

    # start with sentence in Punjabi
    sentence_inpunjabi = ' ' + sentence_inenglish[:] + ' '
    sentence_inpunjabi = sentence_inpunjabi.replace('.', '')
    for word in EtoP.keys():
        # if the word is included in the dictionary
        while (' ' + word + ' ') in sentence_inpunjabi:
            sentence_inpunjabi = sentence_inpunjabi.replace(' ' + word + ' ', ' ' + EtoP[
                word] + ' ')  # adding the punjabi meaning to the english word

    if (sentence_inpunjabi[len(sentence_inpunjabi) - 1] == ' '):
        sentence_inpunjabi = sentence_inpunjabi[:len(sentence_inpunjabi) - 1]

    return sentence_inpunjabi + '.'  # sentence is returned in punjabi


def translatePunjabitoEnglish(sentence_inpunjabi):
    global EtoP
    global PtoE
    sentence_inenglish = ' ' + sentence_inpunjabi[:] + ' '
    sentence_inenglish = sentence_inenglish.replace('.', '')
    # start with sentence in English
    # sentence_inenglish = ''
    # obtain a dictionary that goes from Punjabi to english
    # PtoE = reverseDictionary(EtoP)
    # add english meaning for every word
    for word in PtoE.keys():
        while (' ' + word + ' ') in sentence_inenglish:
            # if the word is included in the dictionary
            sentence_inenglish = sentence_inenglish.replace(' ' + word + ' ', ' ' + PtoE[
                word] + ' ')  # adding the english meaning to the Punjabi word

    if (sentence_inenglish[len(sentence_inenglish) - 1] == ' '):
        sentence_inenglish = sentence_inenglish[:len(sentence_inenglish) - 1]
    return sentence_inenglish + '.'  # sentence is returned in english


# Now that everything is defined, we can start the actual code.
# I wanted to give the user the option to be greeted and enter or exit the translator.

print("Welcome to the 3 language translator!.")  # Greets the user.
# Define the variables yes and no
yes = 'y'
no = 'n'
# Ask user if they would like to enter.
enter = input("Would you like to use this translator? Enter Y/N ")

# We have to run a loop to go according to the user's watns. When they would like to exit the loop will break,
# else it will continue.
# While loop is created if the user enters into the system

while enter.lower() != yes:
    # If user chooses no, it will stop and print this message out
    if enter.lower() == no:
        print("Goodbye.")
        exit()
    # If user enters anything other that Y or N, it will return that they need to enter something appropriate.
    elif enter.lower() != yes:
        print("Invalid answer. Please try again.")
        enter = input("Would you like to use this translator? Enter Y/N")

# This loop is run to determine what ar ethe languages being used to translate from and to.
while True:
    toLan = input("What language will you be translating from? (Eng/Punj): ")
    # Checks if the input is valid, if not asks user to input again.
    while toLan.lower() != 'eng' and toLan.lower() != 'punj':
        print("Invalid entry. Please try again.")
        toLan = input("What language will you be translating from? (Eng/Punj): ")
    toLan = toLan.lower()

    toLan = input('What language do you want to translate to? (Eng/Punj): ')
    # Checks if the input is valid, if not asks user to input again.
    while toLan.lower() != 'eng' and toLan.lower() != 'punj':
        print("Invalid answer. Please try again.")
        toLan = input('What language do you want to translate to? (Eng/Punj): ')
    toLan = toLan.lower()

    # Because this dictionary consists of very small amount of words, I would like to give the user to an option to
    # look at the words to pick from
    seediction = ''
    print("Would you like to see " ,end = '')

    if toLan == 'eng':
        # If they choose to translate from English
        seediction = input("English words (Y/N)? ")
        while seediction.lower() != yes and seediction.lower() != no:
            print('Invalid answer. Please try again.')
            seediction = input("Would you like to see the English words? (Y/N) ")

    elif toLan == 'punj':
        # If they choose to translate from Punjabi
        seediction = input("Punjabi words (Y/N)? ")
        while seediction.lower() != yes and seediction.lower() != no:
            print('Invalid answer. Please try again.')
            seediciton = input("Would you like to see the Punjabi words? (Y/N) ")

    seediction = seediction.lower()
    if toLan == 'eng' and seediction == yes:
        print('------')
        for key in EtoP.keys():
            # Print all the keys of the chosen language dictionary
            print('-', key)
        print('--------')
    elif toLan == 'punj' and seediction == yes:
        print('------')
        for key in PtoE.keys():
            print('-', key)
        print('--------')

    # testing the translator program
    sentence = 'Hi how-are-you? '
    translatedEtoS = translateEnglishtoPunjabi(sentence)
    print('--------------------------------------')
    print('Input:', sentence)
    print('Output:', translatedEtoS)
    print('--------------------------------------')

    sentence = 'masum te vadiya'
    translatedStoE = translatePunjabitoEnglish(sentence)
    print('Input:', sentence)
    print('Output:', translatedStoE)
    print('--------------------------------------')
