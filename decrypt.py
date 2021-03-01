def lassoLetter (letter, shiftAmount ):
    # Translate letter to ACII Code and store in letterCode Variable
    letterCode = ord(letter.lower())

    # The ASCII representation of a lower case letter
    aAscii = ord('a')

    # Number of english alphabets
    alphabetSize = 26

    # Calculate the ASCII number for the decoded letter
    # Take into account looping around the alphabets
    trueLetterCode = aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize)

    # Convert ASCII number to character
    decodedLetter = chr(trueLetterCode)

    # Send the decoded letter back
    return decodedLetter


def lassoWord (word, shiftAmount):
    # Update variable each time letter is decoded
    decodedWord = ""

    # Iterate through all letters in the word parameter
    for letter in word:
        # Call lassoLetter() and save the return value in decodedLetter variable
        decodedLetter = lassoLetter(letter, shiftAmount)

        # Add decodedLetter value to the end of the decodedWord value
        decodedWord = decodedWord + decodedLetter

    # Return the value of decodedWord
    return decodedWord


# Decrypt Message
print( "Shifting WHY by 13 gives: \n" + lassoWord( "WHY", 13 ) )
print( "Shifting WHY by 13 gives: \n" + lassoWord( "oskza", -18 ) )
print( "Shifting WHY by 13 gives: \n" + lassoWord( "ohupo", -1 ) ) 
print( "Shifting WHY by 13 gives: \n" + lassoWord( "ED", 25 ) )
print(lassoLetter('p', -2))
