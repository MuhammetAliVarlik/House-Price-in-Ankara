#!/usr/bin/env python
# -*-coding:utf-8-*-
import pandas as pd
import math
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import pickle
import json

# from grid_search import GridSearch


pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)


class TrainModel:
    def __init__(self):
        pass

    @staticmethod
    def train_model():
        read_file = pd.read_excel('datas.xlsx')
        df = pd.DataFrame(read_file)
        df = df.drop(['Sütun1', 'id', ], axis='columns')
        df = df.set_axis(['price', 'number_of_rooms', 'net_m2', 'building_age', 'warming_type', 'credit_eligible',
                          'floor_location', 'number_of_bathrooms', 'district', 'population', 'education', 'illiterate'],
                         axis=1,
                         inplace=False)
        df_copy = df

        le_warming_type = LabelEncoder()
        le_credit_eligible = LabelEncoder()
        le_floor_location = LabelEncoder()
        le_district = LabelEncoder()

        warming_type = df['warming_type'].unique().tolist()
        credit_eligible = df['credit_eligible'].unique().tolist()
        floor_location = df['floor_location'].unique().tolist()
        district = df['district'].unique().tolist()
        categories = {
            "warming_type": warming_type,
            "credit_eligible": credit_eligible,
            "floor_location": floor_location,
            "district": district
        }
        with open('static/categories.json', 'w', encoding='utf8') as f:
            json.dump(categories, f)

        df['Warming_type'] = le_warming_type.fit_transform(df['warming_type'])
        df['Credit_eligible'] = le_credit_eligible.fit_transform(df['credit_eligible'])
        df['Floor_location'] = le_floor_location.fit_transform(df['floor_location'])
        df['District'] = le_district.fit_transform(df['district'])

        df = df.drop(
            ["warming_type", "credit_eligible", "floor_location", "district", "population", "education", "illiterate"],
            axis='columns')

        median_price = math.floor(df.price.median())
        df.price = df.price.fillna(median_price)

        median_number_of_rooms = math.floor(df.number_of_rooms.median())
        df.number_of_rooms = df.number_of_rooms.fillna(median_number_of_rooms)

        median_net_m2 = math.floor(df.net_m2.median())
        df.net_m2 = df.net_m2.fillna(median_net_m2)

        median_building_age = math.floor(df.building_age.median())
        df.building_age = df.building_age.fillna(median_building_age)

        median_number_of_bathrooms = math.floor(df.number_of_bathrooms.median())
        df.number_of_bathrooms = df.number_of_bathrooms.fillna(median_number_of_bathrooms)

        X = df.drop(['price'], axis='columns')
        Y = df.price

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=15)
        model = DecisionTreeRegressor(criterion='mse', splitter='best')
        model.fit(X_train, Y_train)
        score = model.score(X_test, Y_test)
        prediction = model.predict(X_test)
        print("Predictions:", prediction)
        print("Real:", Y_test.values.tolist())
        print("Score:", score)

        with open("features.pickle", "wb") as f:
            pickle.dump(df_copy, f)
        with open("model.pickle", "wb") as f:
            pickle.dump(model, f)


TrainModel().train_model()
