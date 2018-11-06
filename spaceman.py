import random

count = int(7)
letters_matched = []
available = list("abcdefghijklmnopqrstuvwyxz")
secret_word = ''


def load_word():  # tested this function, it works
    global secret_word

    f = open('words.txt', 'r')
    words = f.read()
    f.close()

    words_list = words.split()
    secret_word = random.choice(words_list)
    return secret_word


def user_input():
    global letters_guessed
    global secret_word
    global attempt

    letters_guessed = []
    the_input = input("Type in the letter you want to choose:")

    if the_input.isalpha():
        if len(the_input) != 1:
            print("Only one  character at a time")
            return
        else:
            letters_guessed.append(the_input)
            print(letters_guessed)
            attempt()

    else:
        print("I'm afraid that letter isnt recognized")
        return


def hide_word(secret_word):
    di = dict([i, "_"] for i in secret_word)
    li = list(di.values())
    return ''.join(li)


def reveal_word(secret_word, user_input):
    ls_word = list(secret_word)
    if user_input in ls_word:
        print()


def attempt():
    global letters_guessed
    global secret_word
    global hide_word
    global available
    global user_input
    global count

    count = 0
    the_guess = ''.join(letters_guessed)
    the_word = list()
    almost_hidden = hide_word(secret_word)
    hidden = list(almost_hidden)
    s_list = list(secret_word)

    print("\nletters guessed: {}\n".format(the_guess))

    for s_word in s_list:
        if the_guess in s_word:
            for the_guess in s_word:
                the_word.append(s_word)
                print(s_word)
                # available.remove(s_word)

        elif s_word is not the_guess:
            the_word.append('_')
            if "_" in the_word:
                letters_matched = ''.join(the_word)
                hidden.clear()
                hidden.append(letters_matched)
        else:
            print("error")

    init()


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


def get_available_letters(letters_guessed, available):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    removed = set(letters_guessed)
    # This makes a list so you need brackets
    return [x for x in available if x not in removed]


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
    print("Their are" + " " + str(len(secret_word)) +
          " " + "letters in this word.")
    print("Guess a letter for each space to reveal the word.")
    print("If you guess wrong I start drawing the spaceman.")
    print("If I draw him completely then he flies into space")
    print("and you lose :(")
    print("You get 7 tries before he's completely drawn.")
    print("\n")
    print(
        "These letters are available to choose:\n{}" .format(' '.join(available)))
    print("\n")


def init():
    global secret_word
    global user_input
    global attempt

    print(secret_word)

    user_input()
    attempt()
    count()


secret_word = load_word()
spaceman(secret_word)
init()


def test():
    print(secret_word)
    print(hide_word)
