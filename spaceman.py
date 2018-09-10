import random

letters_guessed = []
available = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def load_word():
   f = open('words.txt', 'r')
   words_list = f.readlines()
   f.close()

   words_list = words_list[0].split(' ')
   secret_word = random.choice(words_list)
   return secret_word

def hide_word(secret_word):
    list_word = secret_word.split(' ');
    hide_word = {
        i : _ for i in list_word
    }
    return hide_word
    print(hide_word.keys())

def reveal_word(hide_word, letters_guessed):
    letters = hide_word.values()
    for letters_guessed in letters:

        return letters.__class__(map(reversed, letters.items()))


def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    # FILL IN YOUR CODE HERE...
    if letters_guessed in secret_word:
        return True;
        print("Good Job!");
    else:
        return False
        print("Sorry" + " " + letters_guessed + " " + "is not in word :(")


def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    print("Letters Guessed: " + letters_guessed)
    print(reveal_word)



def get_available_letters(letters_guessed,available):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    removed = set(letters_guessed)
    return (x for x in available if x not in removed)


def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to Spaceman")
    print("Their are" + " " + str(len(secret_word)) + " " + "letters in this word")
    print("Guess a letter for each space to reveal the word")
    print("If you guess wrong I start drawing the spaceman.")
    print("If I draw him completely then he flies into space and you lose :( \n You get 7 tries before he's completely drawn.")
    print("\n")

secret_word = load_word()
spaceman(
    load_word()
)


def letters_guessed(attempt):

    if letters_guessed.isalpha():
        lower_attempt = attempt.lower()
        return lower_attempt
        print(lower_attempt)

    elif attempt.isdigit():
        print("Letters Only");

    elif len(attempt) != 1:
        print("Choose One Letter");

    elif attempt in letters_guessed.values():
        print("Already Chosen")
        print(letters_guessed)
    else:
        "Try Again"

def user_input(prompt):
    user_input = input(prompt)
    return user_input;

def running():
    True

while running:
    selection = user_input(
        "Choose a letter:")
    running = letters_guessed(selection)
