'''
Amir Stephens, A20439928 Part B.
'''
import nltk

'''
Function for splitting a set of tokens into bigrams. This returns the bigrams and each bigrams frequency of occurence.
'''
def generature_bigram(tokens):
    bigrams = [(i.lower(), j.lower()) for i, j in zip(tokens, tokens[1:]) if i != " " or j != " "]
    bigram_frequency = dict()
    for i in bigrams:
        if i in bigram_frequency:
            bigram_frequency[i] += 1
        else:
            bigram_frequency[i] = 1
    return bigrams, bigram_frequency
'''
Code taken from part A to generate the frequency of unigrams.
'''
def frequency_unigram(words, stopwords):
    words = [word for word in words if word.lower() not in stopwords]
    frequencyDistribution = nltk.FreqDist(word.lower() for word in words)
    freqAndWords = dict()
    for word in words:
        freqAndWords[word] = frequencyDistribution[word]
    freqAndWords = list(freqAndWords.items())
    freqAndWords.sort(key = lambda a: a[1])
    freqAndWords.reverse()
    return freqAndWords
'''
This searches for the frequency of a unigram.
'''
def unigram_occurence(word, frequency_list):
    words, frequencies = map(list, zip(*frequency_list))
    for i in range(len(words)):
        if word.lower() == words[i].lower():
            return frequencies[i]
    return 0

if __name__ == "__main__":
    if  nltk.corpus.brown == None:
        nltk.download('brown')
    corpus_brown = nltk.corpus.brown
    words_brown = corpus_brown.words()
    corpus_stopwords = nltk.corpus.stopwords.words('english')
    frequency_brown = frequency_unigram(words_brown, corpus_stopwords)

    sentence = ""
    while sentence == "":
        sentence = input("Please enter a sentence: ")
        if sentence == "":
            print("Please enter a valid sentence.")
    sentence = sentence.lower()
    '''
    Code taken from Notebook 6 for tokenizing. I perform this type of tokenizing on the inputted string, just incase it is a more complex string.
    '''
    pattern = r"""(?x)                 # set flag to allow verbose regexps
                (?:[A-Z]\.)+           # abbreviations, e.g. U.S.A.
                |\d+(?:\.\d+)?%?       # numbers, incl. currency and percentages
                |\w+(?:[-']\w+)*       # words w/ optional internal hyphens/apostrophe
                |(?:[+/\-@&*])         # special characters with meanings
                """

    tokenizer = nltk.tokenize.regexp.RegexpTokenizer(pattern)
    tokens = tokenizer.tokenize(sentence)
    brown_bigrams, brown_bigram_frequency = generature_bigram(words_brown)
    sentence_bigrams, sentence_bigram_frequency = generature_bigram(tokens)

    words, frequencies = map(list, zip(*frequency_brown))
    for i in range(len(words)):
        words[i] = words[i].lower()
    '''
    This setion here is where the probability of the sentence appearing in the bigram takes place. We append start_end at the start and append 
    as these the professor said the start and end appear the same amoutnt of times.
    '''
    probabiliy_trail = [.25]
    for bigram in sentence_bigrams:
        if bigram[0] in words:
            probability = brown_bigram_frequency[bigram] / frequencies[0]
            print("%s: %s" % (str(bigram), str(probability)))
        else:
            probability = 0
            print("%s: 0" % str(bigram))
        probabiliy_trail.append(probability)
    probabiliy_trail.append(.25)
    probability_final = 1
    for i in probabiliy_trail:
        probability_final *= i
    print("Probably of sentence: %s" % probability_final)