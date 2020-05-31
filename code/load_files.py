import pandas as pd 

happy_emojis = ['😊', '😁', '😂', '🤣', '😀', '😆', '🙂', '😄'];
sad_emojis = ['😪', '😓', '😢', '😭', '😔', '😞', '☹️'];
angry_emojis = ['😡', '😠', '😤'];
hope_emojis = ['🙏', '🙌', '🙋', '😷'];

not_happy = sad_emojis + angry_emojis + hope_emojis
not_sad = happy_emojis + angry_emojis + hope_emojis
not_angry = sad_emojis + happy_emojis + hope_emojis
not_hope = sad_emojis + angry_emojis + happy_emojis

def textClass(text):
	# print(text);
	if(any(word in text for word in happy_emojis)):
		if(not any(word in text for word in not_happy)):
			return "happy";
		else:
			return "no class";

	if(any(word in text for word in sad_emojis)):
		if(not any(word in text for word in not_sad)):
			return "sad";
		else:
			return "no class";

	if(any(word in text for word in angry_emojis)):
		if(not any(word in text for word in not_angry)):
			return "angry";
		else:
			return "no class";
	
	if(any(word in text for word in hope_emojis)):
		if(not any(word in text for word in not_hope)):
			return "hope";
		else:
			return "no class";

	return "no class";

all_files = [ 
	"coronavirus-tweets/2020-04-16 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-17 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-18 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-19 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-20 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-21 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-22 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-23 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-24 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-25 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-26 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-27 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-28 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-29 Coronavirus Tweets.CSV",
	"coronavirus-tweets/2020-04-30 Coronavirus Tweets.CSV" ]

print('Reading files...');

data = pd.concat((pd.read_csv(f, usecols=["text", "lang"]) for f in all_files))

print('Filtering by language...');

data = data.loc[data['lang'] == "en"]

print('Setting class...');

data["text"] = data["text"].astype("string")
data["class"] = data.apply(lambda x: textClass(x['text']), axis=1)

print('Dividing in train and test...');

train = data.loc[data['class'] != "no class"]
test = data.loc[data['class'] == "no class"]

# print(data.head(10))

print('Saving to csv...');

train.to_csv('train.csv');
test.to_csv('test.csv');

print('Done!');

# Preview the first 5 lines of the loaded data 
# print(data.head(15))

# for i in range(5): 
#     print(data.rows[i]['text']) 