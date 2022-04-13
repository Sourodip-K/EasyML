import pickle
import pandas as pd
def read(path):
    with open(path, 'rb') as file:
        data = pickle.load(file)
    df = pd.DataFrame(data)
    return df