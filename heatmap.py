import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Spearman
spearman_correlations = pd.read_csv("data/spearman_correlations.csv")
spearman_correlations.set_index("Unnamed: 0", inplace=True)

fig = plt.figure(figsize=(6,6))
plt.title("Spearman's Correlation Values")
hm = sns.heatmap(spearman_correlations, annot = True, annot_kws={"size": 7}, xticklabels = True, yticklabels = True)
hm.set_xticklabels(hm.get_xticklabels(), rotation=90, size = 7) 
hm.set_yticklabels(hm.get_yticklabels(), rotation=65, size = 7)

plt.xlabel("(in)equality index")
plt.ylabel("socio-economic status index")
plt.tight_layout()
plt.savefig("data/spearman_heatmap.png")
plt.close()


# Pearson
pearson_correlations = pd.read_csv("data/pearson_correlations.csv")
pearson_correlations.set_index("Unnamed: 0", inplace=True)

fig = plt.figure(figsize=(6,6))
plt.title("Pearson Correlation Values")
hm = sns.heatmap(pearson_correlations, annot = True, annot_kws={"size": 7}, xticklabels = True, yticklabels = True)
hm.set_xticklabels(hm.get_xticklabels(), rotation=90, size = 7) 
hm.set_yticklabels(hm.get_yticklabels(), rotation=65, size = 7)

plt.xlabel("(in)equality index")
plt.ylabel("socio-economic status index")
plt.tight_layout()
plt.savefig("data/pearson_heatmap.png")
plt.close()