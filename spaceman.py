import random
import sys

attempt_counter = int(7)
letters_matched = []
available = list("abcdefghijklmnopqrstuvwyxz")
secret_word = ''
letters_guessed = []


def load_word(secret_word):  # tested this function, it works

    f = open('words.txt', 'r')
    words = f.read()
    f.close()
    #
    words_list = words.split()
    secret_word = random.choice(words_list)
    return secret_word


def incorrect_guess(secret_word) :
    # if is_word_guessed(secret_word, letters_guessed) is True:
    #     print("Congrats on guessing the secret word: " + secret_word + '. You Win!')
    global attempt_counter

    if attempt_counter <= 0:
        print("Game Over.  You lose.  The word was " + secret_word)
        play_again = input("Do You want to play again: Y/N\n")
        if play_again == "Y":
            init(secret_word, attempts)
        else:
            sys.exit("See You next time")
    else:
        attempt_counter -= 1
        print("{} attempts left.".format(int(attempt_counter)))
        take_user_input(attempt)

def attempt(letters_guessed_input, attempts):
    global attempt_counter

    if attempt_counter > 0:

        if letters_guessed_input in secret_word:
            print("Good job.")
            # take_user_input(attempt, attempt_counter)
            validate_user_guess(secret_word)
        else:
            print("Incorrect.")

            incorrect_guess(secret_word)


def take_user_input(attempt):
    # global attempt_counter

    while attempt_counter > 0:

        letters_guessed_input = input("Type in the letter you want to choose: ")

        global guess_input

        guess_input = letters_guessed_input


        if letters_guessed_input.isalpha() is True:
            if len(letters_guessed_input) != 1:
                print("Only one character at a time\n")
                take_user_input(attempt)

            elif letters_guessed_input in letters_guessed:
                print("letter already used\n")
                take_user_input(attempt)

            else:
                letters_guessed.append(letters_guessed_input)
                print(letters_guessed)
                attempt(letters_guessed_input, attempt)
                return


        else:
            print("That input isnt recognized\n")
            take_user_input(attempt)


# draw_game_board(secret_word, guessed_letter=None)
# when you are not sure if you are going to have a argument
# pass in a default value, then you dont need to give it
def draw_game_board(secret_word, letters_guessed=None):
    global game_board
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
def validate_user_guess(secret_word):
    # look at the attempt
    # check if attempt is in the secret_word
    # loop thru the word

    global list_of_indexes
    list_of_indexes = []
    # for letter in secret_word:
    for i in range(0, len(secret_word)):
        # print('i: {}'.format(i))
        if secret_word[i] == guess_input:
            # print('in the if statement')
            list_of_indexes.append(i)
    # if word[letter] == attempt:

        # it is correct -> use some way to update the board
        # if wrong:
            # add to wrong letters list -> maybe we always show this to the user
        print(list_of_indexes)
        update_gameboard()

def update_gameboard():
    #I want to take the results of the validate user guess
    # if len(list_of_indexes) != 0 -> then we know letter is correct
    # else len(list_of_indexes) == 0 -> then we know it was incorrect, dont update the board
    #If the letter is in the word I want to print that letter on the gameboard
    #I want to compare the correct guess index number with the index on the game board
    #print the letter instead of an underscore
    #for the rest of the indexs in the validate print "_"

    if len(list_of_indexes) != 0:
        for i in list_of_indexes:
            game_board[i] = guess_input
    # return game_board
    print(game_board)
    if "_" in game_board:
        take_user_input(attempt)
    else:
        print("You Won. The word is" + secret_word)
        play_again = input("Do You want to play again: Y/N\n")
        if play_again == "Y":
            init(secret_word, attempts)
        else:
            sys.exit("See You next time")








# if __name__ == '__main__':
#     # print(validate_user_guess('apples', 'p'))
#     gameboard = ['_','_','_','_','_','_'] #apples
#     list_of_indexes = [1,2]
#     letter = 'p'
    # update_gameboard(gameboard, list_of_indexes, letter)

#
#
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
#
#
def init(secret_word, attempt):

    draw_game_board(secret_word, letters_guessed=None)
    print("\n")
    print(secret_word)

    take_user_input(attempt)





secret_word = load_word(secret_word)
spaceman(secret_word)
init(secret_word, attempt)


# def test():
#     print(secret_word)
#     print(draw_game_board)
