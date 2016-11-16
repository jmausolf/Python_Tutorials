import sys
sys.path.append('sklearn_magicloops')
from magicloops import *

#Define Data
dataset  = 'data/gss2014.csv'
outcome  = 'partyid_str_rep'
features = ['age', 'sex', 'race', 'educ']


#Run
main(dataset, outcome, features)
