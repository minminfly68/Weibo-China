#pip install jieba
from jieba.analyse import *
import pandas as pd
import operator

def topic_extraction():
	df = pd.read_csv("2656274875-2.csv")
	ls_key = []
	for row in df.iterrows():
		s = row[1][2]
		#for keyword, weight in extract_tags(s, withWeight=True, topK=1):
		for keyword, weight in textrank(s, withWeight=True, topK=1): # If you would like to switch to textrank
			temp_key = keyword
		if not temp_key.isdigit():
			ls_key.append(temp_key)
	
	dict_key = dict((x,ls_key.count(x)) for x in set(ls_key))
	dict_key = dict(sorted(dict_key.items(), key=operator.itemgetter(1),reverse=True))

	df_output = pd.DataFrame(list(dict_key.items()), columns=['topic', 'frequency'])
	df_output.to_csv("2_output_rank.csv", index=False, encoding='utf_8_sig')
	return 

if __name__ == "__main__":
	topic_extraction()