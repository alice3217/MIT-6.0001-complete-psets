# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    s = ""
    for char in secret_word:
        if char in letters_guessed:
            s += char
        
    return len(s) == len(secret_word)
        



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    secret_word_to_print = ""
    for char in secret_word:
        if char not in letters_guessed:
            secret_word_to_print += "_ "
        else:
            secret_word_to_print += char
            
    return secret_word_to_print


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = ""
    for i in string.ascii_lowercase:
        if i not in letters_guessed:
            available_letters += i
            
    return available_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    #initial print statements 
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is", len(secret_word), "letters long")
    print("-----------------")
    
    guesses = 6
    all_guesses = []
    print("You have", guesses, " guesses")
    print ("Available letters:", get_available_letters(all_guesses))
    warning = 3
    for int in range(0, 100):
        
        users_guess = input("Please guess a letter: ")
        #ensures that the user can only guess 1 letter
        assert len(users_guess) == 1, "You must guess a letter and you may only guess one letter at a time"
        #makes the users guess lowercase
        users_guess = users_guess.lower()
       
        
        
        #checks if the users guess is a letter and warns if it is not
        if not users_guess.isalpha() and warning > 0:
           warning -= 1
           print("Oops! That is not a valid letter. You have", warning, "warnings left:", get_guessed_word (secret_word, all_guesses))
           continue
       #checks if the users has repeated a guess and warns if they have
        if users_guess in all_guesses:
            warning -= 1
            print("Oops! You've already guessed that letter. You now have", warning, "warnings:", get_guessed_word (secret_word, all_guesses))
            continue
       #checks if there are 0 warnings left and deducts a guess if true
        if warning == 0:
            warning = 3
            if guesses == 0:
                print("You run out of guesses due to invalid input. The secret word was", secret_word)
                break
            guesses -= 1
            print ("You have", guesses, "guesses left")
            continue
       
        #creates a list for all the user's guesses
        all_guesses.append(users_guess)
        
        
        
        #checks is the usesr guessed a letter in the secret word
        if users_guess not in secret_word:
            if users_guess in ["a", "e", "i", "o", "u"]:
                guesses -= 2
            else:
                guesses -= 1
            if guesses < 0:
                print("Oops, you run out of guesses. The secret word was", secret_word)
                break
            
            print("Oops! That letter is not in my word:", get_guessed_word (secret_word, all_guesses))
            print("You have", guesses, " guesses left")
            
            
           
        else:
            print("Good guess:", get_guessed_word (secret_word, all_guesses))
            print("You have", guesses, "guesses left")
            
            
        print ("Available letters:", get_available_letters(all_guesses))    
        
        
        
        if is_word_guessed(secret_word, all_guesses):
            list_of_unique_char = []
            for char in secret_word:
                if char not in list_of_unique_char:
                    list_of_unique_char.append(char)
                    
            score = guesses * len(list_of_unique_char)
            print("Congratulations, You won!")
            print("Your total score for this game is:", score)
            break
        
        if guesses == 0:
            print("Sorry, you run out of guesses. The secret word was", secret_word)
            break
        
        
        
        print ("-----------------")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    a_list = []
    word_no_spaces = my_word.replace(" ", "")
    
    if len(word_no_spaces) == len(other_word):
        #makes a list with the indexes of the letters in my_word
        list_index = [pos for pos, char in enumerate(word_no_spaces) if char.isalpha()]
        index = 0
        #assigns a variable with the value of the index of a letter
        index_in_list = list_index[index]
        #compares the indexes of the letters in the words list and the fragment of the word the user has guessed

        for int in range(len(list_index)):
            index_in_list = list_index[index]
            if word_no_spaces[index_in_list] == other_word[index_in_list]:
                
                a_list.append("Yes")
            #makes sure it goes to the next index of the next letter
                index += 1
                
            else:
                index_in_list = list_index[index]
                a_list.append("No")
                index += 1
                
        #The part that matches the words            
        if "No" in a_list:
            return False
        else:
            return True
        
    else:
        return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    num_words = 0
    list_of_possible_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list_of_possible_words.append(word)
            num_words += 1
    
    if num_words == 0:
        
        return "No matches found"
    else:
        
        return list_of_possible_words



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
   
    #initial print statements 
    print ("Welcome to the game Hangman!")
    print ("I am thinking of a word that is", len(secret_word), "letters long")
    print("-----------------")
    
    guesses = 6
    all_guesses = []
    print("You have", guesses, " guesses")
    print ("Available letters:", get_available_letters(all_guesses))
    warning = 3
    for int in range(0, 100):
        
        users_guess = input("Please guess a letter: ")
        #ensures that the user can only guess 1 letter
        assert len(users_guess) == 1, "You must guess a letter and you may only guess one letter at a time"
        
        
        
        #makes the users guess lowercase
        if users_guess != "*":
            users_guess = users_guess.lower()
       
        
        
        #checks if the users guess is a letter and warns if it is not
        if not users_guess.isalpha() and warning > 0 and users_guess != "*":
           warning -= 1
           print("Oops! That is not a valid letter. You have", warning, "warnings left:", get_guessed_word (secret_word, all_guesses))
           continue
       #checks if the users has repeated a guess and warns if they have
        if users_guess in all_guesses:
            warning -= 1
            print("Oops! You've already guessed that letter. You now have", warning, "warnings:", get_guessed_word (secret_word, all_guesses))
            continue
       #checks if there are 0 warnings left and deducts a guess if true
        if warning == 0:
            warning = 3
            if guesses == 0:
                print("You run out of guesses due to invalid input. The secret word was", secret_word)
                break
            guesses -= 1
            print ("You have", guesses, "guesses left")
            continue
       
            
        #creates a list for all the user's guesses
        if users_guess != "*":
            all_guesses.append(users_guess)
        
        
        
        #checks is the usesr guessed a letter in the secret word
        if users_guess not in secret_word and users_guess != "*":
            if users_guess in ["a", "e", "i", "o", "u"]:
                guesses -= 2
            else:
                guesses -= 1
            if guesses < 0:
                print("Oops, you run out of guesses. The secret word was", secret_word)
                break
            
            print("Oops! That letter is not in my word:", get_guessed_word (secret_word, all_guesses))
            print("You have", guesses, " guesses left")
        #with hint
        elif users_guess == "*":
            
            print("Possible word matches are:", show_possible_matches(get_guessed_word(secret_word, all_guesses)))
            continue    
        else:
            print("Good guess:", get_guessed_word (secret_word, all_guesses))
            print("You have", guesses, "guesses left")
            
            
        print ("Available letters:", get_available_letters(all_guesses))    
        
        
        
        if is_word_guessed(secret_word, all_guesses):
            list_of_unique_char = []
            for char in secret_word:
                if char not in list_of_unique_char:
                    list_of_unique_char.append(char)
                    
            score = guesses * len(list_of_unique_char)
            print("Congratulations, You won!")
            print("Your total score for this game is:", score)
            break
        
        if guesses == 0:
            print("Sorry, you run out of guesses. The secret word was", secret_word)
            break
        
        
        
        print ("-----------------")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
     #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
     # secret_word = choose_word(wordlist)
      #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
