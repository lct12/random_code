# this code trains a neural network on a list/series of raw documents 

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
import time
from gensim.models import Word2Vec
import os 
from os import sep 
from code_snippets import convertNumbers
cwd = os.getcwd()

# This function takes in a list or series of raw documents and then trains a Word2Vec neural network 
def trainW2V(rawList,pickle=True, modelName='w2v',type='skip-gram',hs=0,negative=5,ns_exponent=0.75,sample=0.001,
	vector_size=300,window=10,min_count=3,workers=4,returnTokenized=True,trainModel=True):
	# set pickle to true to pickle the model
	# model name = the name you want to save your model under
	# type = model type: skip-gram or cbow
	# hs: hierachial softmax. Set to 1 if you want to use HS, set to 0 to use negative sampling
	# negative: specifiies how many 'noise words' should be drawn when using negative sampling
	# ns exponent = exponent used to select which words are sampled during negative sampling. 0.75 comes from original word2vec paper
		# 1.0 = all frequencies are exactly in proportion to frequency in corpus; 0.0 = equal frequencies
	# sample = number for configuring which higher-frequency words are randomly downsampled (see equation in neural network notes)
	# vector_size = size of the embeddings vector. Larger = better but more computationally intensive usually
	# window = size of context window. Larger is usually better but more comp. intensive
	# min_count = minimum number of times a word must show up in the sample for it to be included in the training
	# workers = used to parallelize the computation, but only if you have Cython installed. Lifts the GIL.
	# set returnTokenized = True to return the tokenized list of the documents
	# set trainModel = True to train the w2v model

	# begin by tokenizing the document list
	print('tokenizing the list!')
	rawTokenizedList = [tokenizer.tokenize(document.rstrip().lower()) for document in rawList]

	# change numbers in list into words
	tokenizedList = [convertNumbers(document) for document in rawTokenizedList]
	if trainModel == False:
		return tokenizedList
	# if trainModel = True, continue on to train the model
	if type == 'skip-gram':
		sg = 1
	elif type == 'cbow':
		sg = 0
	# train the model
	start = time.time()
	print(f"Time to train {type} Word2Vec model {modelName}:\n")
	model = Word2Vec(sentences=tokenizedList, hs=hs,negative=negative,ns_exponent=ns_exponent,sample=sample,
	vector_size=vector_size,window=window,min_count=min_count,workers=workers)
	end = time.time()
	print(end - start)
	if pickle == 'True':
		model.save(f'{cwd}{sep}pickle{sep}{modelName}.model')
	if returnTokenized == True:
		return model, tokenizedList
	else:
		return model




