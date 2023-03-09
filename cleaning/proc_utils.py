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
    df.dropna(subset=['sun_sign'], inplace=True)
    df.dropna(subset=['birth_time'], inplace=True)
    df.dropna(subset=['neptune_house'], inplace=True)

    for planet in PLANETS_LIST:
        convert_to_int(df, f"{planet}_house")
        convert_to_int(df, f"{planet}_pos_degrees")
        convert_to_int(df, f"{planet}_pos_minutes")

    for house in HOUSES_LIST:
        convert_to_int(df, f"house_{house}_pos_degrees")
        convert_to_int(df, f"house_{house}_pos_minutes")

    return df

def fillna_all(df, numeric_value=0, string_value=''):
    for col in df.columns:
        if df[col].dtype == 'int64' or df[col].dtype == 'float64':
            df[col].fillna(numeric_value, inplace=True)
        elif df[col].dtype == 'object':
            df[col].fillna(string_value, inplace=True)
    return df

def clean_df(df):
    column_type_dict = {
        'degrees': int,
        'minutes': float,
        'retrogrades': int,
        '_house': int,
        # 'birth_time': str,
        'birth_day': int,
        'birth_month': int,
        'birth_year':int,
        'death_year': int,
        'occupation': str,
        'death_cause': str,
        'sign': str,
        'name': str
    }
    for col in df.columns:
        if col is not None and col.lower() is not None:
            for key, value in column_type_dict.items():
                if key in col.lower():
                    df[col] = df[col].astype(value)

    # Loop over all columns that end with '_retrograde' --- these had to be forced int separately
    for col in df.columns:
        if col.endswith('_retrograde'):
            # Replace '1' values with 1 and empty cells with 0
            df[col] = df[col].apply(lambda x: 1 if str(x) == '1' else 0)
            # Convert the column to int
            df[col] = df[col].astype(int)
    return df
