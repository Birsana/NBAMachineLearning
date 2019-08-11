
import csv
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

with open('NBA.csv') as f: #change based on which files you want to merge
    reader = csv.reader(f)
    dataList = list(reader)

#want to delete header rows, as well as rows with players that have no salaries (some did not have it reported)
#the first two "columns" in our data (the index and player name) are not needed so I'll remove them
for i in dataList[::-1]:
    del i[:2]
    if i[-1][0] != '$':
        dataList.remove(i)
    else: #remove dollar signs and commas from salaries so I can convert them to floats
        i[-1] = i[-1][1:]
        i[-1] = i[-1].replace(',', '')

for i in dataList: #change everything to float
        for j in i:
            j = float(j)

dataMatrix = np.array(dataList).astype(np.float)
#shuffle the data
np.random.shuffle(dataMatrix)

#print(np.size(dataMatrix,0)) #we have 1288 rows in our matrix

#I'll use 772 for the training set, and 258 for the training and cross validation set.
trainingSet = dataMatrix[0:772]
cvSet = dataMatrix[772: 1030]
testSet = dataMatrix[1030:1288]

X = trainingSet[:,:20]
y = trainingSet[:, [20]]
m = len(y)
xCV = cvSet[:,:20]
yCV = cvSet[:, [20]]
xTest = testSet[:,:20]
yTest = testSet[:, [20]]

'''I used the normal equation instead of gradient descent in my code, but just in case you want to try using
gradience descent, I've coded mean normalization and the code for gradient descent down below
means = []
ranges = []
def meanNorm(matrix, train):
    for i in range(1, np.size(matrix.T, 0)):
        vector = np.array(matrix.T[i, :])
        if train:
            mean = vector.mean()
            means.append(mean)
            maxMin = vector.max() - vector.min()
            if maxMin == 0:
                maxMin = 1
            ranges.append(maxMin)
        for j in range(np.size(matrix.T, 1)):
            if train:
                vector[j] = (vector[j] - mean) / maxMin
            else:
                vector[j] = (vector[j] - means[i - 1]) / ranges[i - 1]
        matrix[:, i] = vector
    return matrix

def gradientDescent(theta, X, y, lRate, iterations):
    for i in range(iterations):

        gradient = ((1 / m) * X.T @ (X @ theta - y))
        theta = theta - lRate * gradient
    return theta'''

#add a column of ones to our matrices
def addOnes(matrix):
    one = np.ones(np.size(matrix, 0))
    oneV = one[:, np.newaxis]
    matrix = np.append(oneV, matrix, axis = 1)
    return matrix

X = addOnes(X)
xCV = addOnes(xCV)
xTest = addOnes(xTest)

'''for i in range(1, 20):
    xAxis = X[:, i]
    plt.scatter(xAxis, y)
    plt.show()'''

def costFunction(theta,X,y):
    error = X@theta - y
    J = np.sum(np.power(error, 2)) / (2 * m)
    return J

#Normal Equation:
def normalEquation(X,y):
    X_transpose = np.transpose(X)
    X_transpose_dot_X = X_transpose.dot(X)
    temp_1 = np.linalg.pinv(X_transpose_dot_X)
    temp_2 = X_transpose.dot(y)
    thetaNorm = temp_1.dot(temp_2)
    return thetaNorm

costDegrees = []
costDegreesCV = []
def degreeChanger():
    optimalTheta = normalEquation(X,y)
    costDegrees.append(costFunction(optimalTheta, X, y))
    costDegreesCV.append(costFunction(optimalTheta, xCV, yCV))
    for i in range(2,4): #if we go to a higher degree, we will have far more features than data points, which will lead
        #to severe overfitting. Also, since I'm using the normal equation, it will have a very long runtime.
        poly = PolynomialFeatures(i)
        xNew = poly.fit_transform(X)
        xCVNew = poly.fit_transform(xCV)
        optimalTheta = normalEquation(xNew,y)

        costDegrees.append(costFunction(optimalTheta, xNew, y))
        costDegreesCV.append(costFunction(optimalTheta, xCVNew, yCV))


'''degreeChanger()
plt.plot(costDegrees, label = "train")
plt.plot(costDegreesCV, label = "CV")
plt.xlabel('degree')
plt.ylabel('cost')
plt.legend()
plt.show()'''

#As the graph shows, once we increase the degree we quickly start to overfit, so degree=1 is in fact the best for
#our model. For some reason, the CV cost is initially lower than the training cost, which I find very strange. This model
#would be a lot better with more data, as I only collected data from the past 5 years. Although pay standards for pro
#basketball players and inflation may skew older data, I still think you can go back way more than 5 years before this
#starts to become a problem


optimalTheta = normalEquation(X, y)
allPositive = abs((xTest@optimalTheta-yTest))
howWrong = allPositive.mean()

#print(howWrong) #on average, our guess is off by this much (seems to be a bit over 4 million)'''

#you can uncomment some print statements to see the testing done for yourself