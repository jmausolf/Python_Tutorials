import os
import glob
import numpy as np
import pandas as pd
import sklearn.feature_extraction.text as text
from sklearn import decomposition
import nltk
from nltk import word_tokenize

#from nltk.tokenize import TreebankWordTokenizer
import re

def remove_non_ascii_2(text):
	import re
	return re.sub(r'[^\x00-\x7F]+', "", text)

def make_text(file, path=''):
    if path=='':
        filepath = file
    else:
        filepath = path+"/"+file

    f = open(filepath)
    raw0 = f.read()
    raw1 = remove_non_ascii_2(raw0)
    tokens = word_tokenize(raw1)
    text = nltk.Text(tokens)
    return text

def tokenize_nltk(text):
    tokens = word_tokenize(text)
    text = nltk.Text(tokens)
    words = [w.lower() for w in text if w.isalpha()]
    return words



#Define Corpus Path and Files
#file_path = os.path.join('data', 'president')
#file_path = os.path.join('data', 'Speech_President')
#file_path = os.path.join('data', 'twitter')
print(file_path)

os.chdir(file_path)
filenames = glob.glob("*.txt")
#filenames = glob.glob("*.csv")

#rawcsv = "Hillary_Tweets.csv"
#twitter = pd.read_table(rawcsv, sep=",")
#filenames = twitter['TWEET']

def select_files(text_or_tweet, file_path="."):

	print(file_path)
	os.chdir(file_path)

	if text_or_tweet == "text":
		filenames = glob.glob("*.txt")
	elif text_or_tweet == "tweet":
		rawcsv = "Hillary_Tweets.csv"
		twitter = pd.read_table(rawcsv, sep=",")
		filenames = twitter['TWEET']

	return filenames

select_files("tweet", "data/twitter")

def select_vectorizer(vectorizer_type, req_ngram_range=[1,2]):

	"""
	Select the desired vectorizer for either text or tweet
	@ text_tfidf_std
	@ text_tfidf_custom
	@ text_count_std

	@ tweet_tfidf_std
	@ tweet_tfidf_custom
	"""

	# SPECIFY VECTORIZER ALGORITHM
	#---------------------------------#

	ngram_lengths = req_ngram_range

	if vectorizer_type == "text_tfidf_std":
		# Standard TFIDF Vectorizer (Text)
		vectorizer = text.TfidfVectorizer(input='filename', analyzer='word', ngram_range=(ngram_lengths), stop_words='english', min_df=2)
		return vectorizer
	elif vectorizer_type == "text_tfidf_custom":
		# TFIDF Vectorizer with NLTK Tokenizer (Text)
		vectorizer = text.TfidfVectorizer(input='filename', analyzer='word', ngram_range=(ngram_lengths), stop_words='english', min_df=2, tokenizer=tokenize_nltk)
		return vectorizer
	elif vectorizer_type == "text_count_std":
		vectorizer = text.CountVectorizer(input='filename', analyzer='word', ngram_range=(ngram_lengths), stop_words='english', min_df=2)
		return vectorizer
	elif vectorizer_type == "tweet_tfidf_std":
		# Standard TFIDF Vectorizer (Content)
		vectorizer = text.TfidfVectorizer(input='content', analyzer='word', ngram_range=(ngram_lengths), stop_words='english', min_df=2)
		return vectorizer
	elif vectorizer_type == "tweet_tfidf_custom":
		print(vectorizer_type)
		# Standard TFIDF Vectorizer (Content)
		vectorizer = text.TfidfVectorizer(input='content', analyzer='word', ngram_range=(ngram_lengths), stop_words='english', min_df=2, tokenizer=tokenize_nltk)
		return vectorizer
	else:
		print("error")
		pass

#select_vectorizer("text_count_custom", 5, 15, [1,2])
#x = select_vectorizer("tweet_tfidf_std", [1,2])
#print(x)

print("Selecting {} files from {}...".format(len(filenames), file_path))

def topic_modeler(vectorizer_type, n_topics, n_top_terms, req_ngram_range=[1,2]):

	"""
	Select the desired vectorizer for either text or tweet
	@ text_tfidf_std
	@ text_tfidf_custom
	@ text_count_std

	@ tweet_tfidf_std
	@ tweet_tfidf_custom
	"""

	#Specify Number of Topics, Ngram Structure, and Terms per Topic
	num_topics = n_topics
	num_top_words = n_top_terms
	ngram_lengths = req_ngram_range


	# SPECIFY VECTORIZER ALGORITHM
	vectorizer = select_vectorizer(vectorizer_type, ngram_lengths)


	# Vectorizer Results
	dtm = vectorizer.fit_transform(filenames).toarray()
	vocab = np.array(vectorizer.get_feature_names())
	print("Evaluating vocabulary...")
	print("Found {} terms in {} files...".format(dtm.shape[1], dtm.shape[0]))


	# DEFINE and BUILD MODEL
	#---------------------------------#

	#Define Topic Model
	clf = decomposition.NMF(n_components=num_topics+1, random_state=3)

	#Fit Topic Model
	doctopic = clf.fit_transform(dtm)
	topic_words = []
	for topic in clf.components_:
	    word_idx = np.argsort(topic)[::-1][0:num_top_words]
	    topic_words.append([vocab[i] for i in word_idx])


	# Show the Top Topics
	for t in range(len(topic_words)):
	    print("Topic {}: {}".format(t, ', '.join(topic_words[t][:])))


#topic_modeler("tweet_tfidf_std", 10, 5, [1,3])
#topic_modeler("text_tfidf_std", 10, 5, [1,3])
