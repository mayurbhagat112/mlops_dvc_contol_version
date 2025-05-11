import pandas as pd
import numpy as np
import os 

data={'name':['Alice','Bob','ajay'],
      'age':[24,54,34],
      'city':['mumbai','delhi','pune']
      }

df=pd.DataFrame(data)


data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")