# Checking whther coloumn is available or not
def validate_schema(df,schema):
    for column in schema:
        if column not in df.columns:
            raise ValueError(f"Missing column : {column}")