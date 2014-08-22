__author__ = 'jason'


from nltk.corpus import gutenberg

', '.join(gutenberg.words()[:100])

# now we want to remove stop words

from nltk.corpus import stopwords

stop = stopwords.words('english')
stop_removed = [word for word in gutenberg.words() if word not in stop]

', '.join(stop_removed)

