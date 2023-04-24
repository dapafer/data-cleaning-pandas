# This function drops the rows with more than a given number of NaN.
def drop_null_rows(df, threshold):
    df.dropna(axis=0, inplace=True, thresh=threshold)
    df.reset_index(drop = True)
    return

# This function replace the activities by the main one.
def replace_activities(Activity):
    if 'swimming' in Activity.lower():
        return 'swimming'
    elif 'surfing' in Activity.lower():
        return 'surfing'
    else:
        return Activity