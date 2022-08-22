import pandas as pd
import pickle
import numpy as np


pd.options.display.width = None
pd.options.display.max_columns = None
pd.set_option('display.max_rows', 3000)
pd.set_option('display.max_columns', 3000)


class Prediction:
    def __init__(self):
        with open("model.pickle", "rb") as f:
            self.model = pickle.load(f)
        with open("features.pickle", "rb") as f:
            self.features = pickle.load(f)

    def predict(self, rooms, m2, age, bathrooms, warming, credit, floor, district):
        warming = np.where(self.features.warming_type == warming)[0][0]
        credit = np.where(self.features.credit_eligible == credit)[0][0]
        district = np.where(self.features.district == district)[0][0]
        floor = np.where(self.features.floor_location == floor)[0][0]

        data = {
            'number_of_rooms': [rooms],
            'net_m2': [m2],
            'building_age': [age],
            'number_of_bathrooms': [bathrooms],
            'Warming_type': [warming],
            'Credit_eligible': [credit],
            'Floor_location': [floor],
            'District': [district],
        }
        df1 = pd.DataFrame(data)
        prediction = self.model.predict(df1)
        return prediction[0]



#4, 150, 15, 1, "Kombi", "Uygun", "Kot 1","Keçiören"
