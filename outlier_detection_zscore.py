import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_excel('Prime.xlsx') #here i use pandas to read xlsx file
Expenditures = data["Expenditures"] #extracting Expenditures variable


plt.boxplot(Expenditures)#creating plot
plt.show()#Showing plot

mean = np.mean(Expenditures)#mean of Expenditures
std = np.std(Expenditures)#standard-deviation of Expenditures


#A standard cut-off value for finding outliers are, Z-scores < +3 or Z-scores > -3.
#Z-scores beyond +/- 3 are so extreme and we can say the corresponding values of those z-scores are outliers.

#equation of Z score = (x -mean)/standard-deviation
#where x is the corresponding value

threshold = 3 #limit for outlier
outlier = [] #for storing outliers
z_score=[] #for storing z-scores


#calculating Z-Scores for all values of Expenditures
for i in Expenditures:
    z = (i-mean)/std #Z-score formula
    z_score.append(z) #storing z-scores
    #checking outlier or not and storing in list
    if z > threshold or z < (-threshold):
        outlier.append(i)


#printing minimum and maximum Z-Score and outliers
print('Min_Z-Score = ', min(z_score),', Max_Z-score = ', max(z_score))
print('outlier in dataset is', outlier)


