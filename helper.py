import pandas as pd

def column_exploder(df:pd.DataFrame, row_name:str):
    # row_name = ''
    row_values = set()

    for _, row in df.iterrows():
       row_values.update(set(row[row_name]))

    row_values = list(row_values)
    
    for item in row_values:
        df[item] = 0

    for i, row in df.iterrows():
        for item in row_values:
            df[item].iloc[i] = 0
            if item in row[row_name]:
                df[item].iloc[i] = 1
    return df
                
