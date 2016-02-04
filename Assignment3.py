# Make variable names more insightful, if it is an index name it so you know what you are indexing
# 


########################################################################
##
## CS 101
## Program 3
## Brendan O'Connor
## bmo7x9@mail.umkc.edu / brendan.oconnor.913@gmail.com 
## Created 9/26/2015
## Due 10/4/2015
##
## PROBLEM : 
##      The problem is to take hawiian words and provide a phonetic guide for  
##      the user on how to properly pronounce the words.
##
## ALGORITHM : 
##
## I1 Get a string input from the user
## I2 Compare string against a list of valid Hawiian characters
## I3 If the string contains invalid characters output an error and 
## I4 ask for a new string with valid hawaiian characters
## I5 if any unusual accented hawiian characters we will convert them to regular
## alpha characters
## I5 If the string contains only valid characters continue the rest of the 
## script
## E1 Once a valid string is obtained, iterate through each character
## E2 For each character evaulate according to the following rules and
## E3 Insert the corresoponding character or phonetic into a new variable
## F1 If the character is in a list of consonants put the character
##  unchanged into the variable
## F2 Unless it is 'w' after 'i or e' - insert a v instead of w
## F3 If the character is in a list of vowels replace each vowel with
##  the following unless the vowel is followed by another vowel then check to
##  see if it is in the exception list.
## F4 For regular vowels w/o following vowels insert the following below
##  followed by '-' (unless it is the last character) into the variable.
## F5 a - 'ah', e - 'eh', i -'ee', 'o' - oh, u - 'oo'
## F6 For the exceptions insert the corresponding string into the variable
##  followed by '-' (unless it is the last character)
## F7 ai - 'eye', ae - 'eye', ao - 'ow', au - 'ow', ei - 'ay', eu - 'eh-oo'
##  iu - 'ew', oi - 'oy', ou - 'ow', ui - 'ooey'
## F8 If ' ' or " ' " then simply input it unchanged into the variable
## O1 After each character has been evaluated and inserted into the new string
##  the variable will be printed
## O2 Then the user will be asked if they want to enter another word
## O3 The program will check to make sure valid input was entered
## O4 If Yes it will go back to I1 if not the program will end
## 
## ERROR HANDLING:
##      The only error handling will be to make sure valid input is entered
##      when asked for the string and if they want to enter another word.
##
## OTHER COMMENTS:
##      
##
########################################################################

# 1. Think before you program!
# 2. A program is a human readable essay on problem solving that is executed by a computer
# 3. Best way to improve is to practice
# 4. Foolish consistency is the hobgoblin of little minds
# 5. Test code thoroughly and often
# 6. If it is hard to write, it is hard to read, add a comment
# 7. All input is evil until proven otherwise


hawiianchars = ["a","e","i","o","u","p","k","h","l","m","n","w"," ","'"]
consonantsandsymbols = ["p", "k", "h", "l", "m", "n", "w", " ", "'"]
vowels = ["a", "e", "i", "o", "u"]
vowelexceptions = ["ai", "ae", "ao", "au", "ei", "eu", "iu", "oi", "ou", "ui"]
# list of valid hawiian characters and substrings for sorting

# A function used to determine if the letter before index w of string == character 
def is_following(string, character, w):
    if w == 0:
        return False
    else:
        if string[w-1] == character:
            return True
        else:
            return False

# Function to check and see if the two preceeding characters are in the vowel exceptions group
def is_following_execp(string, n):
    if int(n) < 2:
        return False
    else:
        if string[int(n)-2:int(n)] in vowelexceptions:
            return True
        else:
            return False

# A function to return the phonetics of a normal vowel
def is_reg_vowel(vow):
    if vow == 'a':
        return 'ah-'
    elif vow == 'e':
        return 'eh-'
    elif vow == 'i':
        return 'ee-'
    elif vow == 'o':
        return 'oh-'
    elif vow == 'u':
        return 'oo-'
    else:
        return 'error not a vowel'

translating = True
while translating:

    stringtest = True
    # Prompt for word and validate it
    while stringtest:

        try:
            # Get hawiian word
            initialstr = input("Please insert a Hawiian word you wish to pronounce('h' for help): ").lower()
            invalid = "" # For storing invalid characters
            invalidchars = False # Used for outputting invalid characters

            # We are going to check the string for invalid hawiian characters with a for loop
            for char in initialstr:
                if initialstr.upper() == 'H':
                    print("Valid characters are", hawiianchars)
                elif char not in hawiianchars:
                    invalid += char
                    invalidchars = True
            else:
                stringtest = False # end the loop if no errors or 'h' encountered

            if invalidchars:
                print("The following are invalid hawiian characters:", invalid) # Output what made the input invalid
        except:
            print("Please enter valid input")

    # We now need to evaulate each char in string to determine the phonetics
    finalstring = "" # Variable we will store phonetics in
    n = 0 # Index used to check characters preceeding the current itieration
    for char in initialstr:
        if char in consonantsandsymbols:
            if char == "w":
                if is_following(initialstr, 'i', n) or is_following(initialstr, 'e', n): # following i or e
                    finalstring += 'v'
            elif (char == ' ' or char == "'") and (initialstr[n-1] in vowels): # Getting rid of '-' before spaces and apostrophe's
                finalstring = finalstring[:-1]
                finalstring += char
            else:
                finalstring += char

        elif char in vowels:
            if char in ["e", "i", "o", "u"] and (not is_following_execp(initialstr, n or is_following_execp(initialstr, n-1))):
            # Only want to apply exception pronunciation if there aren't any exceptions preceding it
            # or if there is an exception preceding it then the character before the current char isn't included in the exception pronunciation

                # Go through each exception vowel case and apply the phonetic rule
                if is_following(initialstr, 'a', n): # following a
                    if char == 'i' or char == 'e':
                        finalstring = finalstring[:-3] # strips the preceeding vowel phonetic from finalstring
                        finalstring += 'eye-' # Adds the phonetic rule
                    elif char == 'o' or char == 'u':
                        finalstring = finalstring[:-3] 
                        finalstring += 'ow-'

                elif is_following(initialstr, 'e', n): # following e
                    if char == 'i':
                        finalstring = finalstring[:-3] 
                        finalstring += 'ay-'
                    elif char == 'u':
                        finalstring = finalstring[:-3] 
                        finalstring += 'eh-oo'
                    else: #e or o
                        finalstring += is_reg_vowel(char)

                elif is_following(initialstr, 'o', n): # following o
                    if char == 'i':
                        finalstring = finalstring[:-3] 
                        finalstring += 'oy-'
                    elif char == 'u':
                        finalstring = finalstring[:-3] 
                        finalstring += 'ow-'
                    else: #char == e or o:
                        finalstring += is_reg_vowel(char)

                elif is_following(initialstr, 'i', n) and char == 'u': # following i and char == u
                    finalstring = finalstring[:-3] 
                    finalstring += 'ew-'
                elif is_following(initialstr, 'u', n) and char == 'i': # following u and char == i
                    finalstring = finalstring[:-3] 
                    finalstring += 'ooey-'
                else: # not in exception list
                    finalstring += is_reg_vowel(char)
            else: # char == a
                finalstring += is_reg_vowel(char)
        n += 1

    finalstring = finalstring.strip('-').capitalize() # clean up the string for outputting
    print(finalstring)

    while True: # Give the user the option of doing more words or stopping
        trans_again = input("Would you like to translate another word? ").upper()

        if trans_again == "Y" or trans_again == "Yes":
            break
        elif trans_again in ["N", "NO"]:
            translating = False
            break
        else:
            print("You need to enter Y, N, Yes, or No.")

