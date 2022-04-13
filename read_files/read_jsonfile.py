import pandas as pd
def read(path):
    df = pd.read_json(path)
    return df