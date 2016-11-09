

# Welcome to Text Keyword Counter

This package allows you to analyze a set of `.txt` text files and quantify the count of a given set of keywords and phrases. It returns a .CSV of the results, which can be used to generate various graphs:

### [Discussion of Guns by President Obama and Congress, 2009-2016](https://public.tableau.com/views/DiscussionofGunsbyPresidentObamaandCongress2009-2016/Story1?:embed=y&:display_count=yes)

![Discussion of Guns by President Obama and Congress, 2009-2016](presidential_congressional_discussion_of_guns.png)
---

# Dependencies

To run this package, you will need several functions.

1. This package was written on and assumes you are running a Mac system, not Linux.
2. This package requires an Anaconda Distribution of Python, either 2.7+ or 3.5+
	* see https://www.continuum.io/downloads


# To Run

1. Git clone this [repository](https://github.com/jmausolf/Python_Tutorials) and navigate to the tutorial:

```bash
git clone https://github.com/jmausolf/Python_Tutorials
cd Python_Tutorials/Topic_Models_for_Text/
```


2. Run one of the examples:

##### Run a Non-Negative Matrix Factorization (NMF) topic model using a TFIDF vectorizer with custom tokenization

```bash
# Run the NMF Model on Presidential Speech
python topic_modelr.py "text_tfidf_custom" "nmf" 15 10 2 4 "data/president"

```

##### Run a Latent Dirichlet Allocation (LDA) topic model using a TFIDF vectorizer with custom tokenization

```bash
# Run the LDA Model on Clinton Tweets
python topic_modelr.py "tweet_tfidf_custom" "lda" 15 5 1 4 "data/twitter"

```
