import pandas as pd
from snownlp import SnowNLP  # pip install snownlp

if __name__ == '__main__':
    df = pd.read_csv("output.csv")
    ls_senti = []
    for row in df.itertuples():
        if isinstance(row[3], str):
            s = SnowNLP(row[3])
            ls_senti.append(s.sentiments)
            print(s.sentiments)
        else:
            ls_senti.append(9)
            print("Error")
    df['sentiment_snow'] = ls_senti
    df.to_csv("output.csv", index=False, encoding='utf_8_sig')

