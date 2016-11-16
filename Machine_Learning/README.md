#Machine Learning Tutorial

This module illustrates some basic machine learning in Python using Sci-Kit Learn.

We do not assume *a priori* that any single model will be best for the data. Instead, we loop over multiple classifiers and parameterizations. In this way, we can run hundreds of models and select the best one on a variety of metrics, such as precision and recall.

### Example Precision-Recall Plot:

![](results/example.png)

---

## Quick Start Guide

Example data for this repository comes from the [General Social Survey (GSS) 2014](http://gss.norc.org/get-the-data/stata). More notes on the data preprocessing are detailed in the [data](data/) folder.

To run the example:

```bash
git clone https://github.com/jmausolf/Python_Tutorials
cd Python_Tutorials/Machine_Learning
python run.py
```

---

## The Details

To modify the default data, outcome variable, or parameters, open the `run.py` script with your favorite text editor, such as Atom, Sublime, or Vim. Here, you must specify the dataset (as .CSV), the outcome variable you would like to predict (for binary classification), and the features you would like to use to make the predictions.

#### Default Example:

```python
#Define Data
dataset  = 'file'
outcome  = 'partyid_str_rep'
features = ['age', 'sex', 'race', 'educ', 'rincome']
```

Once you edit these fields, save the script, and in terminal execute: `python run.py`

#### Note:

Your data may have hundreds of features (independent variables/predictors). If you would like to use all of them (and would rather not type write them all out explicitly) simply uses the `--all_features` option of the magic loop.

```bash
python run.py --all_features True
```

Of course, an overlooked aspect thus far is feature development. The GSS data in the example is not in the ideal form. For example, most of the data is categorical. We might want to make indicators for each categorical column, calculate various aggregations or interactions, among other possibilities. An ideal data pipeline might make the changes to the feature set prior running this script.

---

## Acknowledgements

This tutorial makes use of a [modified submodule](https://github.com/jmausolf/magicloops), originally forked from @rayidghani [magicloops](https://github.com/rayidghani/magicloops). It has been updated to run in Python2 or Python3. In addition, my modified fork modifies the plotting code and several of the functions to take a user-specified dataset, outcome variable, and features.
