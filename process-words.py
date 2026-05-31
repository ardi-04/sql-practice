
def process_words(text):
    words = set() 
    wordsplitted =  text.split(" ")
    for word in wordsplitted:
        words.add(word)
    wordsDict = {'unique_words' : words , 'word_count' : len(wordsplitted) , 'first_word' : wordsplitted[0] ,'last_word' : wordsplitted[-1]}

    print(wordsDict)


process_words(input("Enter a sentence: "))