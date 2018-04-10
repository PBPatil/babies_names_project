# %load q01_create_dict/build.py
import pandas as pd

path = 'data/babies_name.csv'
data = pd.read_csv(path,names=['Name', 'Gender', 'Count', 'Year'])

def q01_create_dict(data):
    count = data.Name.value_counts()
    names = count.index
    name_count = count.values
    keys = list(names)
    vals = list(name_count)
    return dict(zip(keys,vals))
    

        
    
   
    'write your solution here'











