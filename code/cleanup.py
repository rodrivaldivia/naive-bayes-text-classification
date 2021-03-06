import pandas as pd 
import re

data = pd.read_csv("../data/train.csv");
# data = pd.read_csv("test.csv");

data["text"] = data["text"].astype("string")
#lowercase
data["text"] = data["text"].str.lower()
#remove links and mentions
# data["text"] = data["text"].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", str(elem)))  
# remove numbers
# data["text"] = data["text"].apply(lambda elem: re.sub(r"\d+", "", elem))

data = data.loc[data['class'] == "happy"]
# data.to_csv('train_clean.csv');
data.to_csv('../happy.csv');

print(data.info())