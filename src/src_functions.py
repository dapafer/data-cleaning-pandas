# This function drops the rows with more than a given number of NaN.
def drop_null_rows(df, threshold):
    
    return df.dropna(thresh=df.shape[1]-threshold+1)