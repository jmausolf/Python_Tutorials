from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
import pandas as pd


# Define Data
df = pd.read_csv('data/gss2014.csv', index_col=0)
outcome  = 'partyid_str_rep'
features = ['age', 'sex', 'race', 'educ', 'rincome']

# Set, X, y, Train-Test Split
X, y = df[features], df[outcome]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Build Model and Fit
clf = RandomForestClassifier(n_estimators=10, max_depth=None,
    min_samples_split=2, random_state=0)
y_pred = clf.fit(X_train, y_train).predict_proba(X_test)[:,1]

# Calculate Result
result = metrics.roc_auc_score(y_test, y_pred)
print(result)
