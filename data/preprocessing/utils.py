import pandas as pd

PLANETS_LIST = ['neptune', 'pluto']
HOUSES_LIST = ['AC', '2', '3', 'IC', '5', '6', 'DC', '8', '9', 'MC', '11', '12']

def convert_to_int(df, series_id):
    if df[series_id].dtype == int:
        print("The series is already of integer type.")
    else:
        df[series_id] = df[series_id].astype(int)
        
# define the preprocessing pipeline
def preprocess_data(df):
    # drop rows with NaN in birth_time column
    df.dropna(subset=['birth_time'], inplace=True)
    df.dropna(subset=['neptune_house'], inplace=True)
    
    # convert selected columns from string to int
    int_cols = ['age', 'height']
    df[int_cols] = df[int_cols].astype(int)
    
    for planet in PLANETS_LIST:
        convert_to_int(df, f"{planet}_house")
        convert_to_int(df, f"{planet}_pos_degrees")
        convert_to_int(df, f"{planet}_pos_minutes")
        
    for house in HOUSES_LIST:
        convert_to_int(df, f"house_{house}_pos_degrees")
        convert_to_int(df, f"house_{house}_pos_minutes")

    return df