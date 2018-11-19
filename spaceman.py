import random

count = int(7)
letters_matched = []
available = list("abcdefghijklmnopqrstuvwyxz")
secret_word = ''


def load_word(secret_word):  # tested this function, it works

    f = open('words.txt', 'r')
    words = f.read()
    f.close()

    words_list = words.split()
    secret_word = random.choice(words_list)
    return secret_word


def take_user_input(attempt):
    # write some psuedo code
    # take a weeeee break
    # come back to this after you feel refreshed

    # letters_guessed = []
    # the_input = input("Type in the letter you want to choose:")
    #
    # if the_input != alpha():
    #     if len(the_input) != 1:
    #         print("Only one  character at a time")
    #         return
    #     else:
    #         letters_guessed.append(the_input)
    #         print(letters_guessed)
    #         attempt(letters_guessed, secret_word, draw_game_board, available, user_input, count)
    #
    # else:
    #     print("I'm afraid that letter isnt recognized")
    #     return

# draw_game_board(secret_word, guessed_letter=None)
# when you are not sure if you are going to have a argument
# pass in a default value, then you dont need to give it
def draw_game_board(secret_word, letters_guessed=None):
    game_board = []
    word = secret_word
    num_of_letters = len(game_board)

    for letter in word:
        game_board.append('_')

    drawn_board = ' '.join(game_board)
    print(drawn_board)



#
# if __name__ == '__main__':
#     # print(secret_word)
#     print(draw_game_board('secretword'))


def reveal_word(secret_word, user_input):
    ls_word = list(secret_word)
    if user_input in ls_word:
        print()

# This function works....kind of
# return a list of indexes
def validate_user_guess(secret_word, attempt):
    # look at the attempt
    # check if attempt is in the secret_word
    # loop thru the word
    indexes = []
    # for letter in secret_word:
    for i in range(0, len(secret_word)):
        print('i: {}'.format(i))
        if secret_word[i] == attempt:
            print('in the if statement')
            indexes.append(i)
    # if word[letter] == attempt:

        # it is correct -> use some way to update the board
        # if wrong:
            # add to wrong letters list -> maybe we always show this to the user
    return indexes

def update_gameboard(gameboard, list_of_indexes, letter):
    #I want to take the results of the validate user guess
    # if len(list_of_indexes) != 0 -> then we know letter is correct
    # else len(list_of_indexes) == 0 -> then we know it was incorrect, dont update the board
    #If the letter is in the word I want to print that letter on the gameboard
    #I want to compare the correct guess index number with the index on the game board
    #print the letter instead of an underscore
    #for the rest of the indexs in the validate print "_"

    if len(list_of_indexes) != 0:
        for i in list_of_indexes:
            gameboard[i] = letter
    return gameboard
    # print(gameboard)




if __name__ == '__main__':
    # print(validate_user_guess('apples', 'p'))
    gameboard = ['_','_','_','_','_','_'] #apples
    list_of_indexes = [1,2]
    letter = 'p'
    update_gameboard(gameboard, list_of_indexes, letter)

# def attempt(letters_guessed, secret_word, draw_game_board, available, user_input, count):
#
#     count = 0
#     the_guess = ''.join(letters_guessed)
#     the_word = list()
#     almost_hidden = draw_game_board(secret_word)
#     hidden = list(almost_hidden)
#     s_list = list(secret_word)
#
#     print("\nletters guessed: {}\n".format(the_guess))
#
#     for s_word in s_list:
#         if the_guess in s_word:
#             for the_guess in s_word:
#                 the_word.append(s_word)
#                 print(s_word)
#                 # available.remove(s_word)
#
#         elif s_word is not the_guess:
#             the_word.append('_')
#             if "_" in the_word:
#                 letters_matched = ''.join(the_word)
#                 hidden.clear()
#                 hidden.append(letters_matched)
#         else:
#             print("error")
#
#     init(secret_word, user_input, attempt)
#
#
def get_guessed_word(secret_word, letters_guessed, draw_game_board):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.

    lettersGuessed: list of letters that have been guessed so far.

    returns: string, of letters and underscores.

    For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.

    For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    print("Letters Guessed: " + letters_guessed)



#
# def get_available_letters(letters_guessed, available):
#     '''
#     lettersGuessed: list of letters that have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''
#
#     removed = set(letters_guessed)
#     # This makes a list so you need brackets
#     return [x for x in available if x not in removed]
#
#
# def spaceman(secret_word):
#     '''
#     secretWord: string, the secret word to guess.
#     Starts up a game of Spaceman in the command line.
#     * At the start of the game, let the user know how many
#       letters the secretWord contains.
#     * Ask the user to guess one letter per round.
#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the computer's word.
#     * After each round, you should also display to the user the
#       partially guessed word so far, as well as letters that the
#       user has not yet guessed.
#     '''
#     # FILL IN YOUR CODE HERE...
#     print("Welcome to Spaceman")
#     print("Their are" + " " + str(len(secret_word)) +
#           " " + "letters in this word.")
#     print("Guess a letter for each space to reveal the word.")
#     print("If you guess wrong I start drawing the spaceman.")
#     print("If I draw him completely then he flies into space")
#     print("and you lose :(")
#     print("You get 7 tries before he's completely drawn.")
#     print("\n")
#     print(
#         "These letters are available to choose:\n{}" .format(' '.join(available)))
#     print("\n")
#
#
# def init(secret_word, user_input, attempt):
#
#
#     print("_" * len(secret_word))
#     print(secret_word)
#
#     user_input(secret_word, user_input, attempt)
#     attempt()
#     count()
#
#
# secret_word = load_word(secret_word)
# spaceman(secret_word)
# init(secret_word, user_input, attempt)


# def test():
#     print(secret_word)
#     print(draw_game_board)
