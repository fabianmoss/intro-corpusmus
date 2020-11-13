import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")
import numpy as np

df = pd.read_csv("composer_counts.csv", index_col="composer")
df = df.div(df.sum(axis=0), axis=1)

fig, axes = plt.subplots(4,1, figsize=(16,8), sharex=True)

for i, ax in enumerate(axes):
    ax.bar(np.arange(df.shape[0]), df[df.columns[i]])
    ax.set_ylabel(df.columns[i])
    ax.set_ylim(0,0.42)

axes[-1].set_xticks(np.arange(df.shape[0]))
axes[-1].set_xticklabels(df.index, rotation=90)

plt.tight_layout()
plt.savefig("./../img/composer_counts.pdf")
