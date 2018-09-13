import random

count = int(7)
letters_guessed = []
letters_matched = []
available = list("abcdefghijklmnopqrstuvwyxz")
secret_word = ''

def load_word(): # tested this function, it wo
   global secret_word

   f = open('words.txt', 'r')
   words = f.read()
   f.close()

   words_list = words.split()
   secret_word = random.choice(words_list)
   return secret_word


def user_input(letters_guessed):
    user_input = input("Type in the letter you want to choose:")

    if user_input.isalpha() == True and len(user_input) == 1:
        letters_guessed.append(user_input)

    elif len(user_input) !=1:
        print("Only one  character at a time")
        return
    else:
        print("I'm afraid that letter isnt recognized")
        return


def hide_word(secret_word):
    di = dict([i, "_"] for i in secret_word)
    li = list(di.values())
    return ''.join(li)


def reveal_word(secret_word, user_input):
    ls_word = list(secret_word)
    if user_input in  ls_word:
        print()


def attempt(secret_word, letters_guessed, init):
    count = 0
    the_guess = letters_guessed(secret_word)

    s_list = list(secret_word)
    print(s_list)

    for s_word in s_list:
        #print(s_word)
        if s_word not in the_guess:
            count += 1
            total_count = str(count);
            print("Not in word")
            print("failed attempts:{}".format(''.join(total_count)))

            if count > 7:
                print("oh no")
            else:
                guess_result(attempt, letters_guessed, s_list, available, hide_word, secret_word)


def guess_result(attempt, letters_guessed, s_list, available, hide_word, secret_word):
    my_guesses = letters_guessed

    s_list = list(secret_word)
    the_word = list()
    hide_word = list(hide_word(secret_word))

    for s_word in s_list:

        if s_word in letters_guessed:

            the_word.append(s_word)
            available.remove(s_word)

        elif s_word is not my_guesses:
            the_word.append('_')
            if "_" in the_word:
                letters_matched =  ''.join(the_word)
                hide_word.clear()
                hide_word.append(letters_matched)
        else:
            print("Error")

        print(the_word);
        print(available);
        print(''.join(hide_word))


def count(available,hide_word):
    global count

    if available in the_word:
        True
        print("yay")
    else:
        False
        print("boo")


    if count == 0:
        print("You lost")
        print(secret_word())
        return
    else:
        count -= 1
        init(secret_word, user_input, attempt)



def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''


    # FILL IN YOUR CODE HERE...
    if user_input in secret_word:
        user_input.pop(letters_guessed)
        print("Good Job!");
        return True;
    else:
        return False
        print("Sorry" + " " + str(letters_guessed)+ " " + "is not in word :(")


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
    return [x for x in available if x not in removed] # This makes a list so you need brackets


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
    print("Their are" + " " + str(len(secret_word)) + " " + "letters in this word.")
    print("Guess a letter for each space to reveal the word.")
    print("If you guess wrong I start drawing the spaceman.")
    print("If I draw him completely then he flies into space")
    print("and you lose :(")
    print("You get 7 tries before he's completely drawn.")
    print("\n")
    print(
    "These letters are available to choose:\n{}" .format(' '.join(available)))
    print("\n")


def init(secret_word, user_input, attempt):

    print(secret_word)
    print(hide_word(secret_word))

    user_input(letters_guessed)
    attempt(secret_word, hide_word, init)


secret_word = load_word()
spaceman(secret_word)
init(secret_word, user_input, attempt)


def test():
        print(secret_word)
        print(hide_word)
