import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("ggplot")

# df = pd.read_csv("https://raw.githubusercontent.com/DCMLab/ABC/master/data/all_annotations.tsv", sep="\t")
# df.to_csv("./ABC.tsv", sep="\t")
df = pd.read_csv("./ABC.tsv", sep="\t")

df.chord.value_counts()[:20].plot(kind="bar", figsize=(6,3))
plt.tight_layout()
plt.savefig("./../img/chord_stats.pdf")
# plt.show()
