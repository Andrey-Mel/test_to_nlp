import pandas as pd
import numpy as np
import re




df = pd.read_csv('/content/drive/MyDrive/test_data_nlp/test_data.csv', delimiter=',')


# регулярные выражения
# шаблон (слова/сочетания словб которые необходимо найти в столбцах)
r = re.compile(r'(добрый день)|(здравствуйте)|(до свидания)|(меня зовут.*?)|(мое имя.?)', re.UNICODE)
dfm = df[(df.role == 'manager') & (df.text)]


#Для каждой строки ищем шаблон в столбце "role"
otvet = dfm['text'].str.lower().str.contains(r)

dfm = dfm[otvet]
df['greeting'] = ''
for i in dfm.index:
    df.iloc[i,[4]] = df.iloc[i,[3]].str.lower().str.contains(r)


fr = r"диджитал бизнес"

dfa = df[(df.role == 'client') & (df['text'])]
company = dfa['text'].str.lower().str.contains('диджитал бизнес')
dfa = dfa[company]
df['company'] = ''
for i in dfa.index:
    df.iloc[i, [5]] = df.iloc[i,[3]].str.lower().str.findall(fr)[0]


lst_diag = []
lst_diag = df['dlg_id'].unique()


greeting = re.compile('(здравствуйте)|(добрый день)|(до свидания)')

man_text = []
for j in range(len(lst_diag)):

    dfm1 = df[(df.dlg_id == lst_diag[j]) & (df.role == 'manager') & (df.text)]

    texts = list(dfm1.text.values)
    # man_text.append(list(text))
    for text in texts:
        if greeting.findall(text.lower()):
            s = greeting.findall(text.lower())

            if 'до свидания' in s[0]:
                print(f'manager_{j} по прощался')

            if ('добрый день','до свидания') in s[0]:
                print(f'manager_{j} полное приветствие')

            elif ('здравствуйте','до свидания') in s[0]:
                print(f'manager_{j} полное приветсвие')

df.to_csv('test.csv', index=False)
