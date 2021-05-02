class Word_Bank:
    def __init__(self):
        self.words = []

    def addWord(self, word, translation):
        new_word = {word: translation}
        self.words.append(new_word)

    def removeWord(self, word):
        # Check to see if list is empty
        if len(self.words) == 0:
            return self.words

        # Find the key that matches the word we want to remove
        for i in range(len(self.words)):
            key = list(self.words[i].keys())[0] # Get the Value of the Key

            if key == word:
                self.words.remove(self.words[i])
            else:
                print("{0} does not exist".format(word))

    # You can add a list of words to the existing self.words[] attribute
    def mergeListOfWords(self, list_of_words):
        self.words.extend(list_of_words)


