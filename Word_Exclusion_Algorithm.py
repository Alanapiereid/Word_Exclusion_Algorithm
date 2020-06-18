import pandas as pd
import numpy
import string
import nltk
from nltk import word_tokenize, pos_tag
from nltk import everygrams
import math
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
import string

nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


#enter a string and a word list. Words will be excluded from the string that lie above the set frequency threshold
def exclude_list(input_string, dictionary_data):
    print('There are', len(dictionary_data), 'sentences in our corpus')
    df2 = pd.DataFrame(dictionary_data, columns=['Sentences'])
    my_text = df2['Sentences'].astype(str).values.tolist()
    corpus = []
    for line in my_text:
        words = nltk.word_tokenize(line.lower())
        for i in words:
            if i not in string.punctuation:
                corpus.append(i.lower())
    fdist = nltk.FreqDist(corpus)
    result = pd.DataFrame(fdist.most_common(100000),
                     columns=['Word', 'Frequency'])
    total_count = sum([int(y) for y in result.Frequency])
    print(total_count)
    exclude_words = []
    dict_ = dict(zip([x for x in result.Word], [int(y) for y in result.Frequency]))
    for i,j in dict_.items():
        equation_result = 1 - math.sqrt(10 ** -5 / (j/total_count))
        if equation_result > 0.96:
            exclude_words.append(i)
    #print('Here are the excluded words: \n\n\n', exclude_words)
    input_string = input_string.split()
    exclude = []
    for word in input_string:
        if word not in exclude_words:
            exclude.append(word)
    return exclude