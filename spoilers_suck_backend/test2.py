import gensim
from nltk.corpora import *

def cleanDoc(doc):
    stopset = set(stopwords.words('english'))
    stemmer = nltk.PorterStemmer()
    tokens = WordPunctTokenizer().tokenize(doc)
    clean = [token.lower() for token in tokens if token.lower() not in stopset and len(token) > 2]
    final = [stemmer.stem(word) for word in clean]
    return final

dictionary = corpora.Dictionary(line.lower().split() for line in open('spoilers.txt'))
print len(dictionary)