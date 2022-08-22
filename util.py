import pickle
import json

__warming_type = None
__credit_eligible = None
__floor_location = None
__district = None
__data_columns = None
__model = None

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __warming_type
    global __credit_eligible
    global __floor_location
    global __district

    with open("static/categories.json", "r") as f:
        __data_columns = json.load(f)
        __warming_type = __data_columns['warming_type']
        __credit_eligible = __data_columns['credit_eligible']
        __floor_location = __data_columns['floor_location']
        __district = __data_columns['district']
        print(__data_columns)
    global __model
    if __model is None:
        with open('model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_district_names():
    return __district


def get_warming_type_names():
    return __warming_type


def get_credit_eligible_names():
    return __credit_eligible


def get_floor_location_names():
    return __floor_location


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()

