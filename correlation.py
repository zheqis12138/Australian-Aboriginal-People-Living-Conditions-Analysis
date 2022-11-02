from numpy.random import randn
from numpy.random import seed
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
from scipy.stats import spearmanr
from scipy.stats import pearsonr
import csv
import pandas as pd

# read data
socio_name = "data/integrate_abs_data.csv"
equality_name = "data/inequality_socioeco.csv"
socio_data = pd.DataFrame(pd.read_csv(socio_name))
equality_data = pd.read_csv(equality_name)


# pearson and spearman's correlation values

pearson_value = []
spearman_value = []

for i in range(1,9):
    x = socio_data.iloc[:,i]
    pearson_row = []
    spearman_row = []
    for j in range(2,8):
        y = equality_data.iloc[:,j]
        corr, _ = pearsonr(x, y)
        spearcorr, _ = spearmanr(x, y)
        pearson_row.append(round(corr,2))
        spearman_row.append(round(spearcorr,2))
        
    pearson_value.append(pearson_row)
    spearman_value.append(spearman_row)
    
pearson_data = pd.DataFrame(pearson_value)
pearson_data.index = socio_data.columns[1:9]
pearson_data.columns = equality_data.columns[2:8]
pearson_data.to_csv("data/pearson_correlations.csv")

spearman_data = pd.DataFrame(spearman_value)
spearman_data.index = socio_data.columns[1:9]
spearman_data.columns = equality_data.columns[2:8]
spearman_data.to_csv("data/spearman_correlations.csv")

    
