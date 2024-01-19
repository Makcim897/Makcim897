import pandas as pd
while True:
    article = pd.read_csv('data1.csv', delimiter=';')
    names = ['user_id', 'user_height', 'user_age']
    article.to_csv("data1.csv", index=False, sep=";")
    col = str(input(''))
    num = int(input(''))
    def read_slot():
        print(article.at[num, col])
    read_slot()