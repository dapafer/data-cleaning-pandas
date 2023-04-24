# This function drops the rows with more than a given number of NaN.
def drop_null_rows(df, threshold):
    df.dropna(axis=0, inplace=True, thresh=threshold)
    df.reset_index(drop = True)
    return
