import pandas as pd

# cleans fifa dataset 
def clean_fifa_data(data):
    # basic cleaning 
    data.drop_duplicates()
    data.dropna(axis = 0, how = 'all', inplace = True)
    data.rename(columns=str.upper, inplace=True)
    data.rename(columns=lambda x: x.strip().replace(" ", "_"), inplace=True)

    data['BP_INFO'] = data.apply(lambda row: row[row['BP']], axis=1)
    strip_potential(data)
    #with_potential(data)
    
    data.reset_index(drop=True, inplace=True)
    
    return data[['REACTIONS','BASE_STATS', 'BP_INFO','OVA']]

# helper function strip potential from positions
def strip_potential(data):
    data['BP_INFO'] = data['BP_INFO'].str.split("+").str[0]
    data['BP_INFO'] = pd.to_numeric(data['BP_INFO'], errors='coerce')
    return data

# helper function to add potential
# tested it, same model, same metrics 
def with_potential(data):
    data['BP_INFO'] = data['BP_INFO'].str.replace('[^\d+-]', '', regex=True)
    data['BP_INFO'] = pd.to_numeric(data['BP_INFO'], errors='coerce')
    return data
