from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

df=pd.read_csv('bekasi_weather_forecast.csv')

#Dropping the target variable and make it is as newframe
df.drop(['timepoint', 'cloudcover', 'lifted_index', 'prec_type'],axis='columns')

target=df['weather']

#Encoding the strings to Numericals
Numerics=LabelEncoder()

#Creating the new dataframe
df['cuaca']=Numerics.fit_transform(target)
df['arah_angin']=Numerics.fit_transform(df['wind10m.direction'])

df.drop(['timepoint', 'cloudcover', 'lifted_index', 'prec_type'], axis='columns', inplace=True)

#Store labels and name for final use
weather_dict = dict(zip(df['cuaca'], target))
arahangin_dict = dict(zip(df['arah_angin'], df['wind10m.direction']))

df_final = df.drop(['weather', 'wind10m.direction'],axis='columns')

df_final.rename(columns=({'prec_amount': 'prestipasi', 'temp2m': 'suhu', 'rh2m': 'kelembapan',
                          'wind10m.speed': 'kecepatan_angin'}), inplace=True)

#Preprocess Data for Machine Learning Development
X = df_final.drop(['cuaca'], axis = 1)
y = df_final['cuaca']

X['kelembapan'] = X['kelembapan'].str.split('%', expand=True)[0]

over_strategy = {0 : 1000, 1 : 1000, 2 : 1000}
under_strategy = {0 : 1000, 1 : 1000, 2 : 1000}

oversample = SMOTE(random_state=0, sampling_strategy=over_strategy, k_neighbors=1)
undersample = RandomUnderSampler(sampling_strategy = under_strategy)

X_final,y = oversample.fit_resample(X,y)
X_final,y = undersample.fit_resample(X_final, y)

X_train,X_test,y_train,y_test = train_test_split(X_final,y,random_state = 10, test_size = 0.2)

model = GaussianNB()

model.fit(X_train,y_train)
pred_all = model.predict(X_final)
pred_train = model.predict(X_train)
pred_test = model.predict(X_test)

#print(f'Accuracy Score on All Data : {round(accuracy_score(y, pred_all),2)*100}')
#print(f'Accuracy Score on Train Data : {round(accuracy_score(y_train, pred_train),2)*100}')
#print(f'Accuracy Score on Test Data : {round(accuracy_score(y_test, pred_test),2)*100}')
#model.predict([[2, 30, '80', 3, 6]])
