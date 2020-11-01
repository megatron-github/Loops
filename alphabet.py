"""
 *****************************************************************************
   FILE:        alphabet.py

   AUTHOR:		Truong Pham

   ASSIGNMENT:	Project 3: Part 1: Alphabet

   DATE:		9/11/18

   DESCRIPTION:	Find words in the alphabet that did not used in a phrase

 *****************************************************************************
"""
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    """ This program tell you what words was not use in a phrase"""
    given_words = input("Enter some text: ")
    given_words = given_words.upper()
    unsused_letter = ""
    for letter in ALPHABET:
        #Cite: Peer Lucas Barusik 
        #Desc: Explain how "if__not in__" statement exists
        #and how to use it
        if letter not in given_words:
            unsused_letter = unsused_letter + letter

    print("Letters not in the text: {}".format(unsused_letter))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
