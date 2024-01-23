import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))    

    x[0] = sqft
    x[1] = bhk
    x[2] = bath

    if loc_index >= 0 :
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)

def get_location_names():
    
    return __locations

def load_artifact_names():
    global __data_columns
    global __locations
    global __model

    with open(r"server\artifacts\real_estate_columns.json","r") as f:
        __data_columns = json.load(f)['data columns']
        __locations = __data_columns[3:]

    global __model
    with open(r"server\artifacts\RealEstateProject_model.pickle","rb") as f:
        __model = pickle.load(f)
    print("loaded all the artifacts..")

""" if __name__ == "__main__":
    load_artifact_names()
    print(__locations)
    print(get_estimated_price("1st Phase JP Nagar",1000,2,2))
    print(get_estimated_price("1st Phase JP Nagar",1000,3,3))
    print(get_estimated_price("Jalahalli",1000,2,2))
    print(get_estimated_price("Dasanapura",1000,2,2))  """
