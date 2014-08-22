# Data Pipelining Talk @ PyGotham
by Sarah Guido (works @Reonomy)

michigan

nyc py organizer + pygotham organizer

birds eye overview

pandas
scikit-learn
nltk
MRjob
matplotlib

lots of online and offline documentation, books, videos, and tutorials

somewhat ease of use

domain knowledge is extremely helpful + useful


## Preprocessing
Wrangling, Munging, Manipulating
Getting to know your data, do you have missing values?  Are there duplicate values?  Do you need more or less data than you currently have?

Favorite preprocessing tool is Pandas:
Similar to R and Excel
Easy to use data structures:
    DataFrame
Wrangling:
    Merging
    Pivoting
    Joins
    
Keep everything in Python
Community support / resources
File I/O, cleaning, manipulation
Combinable with other modules
numby, scipy, statsmodel, matplotlib

## Machine Learning

algorithms
represneations
useful in everyday life
useful in data analysis


supervised learning
    classifications and regression
    
unsupervised learning
    clustering
    dimensionality reduction
    unlabeled data
    not sure what data is offering

Best python ml lib is scikit-learn:
* open source
* good documentation

## Natural Language Processing

The same word can have different meanings in differnt contexts

Most NLP algos are based on ML

Python has NLTK (natural language toolkit)
    
* Access to over 50 corpora
* NLP tools: stemming, tokenizing
* Good resources for learning

Other things you can do:
* lemmatizing, tokenization, tagging, parse trees
* classification
* chunking
* sentence structure

## Processing Large Data - MapReduce

Data that takes too long to process on your machine

Solution is MapReduce: procsesing with large datasets on distributed system in parallel

### Map step:
takes series of key/value pairs
### Reduce step:
once for each unique key, iterates blah blah

### Python Library: MRjob

test code locally without installing hadoop
lots of thorough docs
a few things to keep in mind:
* keep everything in one class
* mrjob program in separate file
* output to new file

works on hadoop clusters
works with elastic search as well

## Data Visualization

You need to deliver your results in a meaningful way




