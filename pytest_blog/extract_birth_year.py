import datetime

def get_birth_year(df):
    year = datetime.date.today().year
    # if boolean value is present in age column it gives out worng birth_year
    # as boolean values are considered as 0 and 1 for False True respectively. 
    # in that case it will be replaceed by current year so the birth year will be zero
    replace_boolean_values = [True,False]
    if 'Age' in df.columns:
        df['Age'] = df['Age'].replace(replace_boolean_values,0)
        df['birth_year'] = year - df['Age']
    else:
        raise NotImplementedError('unsupported dataframe')
    return df