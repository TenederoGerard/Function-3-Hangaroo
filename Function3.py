def getAvailableLetters(lettersGuessed):

    alphabet= ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
    letter = " "
    for i in alphabet:
        if i not in lettersGuessed:
            letter += i
    return letter 

