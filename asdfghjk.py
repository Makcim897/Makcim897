import pandas as pd
article = pd.read_csv('Data1.csv', delimiter=',',names=['user_id', 'user_name', 'user_age'])
print(article)


article.iloc[1, 1] = "hi"
article.to_csv("data.csv", index=False, sep=";")
print(article)