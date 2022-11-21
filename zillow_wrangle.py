from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import seaborn as sns
from grab_db import my_db
import os
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


#Acquire zillow
def get_zillow_data():
    filename = 'dafinalzillow.csv'
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = my_db('''select taxvaluedollarcnt, fips, yearbuilt, bedroomcnt,bathroomcnt,calculatedfinishedsquarefeet, garagecarcnt, lotsizesquarefeet, poolcnt,regionidzip,roomcnt,numberofstories from properties_2017
join propertylandusetype using (propertylandusetypeid)
join predictions_2017 using (parcelid)
where propertylandusetypeid = 261 and transactiondate = 2017;''','zillow')
        df.to_csv(filename)
        return df
#this function will clean the zillow data.
def clean_zillow(df):
    df['poolcnt'] = df.poolcnt.fillna(0)
    df['garagecarcnt'] = df.garagecarcnt.fillna(0)
    df['numberofstories'] = df['numberofstories'].fillna(round(df.calculatedfinishedsquarefeet/(df.calculatedfinishedsquarefeet[df.numberofstories == 1.0].mean())))
# removes all null rows. If rows are all null they can all be deleted.
    df = df[df.isnull().sum(axis = 1) < len(df.columns)]
    #-assign fips to 1 - 3. Reassign year built to age.
    df['location'] = df.fips.map({6037.0: 0,6059.0:1,6111.0:2})
    df['age'] = 2022 - df.yearbuilt
    #dummies
    df['orange_county'] = 0
    df['ventura'] = 0
    df['losangeles'] = 0
    df.orange_county[df.location == 1] = 1
    df.ventura[df.location == 2] = 1
    df.losangeles[df.location == 0] = 1
    #NULLS
    df = df[df['taxvaluedollarcnt'].isnull() == False]
    df = df[df['lotsizesquarefeet'].isnull() == False]
    df = df[df['age'].isnull() == False]
    df = df[df['numberofstories'].isnull() == False]
    df = df[df['regionidzip'].isnull() == False]
#if there no year built than we will set it to 0
    df.yearbuilt[df.bathroomcnt == 0.0] = df.yearbuilt[df.bathroomcnt == 0].fillna(0)
# nulls inside of bedroom count and bathroom count where yearbuilt was also null can be safely changed to 0's as you cant have a bed/bathroom if you dont have a building.
    df.calculatedfinishedsquarefeet[df.yearbuilt == 0.0] = df.calculatedfinishedsquarefeet[df.yearbuilt == 0.0].replace(np.nan,0)
#drop taxamount as it has lots of nulls and is highly correlated with taxvaluedollarcnt
#drop all remaining nulls as their meaning cant be identified
    #df = df.dropna()
#getting rid of rows with 0's for 3 or more columns as they are useless.
    #df = df[(df == 0).sum(axis=1) < 3]
#getting rid of crazy sqft outlier.
    df = df[df.calculatedfinishedsquarefeet < 500000]
    
#r
#reset index so it is chronological and not missing numbrrs
    df = df.reset_index()
    df = scale_zillow(df)
#drop extra columns.
    df = df.drop(columns = ['Unnamed: 0','fips','index','yearbuilt','location','regionidzip','lotsizesquarefeet','roomcnt','garagecarcnt','numberofstories'])

    return df
def scale_zillow(df):
    Scaler = MinMaxScaler()
    df[['bedroomcnt','bathroomcnt','calculatedfinishedsquarefeet','garagecarcnt','lotsizesquarefeet','poolcnt','regionidzip','roomcnt','numberofstories','location','age']] = Scaler.fit_transform(df[['bedroomcnt','bathroomcnt','calculatedfinishedsquarefeet','garagecarcnt','lotsizesquarefeet','poolcnt','regionidzip','roomcnt','numberofstories','location','age']])
    return df


def my_train_test_split(df):

    train, test = train_test_split(df, test_size=.2, random_state=123)
    train, validate = train_test_split(train, test_size=.25, random_state=123)

    return train, validate, test

def plot_variable_pairs(df):
    return sns.pairplot(df, kind = 'reg', plot_kws={'line_kws':{'color':'red'}})

def plot_categorical_and_continuous_vars(df,cat,num):
    return sns.boxplot(x = cat,y = num, data = df),plt.ylim(0,5000),plt.show() , sns.barplot(x = cat, y = num, data =df),plt.ylim(0,5000),plt.show(), sns.violinplot(x = cat, y= num, data = df),plt.ylim(0,5000),plt.show()
#%%

#%%
