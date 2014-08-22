__author__ = 'jason'


# lets count all words in gutenberg

from mrjob.job import MRJob

class MRWordFreqCount(MRJob):

    def mapper(self, _, line):
        line = line.split()
        for word in line:
            word = word.strip('.,afsdfsd")')
            if True:
                yield word

    def reducer(self, stuff):
        pass