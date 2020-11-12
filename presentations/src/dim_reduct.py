from sklearn.manifold import SpectralEmbedding, LocallyLinearEmbedding, MDS, TSNE, Isomap
from sklearn.decomposition import PCA, FastICA
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("ggplot")
import sys
sys.path.append("../")
sys.path.append("../../../../DCMLab/ExtendedTonality")
from custom_functions import generate_lof
import seaborn as sns

args = {"n_components" : 35}

methods = {
    "PCA": PCA(whiten=True, **args),
    # "ICA" : FastICA(whiten=True, random_state=0, **args), # random state to keep rotation
    # "Isomap" : Isomap(**args),
    # "SE" : SpectralEmbedding(**args),
    # "LLE" : LocallyLinearEmbedding(**args),
    # "MDS" : MDS(n_components=2),
    # "t-SNE": TSNE(),
}

df = pd.read_csv("../../../../DCMLab/ExtendedTonality/lda/tpc_counts.tsv", sep="\t", index_col=0)
df = df.div(df.sum(axis=1), axis=0)
X = df.values

diverging_palette = sns.color_palette("seismic", 35+6)[5:-1]
lof = generate_lof()[1]
lof_nos = [lof[i] for i in df.idxmax(axis=1).values]
colors = [diverging_palette[j+15] for j in lof_nos]


if __name__ == "__main__":
    for i, (name, method) in enumerate(methods.items()):
        fit = method.fit(X)
        plt.plot(np.arange(35), np.cumsum(fit.explained_variance_ratio_), marker="o")
        plt.ylim(0,1)
        plt.ylabel("explained variance (PCA)")
        plt.savefig("./../img/explained_variance.pdf")
        # plt.show()

        # Principal Components
        fig, axes = plt.subplots(4,1, figsize=(12,8), sharex=True)
        for i, ax in enumerate(axes):
            ax.bar(np.arange(35), fit.components_[i], color=diverging_palette)
            ax.set_ylabel(f"PC {i+1} ({round(fit.explained_variance_ratio_[i], 2)})")
        axes[-1].set_xticks(np.arange(35))
        axes[-1].set_xticklabels(generate_lof()[0])
        plt.savefig("./../img/principal_components.pdf")
        # plt.show()

        # plot
        fig, ax = plt.subplots(figsize=(6,6))
        ax.axis('equal')
        X_ = method.fit_transform(X)
        # expl_var = X_.explained_variance_ratio_

        ax.scatter(X_[:,0], X_[:,1], color=colors, marker=".")
        # ax.set_title(name)

        plt.tight_layout()
        # plt.savefig(f"../img/dim_reduct_{name}.pdf")
        # plt.show()
