import pandas as pd
import os
from patsy import dmatrix
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import statsmodels.formula.api as smf

'''
#%%
df=pd.read_csv('data/Overall.csv',index_col=0,header=0)
df=df[df.notnull().all(axis=1)]
y_total=df.loc[:,'Income inequality index':'Learning_or_earning equality index']
x=df.loc[:,'Index of Relative Socio-economic DisadvantageScore':].iloc[:,list(range(0,9,2))]
print(x)
y=y_total.iloc[:,[0]]
scaler = StandardScaler()
y=scaler.fit_transform(y)
scaler = StandardScaler()
x=scaler.fit_transform(x)
poly = PolynomialFeatures(degree = 2)
x_poly = poly.fit_transform(x)
model=sm.OLS(y,x_poly).fit()
print(model.summary())
plt.plot(y_total.index,y,label='actual',color='blue')
plt.plot(y_total.index,model.predict(x_poly),label='pred',color='orange')
plt.legend()
plt.savefig("data/regression.png")
'''

df=pd.read_csv('data/inequality_socioeco.csv',index_col=0,header=0)
df=df[df.notnull().all(axis=1)]
y_total=df.iloc[:,1:7]
x=df.iloc[:,7:].iloc[:,list(range(0,9,2))]

# generate a scatter plot including all inequality index for each socio-eco index, save as subplot to the figure
# write regression summary to textfile

fig, axes = plt.subplots(2, 3, figsize=(9, 6))
fig.suptitle("Regression Models")

with open("data/regression_result.txt", 'w') as fp:
    for i in range(0, len(y_total.columns)):
        if i < 3:
            x_ax = 0
        else:
            x_ax = 1
        y_ax = (i + 3) % 3

        y=y_total.iloc[:,[i]]

        scaler = StandardScaler()
        y=scaler.fit_transform(y)
        scaler = StandardScaler()
        x=scaler.fit_transform(x)
        poly = PolynomialFeatures(degree = 2)
        x_poly = poly.fit_transform(x)
        model=sm.OLS(y,x_poly).fit()

        fp.write('\n------------------------'+y_total.columns[i]+'--------------------------\n')
        fp.write(model.summary().as_text())
        fp.write('\n')
        axes[x_ax,y_ax].plot(y,label='actual',color='blue')
        axes[x_ax,y_ax].plot(model.predict(x_poly),label='pred',color='orange')
        axes[x_ax,y_ax].legend()
        axes[x_ax,y_ax].set_title(y_total.columns[i], size=7)

    fig.tight_layout()
    plt.savefig("data/regression.png")
    plt.close()