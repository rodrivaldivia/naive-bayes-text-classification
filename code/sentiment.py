import os
import pandas as pd 

data = pd.read_csv("../data/train.csv", usecols=["text", "class"]);

data = data.head(200)

positive = 0;
negative = 0;

def sentimentIsPostive(sentimentResponse):
	if('positive' in sentimentResponse):
		return True;
	else:
		return False;

i = 0;
for index, row in data.iterrows():
	tweet = row['text'];
	command = "java -jar fastSentimentClassifier.jar \"" + tweet + "\"";
	ret = os.popen(command).read();

	if(sentimentIsPostive(ret) == True):
		positive+=1;
	else:
		negative+=1;
	
	i+=1
	if(i%10 == 0):
		print(i*100/200, "% completado");


print('Positive tweets:', positive);
print('Negative tweets:', negative);