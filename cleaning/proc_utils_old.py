
def clean_df(df):
    # create a function to update the data type based on column name
    def update_type(col_name):
        if 'degrees' in col_name:
            return int
        elif 'minutes' in col_name:
            return float
        elif 'sign' in col_name:
            return str
        elif 'retrogrades' in col_name:
            return int
        elif 'house' in col_name:
            return int
        elif col_name == 'occupation':
            return str
        elif col_name == 'birth_time':
            return pd.to_datetime
        elif 'birth' in col_name:
            return int
        elif col_name == 'death_cause':
            return str
        elif 'death' in col_name:
            return int
        elif col_name == 'name':
            return str
        else:
            return None

    # apply the function to each column and update the data type
    for col in df.columns:
        new_type = update_type(col)
        if new_type is not None:
            if new_type == pd.to_datetime:
                df[col] = pd.to_datetime(df[col], format=' %H:%M')
                df[col] = df[col].dt.time
            else:
                df[col] = df[col].astype(new_type)

    return df
