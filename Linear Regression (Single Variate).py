'''
    It is a type of supervised learning
    Linear Regression shows a linear relationship between dependent & independent variables
    The idea is to find a best fit line by minimising the error (loss function)
'''

# import dependencies
import math
import numpy
import pandas
from matplotlib import pyplot as plot

if __name__ == "__main__":
    # read csv file & separate dependent & independent values
    df = pandas.read_csv("./datasets/LeastSquareDataSet.csv")
    X = df["x"]  # independent
    Y = df["y"]  # dependent
    print(df)

    # calculate mean values
    X_mean = numpy.mean(X)
    Y_mean = numpy.mean(Y)

    # calculate slope & intercept
    Sxx = Sxy = 0
    for i in range(len(df)):
        Sxx += math.pow((X[i] - X_mean), 2)
        Sxy += (X[i] - X_mean) * (Y[i] - Y_mean)

    m = Sxy/Sxx
    c = Y_mean - (m * X_mean)

    # find prediction line
    Y_prediction = m * X + c
    print(f"Predicted Line : Yi = {m} Xi + {c}")
    print("Predicted corresponding y values -")
    print(Y_prediction)

    # calculate error using RMSE
    RMSE = 0
    for i in range(len(df)):
        RMSE += math.pow((Y[i] - Y_prediction[i]), 2)
    RMSE = math.sqrt(RMSE/len(df))
    print(f"Error : {RMSE}")

    # plot actual & predicted values
    plot.scatter(X, Y)  # actual
    plot.scatter(X, Y_prediction, color="red")  # predicted
    plot.show()
