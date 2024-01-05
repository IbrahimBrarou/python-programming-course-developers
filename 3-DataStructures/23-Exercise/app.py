sentence = "This is a common interview question"
letters = {letter: sentence.lower().count(letter)
           for letter in sentence.lower()}

most = sorted(letters.items(), key=lambda item: item[1], reverse=True)
print(most[0])
