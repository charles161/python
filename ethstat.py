import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = 'eth.csv'
eth_dataset = pd.read_csv(input_path)

def get_headers(dataframe):
    
    return dataframe.columns.values

eth_headers=get_headers(eth_dataset)

print(eth_headers)

INPUT=[]
for ip in eth_dataset['date']:
    s=ip.replace('-','')
    INPUT.append([int(s)])

OUTPUT=eth_dataset['price(USD)']

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=INPUT, y=OUTPUT)

x=int(input('Enter the date in YYYYMMDD : '))

outcome = predictor.predict(X=[[x]])

print(outcome)
