from random import randint
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a+b+c
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)

from sklearn.linear_model import LinearRegression

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

ip=[]
for i in range(3):
    ip.append(int(input('Enter integer '+str(i+1)+' : ')))

X_TEST = [ip]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_

print('Outcome : {}\nCoefficients : {}'.format(outcome, coefficients))
