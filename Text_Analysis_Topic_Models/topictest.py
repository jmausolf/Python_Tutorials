import os
import glob
#CORPUS_PATH = os.path.join('data', 'president')
CORPUS_PATH = os.path.join('data', 'Speech_President')
#filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])
#filenames = sorted([os.path.join(CORPUS_PATH, fn) for fn in os.listdir(CORPUS_PATH)])

os.chdir(CORPUS_PATH)
filenames = glob.glob("*.txt")

# files are located in data/president
print(len(filenames))
print(filenames[:5])

import numpy as np  # a conventional alias
import sklearn.feature_extraction.text as text
vectorizer = text.CountVectorizer(input='filename', stop_words='english', min_df=2)
dtm = vectorizer.fit_transform(filenames).toarray()

vocab = np.array(vectorizer.get_feature_names())
print(dtm.shape)
print(len(vocab))


from sklearn import decomposition
num_topics = 20
num_top_words = 25
clf = decomposition.NMF(n_components=num_topics+1, random_state=1)

#may take some time
doctopic = clf.fit_transform(dtm)
# print words associated with topics
topic_words = []
for topic in clf.components_:
    word_idx = np.argsort(topic)[::-1][0:num_top_words]
    topic_words.append([vocab[i] for i in word_idx])

doctopic = doctopic / np.sum(doctopic, axis=1, keepdims=True)
print(doctopic)

novel_names = []
for fn in filenames:
    basename = os.path.basename(fn)
    name, ext = os.path.splitext(basename)
    name = name.rstrip('0123456789')
    novel_names.append(name)

print(novel_names)

# turn this into an array so we can use NumPy functionsnovel_names = np.asarray(novel_names)
doctopic_orig = doctopic.copy()

# use method described in preprocessing section

num_groups = len(set(novel_names))
doctopic_grouped = np.zeros((num_groups, num_topics))
for i, name in enumerate(sorted(set(novel_names))):
    doctopic_grouped[i, :] = np.mean(doctopic[novel_names == name, :], axis=0)

doctopic = doctopic_grouped
print(doctopic)


novels = sorted(set(novel_names))

print("Top NMF topics in...")

for i in range(len(doctopic)):
    top_topics = np.argsort(doctopic[i,:])[::-1][0:5]
    top_topics_str = ' '.join(str(t) for t in top_topics)
    print("{}: {}".format(novels[i], top_topics_str))


# show the top 15 words
for t in range(len(topic_words)):
    print("Topic {}: {}".format(t, ' '.join(topic_words[t][:])))
