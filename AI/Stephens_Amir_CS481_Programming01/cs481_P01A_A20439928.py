'''
Amir Stephens, A20439928 Part A.
'''
import nltk
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

'''
A method to find the frequency of the words in a corpus, with removing the stopwords. Most of this code was taken from Notebook 10a.
'''
def frequency(words):
    stopwords = nltk.corpus.stopwords.words('english')
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
Simple method to print out the first 10 items of the list.
'''
def top_10(frequency_list):
    print(frequency_list[:10])
    print("---------")
'''
Log plot function. Most of the code is from notebook 10a. I
'''
def log_plot(frequency_list, number, title):
    words, frequencies = map(list, zip(*frequency_list))
    _, ax = plt.subplots()
    x_axis = range(len(words))
    y_axis = range(len(words))

    def format_fn(tick_val, tick_pos):
        if int(tick_val) in x_axis:
            return y_axis[int(tick_val)]
        else:
            return ''

    ax.xaxis.set_major_formatter(format_fn)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.plot(x_axis[:number], frequencies[:number])
    ax.set_title("%s log(rank) vs log(frequency) plot" % title)
    ax.set_xscale("log")
    ax.set_yscale("log")
    plt.xlabel("log(Rank)")
    plt.ylabel("log(Frequency count)")
    plt.show()
'''
This method is used to find the probability a single word appears in a corpus. It takes a word, a word list, and a frequency list.
'''
def unigram_occurence(word, word_list, frequency_list):
    words, frequencies = map(list, zip(*frequency_list))
    for i in range(len(words)):
        if word.lower() == words[i].lower():
            return (frequencies[i]/len(word_list))
    return 0
'''
This is to get the corpuses I'll be working with along with the stop words.
'''
if  nltk.corpus.gutenberg == None or nltk.corpus.reuters == None or nltk.corpus.brown == None:
    nltk.download("reuters")
    nltk.download("brown")
    nltk.download("gutenberg")
corpus_brown = nltk.corpus.brown
corpus_gutenberg = nltk.corpus.gutenberg
corpus_reuters = nltk.corpus.reuters

words_brown = corpus_brown.words()
words_reuters = corpus_reuters.words()
words_gutenberg = corpus_gutenberg.words()
'''
Frequency distribution / top ten ranking.
'''
frequency_brown = frequency(words_brown)
frequency_reuters = frequency(words_reuters)
frequency_gutenberg = frequency(words_gutenberg)

top_10(frequency_brown)
top_10(frequency_reuters)
top_10(frequency_gutenberg)
'''
Log(rank) vs log(frequency) plots.
'''
log_plot(frequency_brown, 1000, "Brown")
log_plot(frequency_reuters, 1000, "Reuters")
log_plot(frequency_gutenberg, 1000, "Gutenberg")
'''
Unigram occurrence.
'''
print("Brown: ", unigram_occurence("combustion", words_brown, frequency_brown))
print("Reuters: ", unigram_occurence("combustion", words_reuters, frequency_reuters))
print("Gutenberg: ", unigram_occurence("combustion", words_gutenberg, frequency_gutenberg))

print("Brown: ", unigram_occurence("home", words_brown, frequency_brown))
print("Reuters: ", unigram_occurence("home", words_reuters, frequency_reuters))
print("Gutenberg: ", unigram_occurence("home", words_gutenberg, frequency_gutenberg))