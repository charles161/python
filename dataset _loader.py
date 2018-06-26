import pandas as pd
import numpy as np

raw_data = {'month': [1, 5, 9, 11, 12], 
        'houses_sold': [200, 400, 400, 300, 200]
        }

df = pd.DataFrame(raw_data, columns = ['month', 'houses_sold'])
df.to_csv('houses_sold.csv')
