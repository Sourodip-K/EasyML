import pandas as pd
def read(path):
    df = pd.read_excel(path)
    return df