import numpy as np
import matplotlib.pyplot as plt

type= "dude what"
A = np.array([1,2,3,2])

result1 = []
result2 = []
result3 = []
def indiff(A,type):

    if(type == "fw"):
        i=0
        lenght = len(A)
        for line in A :
            if(i != lenght-1):
                temp1 = A[i]
                temp2 = A[i+1]
                temp3 = temp2 - temp1
                result1.append(temp3)
            i=i+1
        result1.append("NaN")
        print(result1)

    if(type == "bw"):
        result2.append("NaN")
        i=0
        lenght = len(A)
        for line in A :
            if(i != lenght-1):
                temp1 = A[i]
                temp2 = A[i+1]
                temp3 = temp2 - temp1
                result2.append(temp3)
            i=i+1
        print(result2)



    if(type == "cd"):
        result3.append("NaN")
        lenght = len(A)

        for i in range(1,lenght) :
            if(i<lenght-1):
                temp1 = A[i-1]
                temp2 = A[i+1]
                temp3 = temp2 - temp1
                result3.append(temp3)
            i=i+1
        result3.append("NaN")
        print(result3)








indiff(A,type="cd")
indiff(A,type="fw")
indiff(A,type="bw")
