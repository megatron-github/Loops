"""
 *****************************************************************************
   FILE:          alphabet.py

   DESCRIPTION:	Find words in the alphabet that did not used in a phrase
   
                  Here is a sample interaction with the program.
                  Enter some text: The quick brown fox ate 4 rotten eggs and 
                                   said "YUCK!"
                  Letters not in the text: JLMPVZ


 *****************************************************************************
"""
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    """ This program tell you what words was not use in a phrase"""
      
    given_words = input("Enter some text: ")
    given_words = given_words.upper()
    unsused_letter = ""
    for letter in ALPHABET:
        if letter not in given_words:
            unsused_letter = unsused_letter + letter

    print("Letters not in the text: {}".format(unsused_letter))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
