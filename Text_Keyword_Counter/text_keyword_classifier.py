###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    University of Chicago    ###
###                             ###
###################################

import re
import pandas as pd
import numpy as np
import glob
import os
import nltk
from nltk import word_tokenize



##########################################################
#Preliminary Functions
##########################################################

def group_text(text, group_size):
    """
    This function groups a text into text groups.
    It returns a list of grouped strings.
    """
    word_list = text.split()
    group_list = []
    for k in range(len(word_list)):
        start = k
        end = k + group_size
        group_slice = word_list[start: end]

        # Append only groups of proper length/size
        if len(group_slice) == group_size:
            group_list.append(" ".join(group_slice))
    return group_list


def remove_non_ascii_2(text):
	import re
	return re.sub(r'[^\x00-\x7F]+', "", text)


def read_speech(speechfile):
    speech = str(speechfile)
    f = open(speech, 'rU')
    raw = f.read()
    raw1 = raw.replace('.', ' ')
    sent = remove_non_ascii_2(raw1)
    return sent

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


def get_url(speechfile):
    speech = str(speechfile)
    f = open(speech, 'rU')
    raw = f.read()
    sent = remove_non_ascii_2(raw)
    url = sent.split('\n')[1]
    return url


def get_group_set(group_size, text):
	group_list = group_text(text, group_size)
	group_set = set(group_list)
	return group_set


def ngram(n, data):
	ngram = get_group_set(n, data)
	return ngram




##########################################################
#Speech Phrase Counter Functions
##########################################################


def find_time(text):
	#Add Time to Data Frame
	try:
		try:
			time = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
			return time[0]
		except:
			try:
				time = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
				return time[0]
			except:
				time = re.findall(r'\d{1,2}(?:(?:AM|PM)|(?::\d{1,2})(?:AM|PM)?)', sent)
				return time[0]
	except:
		pass



def return_time(text):
	#Add Time to Data Frame
	try:
		try:
			time0 = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
			time = time0[0].replace('P M ', 'PM').replace('A M ', 'AM')
			return time
		except:
			try:
				time = re.findall(r'\d{1,2}:\d{1,2}\s[A-Z].[A-Z].+', sent)
				return time[0]
			except:
				time = re.findall(r'\d{1,2}(?:(?:AM|PM)|(?::\d{1,2})(?:AM|PM)?)', sent)
				return time[0]
	except:
		pass


def speech_phrase_counter(ngram1, ngram2, ngram3, ngram4, terms, df, n, sent):

	"""
	This function counts the occurence of ngrams of size 1, 2, 3, and 4.
	These are defined externally.
	--------------------------------------------------------------------
	It requires a list of terms. These can be of any number of ngrams
	sizes 1-4.
	--------------------------------------------------------------------
	This function also requires a data frame (df). This should be
	a Pandas data frame in memory. It also requires an index term, n,
	to add the counts to the correct cell in the df.
	--------------------------------------------------------------------
	The sent term is the processed text returned from
	read_speech(speechfile)
	--------------------------------------------------------------------
	NOTE: This function is designed to be called within the function
	speech_classifier.
	--------------------------------------------------------------------
	"""

	for term in terms:
		for gram in ngram4:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram3:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram2:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count
		for gram in ngram1:
			if term == gram:
				count = sent.count(gram)
				df.ix[n, term] = count



##########################################################
#Setup Data Frame
##########################################################


def speech_classifier(folder_name, ds1, ds2, output_file, terms, metric=0, addtime=0, addloc=0, addcite=0):
	"""
	---------------------------------------------------------------
	Variables
	-	folder_name = path/name of folder where speeches are found
	---------------------------------------------------------------
	- 	ds1:ds2 	= - date slices of filenames
					E.g. the filename "2011-09-17_ID1.txt"
						would want date slices of
						ds1 = 0 and ds2 = 10
						This takes the string slice 0:10
						and provides a date = 2011-09-17
	---------------------------------------------------------------
	- output_file 	= the name of the desired CSV
	---------------------------------------------------------------
	- terms			= the list of terms to look for in the speeches
	---------------------------------------------------------------
	- metric  		= option to add tokens, alphanumberic words,
						and vocabulary metrics to dataset
						using NLTK
	---------------------------------------------------------------
	- addtime 		= option to try to extract time terms
						default=0 == ignore (1 = run)
	---------------------------------------------------------------
	- addloc 		= option to try to extract location terms
						default=0 == ignore (1 = run)
	---------------------------------------------------------------
	- addcite 		= option to try to extract url Citation
						default=0 == ignore (1 = run)
						this works for text files where the parser
						adds the parsed URL to the first line of the
						speech file.
	---------------------------------------------------------------
	"""

	#Setup Initial Data Frame
	header = ["DATE", "TIME", "LOCATION", "URL", "TOKENS", "WORDS", "UNIQUE_WORDS"]+terms
	index = np.arange(0)
	df = pd.DataFrame(columns=header, index = index)


	#Get Files in Folder
	folder = str(folder_name)
	outfile = str(output_file)
	os.chdir(folder)
	speech_files = glob.glob("*.txt")


	for speech in speech_files:
		date = speech[ds1:ds2]
		print ("Analyzing speech file {} ... {}".format(speech, date))
		n = len(df.index)

		#Add Row to Data Frame
		df.loc[n] = 0
		df.ix[n, "DATE"] = date


		sent = read_speech(speech)

		#Add Time to Data Frame
		if addtime == 1:
			time = return_time(sent)
			if len(str(time)) > 15:
				time = str(time)[0:12]
			else:
				pass
			df.ix[n, "TIME"] = time
		else:
			pass


		#Add Location
		if addloc == 1:
			try:
				time_ = find_time(sent)
				location0 = sent
				location1 = location0.replace(time_, '|').split('|', 1)[0]
				location2 = location1.replace('\n\n', '|').replace('|\n', '|').replace('| ', '').split('|')
				X = len(location2)-2
				location3 = location2[X]
				location = location3.replace('\n', ', ').replace('\t', '')
			except:
				location = ''
				pass

			if len(str(location)) > 25:
				location = str(location)[0:35]
				print ("Exception: {} ...".format(location))
			else:
				pass
			df.ix[n, "LOCATION"] = location
		else:
			pass

		#Add Citation/URL
		if addcite == 1:
			url = get_url(speech)
			df.ix[n, "URL"] = url
		else:
			pass


		#Add Tokens, Words, Unique Words
		if metric==0:
			pass
		else:
			text = make_text(speech)
			words = [w.lower() for w in text if w.isalpha()]
			df.ix[n, "TOKENS"] = len(text)
			df.ix[n, "WORDS"] = len(words)
			df.ix[n, "UNIQUE_WORDS"] = len(set(words))


		#Add Keyword Data
		ngram1 = get_group_set(1, sent)
		ngram2 = get_group_set(2, sent)
		ngram3 = get_group_set(3, sent)
		ngram4 = get_group_set(4, sent)

		#Count Keywords
		speech_phrase_counter(ngram1, ngram2, ngram3, ngram4, terms, df, n, sent)

	os.chdir("..")
	print (df)
	df.to_csv(outfile, encoding='utf-8')
	return df
