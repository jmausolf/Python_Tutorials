import sys, argparse, textwrap
sys.path.append('sklearn_magicloops')
from magicloops import *

############################################################
# 1.   USER INPUT: Define Your Data, Outcome, and Features
############################################################

#Define Data
dataset  = 'data/gss2014.csv'
outcome  = 'partyid_str_rep'
features = ['age', 'sex', 'race', 'educ', 'rincome']


############################################################
# 2.   RUN THE MODELS
############################################################

# Save Changes and Open Terminal
# In terminal:
# python run.py             #Runs for defined features
# python run.py -a True     #Runs all possible features

# Help:
# python run.py -h

############################################################

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Prepare input file',
            formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-a', '--all_features', default=False, type=bool,
        help=textwrap.dedent("""\
            Option to run magic loop for all features in dataset
            except for the outcome variable.
            @ False     | Runs only specified features (defined in run.py)
            @ True      | Runs all features except outcome (defined in run.py)
            """
            ))


    args = parser.parse_args()
    main(dataset, outcome, features, args.all_features)
