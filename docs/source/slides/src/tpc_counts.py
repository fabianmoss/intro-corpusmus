import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use("ggplot")
import seaborn as sns
sns.set_context("talk")

# colormaps
diverging_cmap = 'seismic'
diverging_palette = sns.color_palette(diverging_cmap, 35+6)[5:-1] # C = 0

def latex_accidentals(idx):
    idx = idx.str.replace("#", "$\\sharp$") \
        .str.replace("x", "$\\sharp\\sharp$") \
        .str.replace("b", "$\\flat$")
    return idx

def generate_lof():
    """returns a tripel:
        - list: line of fifths numbers; default: Fbb -- Bx
        - dict: name : number
        - dict: number : name
    """

    steps = {"F": -1, "C": 0, "G": 1, "D": 2, "A": 3, "E": 4, "B": 5}

    d = {}

    for step, accidentals in steps.items():
        d.update({step : accidentals})
    for step, accidentals in steps.items():
        d.update({step+'#' : accidentals+7})
    for step, accidentals in steps.items():
        d.update({step+'b' : accidentals-7})
    for step, accidentals in steps.items():
        d.update({step+'x' : accidentals+14})
    for step, accidentals in steps.items():
        d.update({step+'bb' : accidentals-14})

    lof = sorted(d, key=d.__getitem__)

    d2 = {v:k for k,v in d.items()}

    return lof, d, d2


if __name__ == "__main__":
    np.random.seed(1)
    df = pd.read_csv("./../../../../DCMLab/ExtendedTonality/data/DataFrames/Schubert_90_2.0_0.0.xml.csv") #Concerto_for_Solo_Piano_1st_Movement_Opus_39_No._8_in_G_Minor.mxl.csv
    lof = generate_lof()[0]

    fs = (10,5) # figsize

    # counts
    vals = df.tpc.value_counts().reindex(lof)
    counts = vals
    # counts = vals[vals.notnull()]
    counts.index = latex_accidentals(counts.index)

    fig, ax = plt.subplots(figsize=fs)
    ax.bar(np.arange(counts.shape[0]), counts)
    ax.set_xticks(np.arange(counts.shape[0]))
    ax.set_xticklabels(counts.index, rotation=90)

    plt.tight_layout()
    plt.savefig("./../img/tpc_dists.pdf")

    # sorted counts
    vals = df.tpc.value_counts().reindex(lof).sort_values(ascending=False)
    counts = vals[vals.notnull()]
    counts.index = latex_accidentals(counts.index)

    fig, ax = plt.subplots(figsize=fs)
    ax.bar(np.arange(counts.shape[0]), counts)
    ax.set_xticks(np.arange(counts.shape[0]))
    ax.set_xticklabels(counts.index, rotation=90)

    plt.tight_layout()
    plt.savefig("./../img/tpc_dists_sorted.pdf")
