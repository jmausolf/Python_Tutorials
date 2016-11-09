

# Welcome to Topic Model Tutorial

This package allows you to analyze a set of `.txt` text files or a dataset of Twitter tweets using topic model algorithms from [SciKit-Learn](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.decomposition

# Dependencies

To run this package, you will need several functions.

1. This package was written on a MAC OSX system. It has not been tested on Linux or Windows.
2. This package requires an Anaconda Distribution of Python, either 2.7+ or 3.5+
	* see https://www.continuum.io/downloads. Although these packages should be included, you can install them if needed:

	* Sci-Kit Learn `pip install sklearn`
	* NLTK `pip install NLTK`


# To Run

1. Git clone this [repository](https://github.com/jmausolf/Python_Tutorials) and navigate to the tutorial:

	```bash
	git clone https://github.com/jmausolf/Python_Tutorials
	cd Python_Tutorials/Topic_Models_for_Text/
	```


2. Run one of the examples:

	###### Run a Non-Negative Matrix Factorization (NMF) topic model using a TFIDF vectorizer with custom tokenization

	```bash
	# Run the NMF Model on Presidential Speech
	python topic_modelr.py "text_tfidf_custom" "nmf" 15 10 2 4 "data/president"

	```

	###### Run a Latent Dirichlet Allocation (LDA) topic model using a TFIDF vectorizer with custom tokenization

	```bash
	# Run the LDA Model on Clinton Tweets
	python topic_modelr.py "tweet_tfidf_custom" "lda" 15 5 1 4 "data/twitter"

	```

# Diving Into the Code

To learn more about the code, please check out the [tutorial](https://github.com/jmausolf/Python_Tutorials/blob/master/Topic_Models_for_Text/Topic_Models_for_Text.Rmd)

To get help in running this function, consult the help file:

```bash
python topic_modelr.py --help

```

##### This yields the following:

```bash

usage: topic_modelr.py [-h]
                       vectorizer_type topic_clf n_topics n_top_terms
                       req_ngram_range [req_ngram_range ...] file_path

Prepare input file

positional arguments:
  vectorizer_type  Select the desired vectorizer for either text or tweet
                   @ text_tfidf_std       | TFIDF Vectorizer (for text)
                   @ text_tfidf_custom    | TFIDF Vectorizer with Custom Tokenizer (for text)
                   @ text_count_std       | Count Vectorizer

                   @ tweet_tfidf_std      | TFIDF Vectorizer (for tweets)
                   @ tweet_tfidf_custom   | TFIDF Vectorizer with Custom Tokenizer (for tweets)

  topic_clf        Select the desired topic model classifier (clf)
                   @ lda     | Topic Model: LatentDirichletAllocation (LDA)
                   @ nmf     | Topic Model: Non-Negative Matrix Factorization (NMF)
                   @ pca     | Topic Model: Principal Components Analysis (PCA)

  n_topics         Select the number of topics to return (as integer)
                   Note: requires n >= number of text files or tweets

                   Consider the following examples:

                   @ 10     | Example: Returns 5 topics
                   @ 15     | Example: Returns 10 topics

  n_top_terms      Select the number of top terms to return for each topic (as integer)
                   Consider the following examples:

                   @ 10     | Example: Returns 10 terms for each topic
                   @ 15     | Example: Returns 15 terms for each topic

  req_ngram_range  Select the requested 'ngram' or number of words per term
                   @ NG-1:  | ngram of length 1, e.g. "pay"
                   @ NG-2:  | ngram of length 2, e.g. "fair share"
                   @ NG-3:  | ngram of length 3, e.g. "pay fair share"

                   Consider the following ngram range examples:

                   @ [1, 2] | Return ngrams of lengths 1 and 2
                   @ [2, 5] | Return ngrams of lengths 2 through 5

  file_path        Select the desired file path for the data

                   Consider the following ngram range examples:

                   @ data/twitter      | Uses data in the data/twitter subdirectory
                   @ data/president    | Uses data in the data/president subdirectory
                   @ .                 | Uses data in the current directory


optional arguments:
  -h, --help       show this help message and exit

```
