
import pandas as pd 

data = pd.DataFrame({'ID': ['asd123', 'asd123', 'dsa321','dsa321'],
                     'problem': [1,2,1,2],
                     'status': [False,False,True,False]})


data.to_csv('checksWeb/testdata.csv', index=False)