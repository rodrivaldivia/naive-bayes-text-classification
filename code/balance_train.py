import pandas as pd

all_files = [ "../data/happy.csv", "../data/sad.csv", "../data/angry.csv", "../data/hope.csv", ]

print('Reading files...');

# happy = 

dataframes = []
cropped = []
for f in all_files:
	dataframes.append(pd.read_csv(f, usecols=["text", "lang", "class"]))

# print(happy.info())
for df in dataframes:
	df = df.head(4700)
	df.info()
	cropped.append(df)

data = pd.concat(cropped)
data.info()
data.to_csv('../data/balanced_train.csv');
