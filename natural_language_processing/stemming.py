__author__ = 'jason'


from nltk.corpus import gutenberg

', '.join(gutenberg.words()[:100])

# now we want to remove stop words

from nltk.corpus import stopwords
stop = stopwords.words('english')
stop_removed = [word for word in gutenberg.words() if word not in stop]

print(', '.join(stop_removed[:100]))

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in stop_removed]

print(', '.join(stemmed[:100]))