# English to Pig Latin Translator
print("Enter the English message to translate into pig latin:")
message = input()

VOWELS = ("a", "e", "i", "o", "u", "y")

pig_latin = []

for word in message.split():# splits sentence message by spaces into list items ['My', 'name', ...etc] with .join() as the inverse
    # Seperate the non-letters at the start of this word (each on in the above list made from sentence)
    prefix_non_letters = ""
    while len(word) > 0 and not word[0].isalpha():
        # the [0] selects the first letter of each word in the list
        prefix_non_letters += word[0]
        word = word[1:]  # removes the first character in the word
    if len(word) == 0:  # this logic ensures if a space got added to the list and the value is thus  len(0) after split(),
        pig_latin.append(prefix_non_letters)  # it immediately appends it back to the list word item (undoing it all)
        continue  # important so that it goes on to the next word
    # Seperate the non-letters at the end of this word:
    suffix_non_letters = ""
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1] #removes the last character from this word
    # Remember if the word was in uppercase or title case:
    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower() # Make the word lowercase for translation

    # Seperate the consonants at the start of this word (perform pig latin translation):
    prefix_consonants = ""
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0] #adds consonant to variable named prefix_consonants
        word = word[1:] #removes the consonant at the start of each word
    # Add the pig latin ending to the word
    if prefix_consonants != "":
        word += prefix_consonants + "ay"
    else:
        word += "yay"
    
    #Set the word back to uppercase or title case:
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
    
    # Add the non-letters back to the start or end of the word.
    pig_latin.append(prefix_non_letters + word + suffix_non_letters) 
    # word in the middle has non-letters removed above, so they get added back AFTER translation

# As was said before, the words are joined together into the pig_latin list and printed
print(" ".join(pig_latin))

