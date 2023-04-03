# Contains the functions for preprocessing and creating counter for NLP

from collections import Counter, defaultdict
import pandas as pd
import spacy
import gensim
import pickle
import os
import re

from os import sep

# Import stopwords
from nltk.corpus import stopwords


# Generate functions that will be used in the preprocessing of the documents
# Create function to clean up each document (get rid of emojis, etc.)
def clean_documents(document_list):
    for document in document_list:

        # Remove new line or '\r' characters
        document = re.sub('\n', ' ', document)
        document = re.sub('\r', ' ', document)
        document = re.sub('-', '', document)
        document = re.sub('/', ' ', document)
        yield(gensim.utils.simple_preprocess(str(document), deacc=True))
        
# Make function to remove stopwords 
def remove_stopwords(document_list,language='english'):
    stop_words = stopwords.words(language)
    return [[word for word in document if word not in stop_words] for document in document_list]

def create_bigram_model(document_words, min_count=5,threshold=100):
    # min_count = minimum number of times two words must co-occur to be considered a bigram
    # threshold = higher = more difficult to be tagged as a bigram
    # Document words = list of lists (list of words within list of documents) that are cleaned and w/stopwords removed
    bigram = gensim.models.Phrases(document_words, min_count=min_count, threshold=threshold) 
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    return [bigram_mod[document] for document in document_words]

def create_trigram_model(document_words, min_count=5,threshold=100):
    # Create trigrams, but you must create a bigram model first
    bigram = gensim.models.Phrases(document_words, min_count=min_count,threshold=threshold)
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram = gensim.models.Phrases(bigram[document_words], min_count= min_count, threshold=threshold) 
    trigram_mod = gensim.models.phrases.Phraser(trigram)
    return [trigram_mod[bigram_mod[document]] for document in document_words]

# Make functions to lemmatize data (model varies by language)
def lemmatization(texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'], language='english'):
    spacyModelDict = {'english':'en_core_web_sm', 'spanish': 'es_core_news_sm',
                    'french': 'fr_core_news_sm', 'german': 'de_core_news_sm',
                    'portuguese': 'pt_core_news_sm', 'italian': 'it_core_news_sm',
                    'dutch':'nl_core_news_sm'}
    spacyModel = spacyModelDict[language]
    
    # Load tokenizer model from SPACY, disable parser, ner (for lemmatization)
    nlp = spacy.load(spacyModel, disable=['parser', 'ner'])
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
    return texts_out

# Now, create function that preprocesses the data given a list, where every item in the list = a document
# and the entire list = a corpus. Returns the lemmatized corpus (along with the pre-lemmatized no-stops corpus).
# If bigram = True, then returns the documents with bigrams included. See above for min count and threshold def'n    
# Fix the language here using language ID!!!!
def preprocess_document_data(document_list, bigram=False,trigram=False,lemmatize_nograms=True,
                            min_count=5,threshold=100, lang='eng'):
    langDict = {'en':'english','fr':'french','de':'german','es':'spanish','pt':'portuguese', 'it':'italian','nl':'dutch'}
    language = langDict[lang]
    print(f'Starting the preprocessing of {language.title()} documents...')
    # Clean up tweets
    document_words = list(clean_documents(document_list))
    print('documents cleaned!')    
    
    # Remove stopwords
    documents_nostops = remove_stopwords(document_words,language=language)
    print('stopwords removed!')
    
    # Make bigrams (if bigram=True)
    if bigram ==True:
        documents_bigrams = create_bigram_model(documents_nostops,min_count=min_count, threshold=threshold)
        print('bigrams created!')
    
        # Create lemmatized documents from the bigrams data
        bigrams_lemmatized = lemmatization(documents_bigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'],language=language)
        print('bigrams are lemmatized!') 

    # Make trigrams (if trigram = True). Do not set both bigrams=True and Trigrams=True
    elif trigram==True:
        documents_trigrams = create_trigram_model(documents_nostops,min_count=min_count,threshold=threshold)
        print('trigrams created!')
    
        # Create lemmatized documents from the bigrams data
        trigrams_lemmatized = lemmatization(documents_trigrams, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'],language=language)
        print('trigrams are lemmatized!') 

    if lemmatize_nograms==True:
        # Create lemmatized documents from non-bigram/trigram data
        documents_lemmatized = lemmatization(documents_nostops, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV'],language=language)
        print('documents are lemmatized!')
    
    if bigram==True and lemmatize_nograms == True:
        # Return lemmatized non-bigram, lemmatized bigram and non-lemmatized non-bigram documents (only use lemmatized if it sig. improves performance)
        return bigrams_lemmatized, documents_nostops, documents_lemmatized,language

    elif bigram==True and lemmatize_nograms == False:
        return bigrams_lemmatized, documents_nostops,language

    elif trigram==True and lemmatize_nograms == True:
        # Return lemmatized non-trigram, lemmatized tri and non lemmatized non tri documents
        return trigrams_lemmatized, documents_nostops, documents_lemmatized,language
    elif trigram==True and lemmatize_nograms==False:
        return trigrams_lemmatized, documents_nostops,language
    else:
        # Return lemmatized and non-lemmatized documents (only use lemmatized if it sig. improves performance)
        return documents_lemmatized, documents_nostops,language

# Define function to create counter dictionary where document_list = list of cleaned and/or lemmatized documents
# Set documentCounter = True if you want to count the number of documents containing a word, rather than the number of times a word appears 
# (Recall that a word can appear multiple times in the same document)
def create_counter_dict(document_list, documentCounter=False):
    # Create a list of all words in the documents
    if documentCounter == True:
        word_list = [w for r in document_list for w in set(r)]
    else:
        word_list = [w for r in document_list for w in r]
    # Create a dictionary of words and corresponding frequency counts using a Counter
    vocab_dict = Counter(word_list)
    return vocab_dict
