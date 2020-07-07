from pyprojroot import here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()

data = pd.read_csv(here('./data/raw/train.csv'))
print(data.shape)
data.head(3)

# checking for null values
data.isnull().sum()

# def split_joke_identifier(df):
#     for index, row in df.iterrows():
#         r = row['Joke_identifier'].split()
#         df['Comedian'] = " ".join(r[:-2])
#         df['State'] = r[-2]
#         df['part'] = r[-1]
#     return df


data['Comedian'] = data.Joke_identifier.apply(lambda x : ' '.join(x.split()[:-2]))
data['State'] = data.Joke_identifier.apply(lambda x : x.split()[-2])
data['Part'] = data.Joke_identifier.apply(lambda x : x.split()[-1])
data.head(3)

data.drop(['Joke_identifier', 'Response_ID'], axis=1, inplace=True)
data.head(3)


data_input = data.drop(['Rating','Viewers_ID'], axis=1)
data_label = data['Rating']


data_input.head()


# Encode all categorical feature with label encoding
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
for col in ['Comedian','State']:
    data_input[col] = lb.fit_transform(data[col])
data_input.head()


data_input.to_csv(here('./data/processed/data_input.csv'), index=False)
data_label.to_csv(here('./data/processed/data_label.csv'), index=False)


