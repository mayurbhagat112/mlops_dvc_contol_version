import pandas as pd
import numpy as np
import os 

data={'name':['Alice','Bob','ajay'],
      'age':[24,54,34],
      'city':['mumbai','delhi','pune']
      }

df=pd.DataFrame(data)

#adding new row to df for version2

new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc


# # Adding new row to df for V3
new_row_loc2 = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}
df.loc[len(df.index)] = new_row_loc2

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")