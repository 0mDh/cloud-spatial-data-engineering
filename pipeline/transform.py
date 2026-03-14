def clean_data(df):
    # NULL VALUE removal #
    df = df.dropna()  
    return df