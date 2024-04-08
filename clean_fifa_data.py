from tarfile import data_filter
import pandas as pd

# cleans fifa dataset 
def clean_fifa_data(data):
    data.drop_duplicates()
    data.dropna(axis = 0, how = 'all', inplace = True)
    data.drop(columns=['ID','NAME', 'JOINED', 'LOAN_DATE_END', 'CONTRACT'],inplace=True)

    data.rename(columns=str.upper, inplace=True)
    data.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)    

    data.dropna(subset=['POSITION'], inplace=True)
    data['POSITION'] = data['POSITION'].apply(lambda x: sort_positions(x))

    get_contract_terms(data)
    strip_height(data)
    strip_weight(data)
    strip_potential(data)
    convert_monetary_columns_to_m(data)
    
    return data

# helper function to sort positions in string 
def sort_positions(pos):
    pos = pos.split()
    pos.sort()
    return ' '.join(pos)

# helper function height to decimal
def strip_height(data):
    foot = data['HEIGHT'].str.split("'").str[0]
    inches = data['HEIGHT'].str.split("'").str[1].str.split('"').str[0]
    height = foot + '.' + inches
    data['HEIGHT'] = height
    data['HEIGHT'] = pd.to_numeric(data['HEIGHT'], errors='coerce')
    return data

# helper function to split TEAM&CONTRACT 
def get_contract_terms(data):
    years_ended = r'(\d{4}) ~ (\d{4})'
    years_continued = r'(\d{4})(?!\d|,|$)'
    date_info_e = data['TEAM_&_CONTRACT'].str.extract(years_ended)
    date_info_c = data['TEAM_&_CONTRACT'].str.extract(years_continued)
    date_info = date_info_e.combine_first(date_info_c)
    ## if secont place empty, then on loan -- continues
    date_info[1].fillna(9999, inplace=True)
    # create new column, assign values
    data['CONTRACT_START'] = date_info[0]
    data['CONTRACT_END'] = date_info[1]
    data.drop(columns=['TEAM_&_CONTRACT'],inplace=True)
    return data

# helper function to remove weight 
def strip_weight(data):
    data['WEIGHT'] = data['WEIGHT'].str.replace('lbs', '').astype(int)
    return data

# helper function strip potential from positions
def strip_potential(data):
    columns = ['LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB','GK']
    for column in columns:
        data[column] = data[column].str.split("+").str[0]
        data[column] = pd.to_numeric(data[column], errors='coerce')
    return data

# convert value to millions
def convert_monetary_columns_to_m(data):
    columns = ['VALUE', 'WAGE', 'RELEASE_CLAUSE']
    for column in columns:
        data[column] = data[column].str.replace('€', '').str.replace('M', '').str.replace('K', ' / 1000').map(pd.eval).astype(float)
    return data