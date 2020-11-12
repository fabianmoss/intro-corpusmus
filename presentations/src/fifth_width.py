import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
import seaborn as sns
sns.set_context("talk")
# plt.rcParams['axes.facecolor']='white'
epfldark = (0.3,0.3,0.3,0.8)
plt.rcParams['xtick.color']=epfldark
plt.rcParams['ytick.color']=epfldark

from statsmodels.nonparametric.smoothers_lowess import lowess

B = 750
fs = 24 # fontsize

if __name__ == "__main__":
    df = pd.read_csv("../../../../DCMLab/ExtendedTonality/metadata.csv", encoding="utf-8", sep="\t")
    df.composer = df.composer.astype("category")

    fig, ax = plt.subplots(figsize=(18,8))

    ax.scatter(
        df.display_year,
        df.fifth_width,
        # c=df.composer.cat.codes,
        marker=".",
        alpha=.5,
        color=epfldark,
        # cmap="rainbow"
        )

    for i in [6.5, 11.5]:
        ax.axhline(
            y=i,
            c='grey',
            ls="--")

    ax.set_xlabel("year", fontsize=fs, color=epfldark)
    ax.set_ylabel("fifth width", fontsize=fs, color=epfldark)
    ax.text(1980, 4.5, "diatonic", fontsize=fs, color=epfldark)
    ax.text(1980, 8.5, "chromatic", fontsize=fs, color=epfldark)
    ax.text(1980, 20, "enharmonic", fontsize=fs, color=epfldark)
    ax.tick_params(axis='x', labelsize=fs)
    ax.tick_params(axis='y', labelsize=fs)
    for b in range(B):
        samp = df.sample(df.shape[0], replace=True)
        x = samp.display_year
        y = samp.fifth_width

        l = lowess(y,x, frac=.15)
        ax.plot(l[:,0], l[:,1], c="red", alpha=.01)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(True)
    ax.spines['left'].set_visible(True)


    plt.tight_layout()
    plt.savefig("./../img/fifth_width.pdf")
    # plt.show()
