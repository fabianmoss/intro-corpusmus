History of Tonality
-------------------

.. figure:: _static/score.jpg
   :width: 100%
   :align: center
   :alt: music score.

   Photo by `Marius Masalar <https://unsplash.com/@marius?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_ 
   on `Unsplash <https://unsplash.com/s/photos/scores?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_.

Principle Component Analysis
............................

Since the dimensionality of :math:`\Delta^{V-1}` is 35, it is impossible to visualize
this space and pieces in it to see whether their arrangement contains any meaningful information.
We address this problem by using a method for *dimensionality reduction*
called *Principal Component Analysis* (PCA) :cite:`Bishop2006`
that projects the data into a lower-dimensional space while at the same time maintaining
as many characteristic properties of the original space as possible.
PCA thus can aid to achieve a better understanding of
the global structure of the space. [#f1]_

PCA considers the data to be represented as a matrix

.. math:: 
   X = \left[\begin{array}{c}
                  x_1^\top \\
                  \vdots \\
                  x_D^\top \\
               \end{array}
            \right] \in [0,1]^{D \times V},\; 	x_d \in \Delta^{V-1},

where the rows are given by the :math:`D` data points, the pieces in the corpus,
and the columns are given by the :math:`V` features, the number of distinct tonal pitch-classes in the vocabulary.
All entries in :math:`X` range between 0 and 1 and all rows of :math:`X` sum to 1 because the pieces are represented
as distributions.
PCA determines the :math:`M\leq V` largest directions and magnitudes of the variance in the data in :math:`X` by first
calculating the *covariance matrix*

.. math:: K_X = \mathrm{cov}[X,X] = \mathrm{E}[(X-\bar{x})(X-\bar{x})^\top] \in\mathbb R^{D\times D},

where :math:`\mathrm{E}` denotes the expected value and :math:`\bar{x}\in[0,1]^V` is the mean of the columns of :math:`X`. 
The main directions of the variance in the data and their magnitude is given by the eigenvectors :math:`w_i` 
and eigenvalues :math:`\lambda_i` of :math:`K_X` which can be calculated by solving

.. math:: K \cdot w_i = \lambda \cdot w_i.

The projection into the lower-dimensional space is then achieved by selecting the :math:`M` largest eigenvalues 
and their corresponding eigenvectors and transform the data to :math:`X^\prime`, the dimensionality reduction of :math:`X` by

.. math:: X^\prime = X \cdot \left[ w_1, 	\ldots, w_M \right]\in \mathbb R^{D\times M}

The sum of all eigenvalues :math:`\lambda_i` is the total amount of variance in the data and the variance explained 
by each principal component is given by :math:`\lambda_i / \sum_j \lambda_j`.

In the present context, :math:`X` was transformed to have zero mean before applying PCA
but that the variance was not standardized to 1.
This was done because the features all are on the same scale and because the
differences in the variance between the respective tonal pitch-classes is of particular
interest here.

.. [#f1] While PCA is one of the most commonly used methods for dimensionality reduction, there are many others 
         (sometimes relying on particular assumptions about the distribution of the data).
         In a qualitative comparison, *Locally Linear Embedding* :cite:`Roweis2000` achieved a similar picture,
         whereas *t-distributed Stochastic Neighbor Embedding* (t-SNE) :cite:`VanDerMaaten2008` 
         that does emphasize the local over the global structure of the data did not.
         We opted here for PCA because it preserves most
         of the global structure and the interpretation of the results is straight-forward.