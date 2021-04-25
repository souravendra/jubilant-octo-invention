import numpy as np
import pandas as pd
import math
import os


def resultant(x, y, z):  # function to calculate resultant
    s = x * x + y * y + z * z
    return np.sqrt(s)


def calcmax(xVal, yVal, zVal):  # function to calculate max value from a set of resultants
    maxValue = -math.inf
    for i in range(len(xVal)):
        acc = resultant(xVal[i], yVal[i], zVal[i])
        maxValue = max(acc, maxValue)

    return maxValue  # returns the max value from current CSV


# column names
column_names = ["Xvalue", "Yvalue", "Zvalue"]

files = [file for file in os.listdir('./csvdata')]  # list of files in folder

output = []  # contains max values of each csv, should have the same number of entries as the total number of csv files

for file in files:
    df = pd.read_csv(file, sep=';', engine='python',
                     names=column_names)  # sep='' contains the separator, usually ' ', ',', '_', etc

    # creating empty lists
    xVal = []
    yVal = []
    zVal = []

    # reading input from csv
    xVal = df.Xvalue.to_list()
    yVal = df.Yvalue.to_list()
    zVal = df.Zvalue.to_list()

    if len(xVal) != len(yVal) or len(yVal) != len(zVal) or len(zVal) != len(xVal):
        print("incorrect data format, length of columns don't match")

    else:
        output.append(str(calcmax(xVal, yVal, zVal)))

dict = {'File': files, 'Max Value': output}

op = pd.DataFrame(dict)
op.to_csv('maxvalue.csv')  # saving the output list to a single csv file
