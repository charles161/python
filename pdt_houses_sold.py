import pandas as pd
from sklearn.linear_model import LinearRegression

input_path = 'houses_sold.csv'
hs_dataset = pd.read_csv(input_path)

def get_headers(dataframe):
    
    return dataframe.columns.values

hs_headers=get_headers(hs_dataset)

INPUT=[]
for ip in hs_dataset[hs_headers[1]]:
    INPUT.append([ip])
    
OUTPUT=hs_dataset[hs_headers[2]]

#training the model
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=INPUT, y=OUTPUT)

x=int(input('Enter the month in number : '))

outcome = predictor.predict(X=[[x]])

print(outcome)

