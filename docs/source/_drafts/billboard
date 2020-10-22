Harmonic Clusters in Pop Charts
===============================

.. image:: _static/pop.jpg
   :width: 100%
   :align: center
   :alt: Photo by `israel palacio <https://unsplash.com/@othentikisra?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_ 
         on `Unsplash <https://unsplash.com/s/photos/music?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_.

Clustering analysis in :cite:`Schaffer2020`. 

.. code-block:: python

   def zipf_mandelbrot(x, a, b, c):
      """Zipf-Mandelbrot function of `x` given parameters `a`, `b`, `c`."""
      z = a / ( (b + x)**c )
      return z

The dataset
-----------

djfdjf

Research question
-----------------

Hypothesis: Corpus is not stylistically uniform but consists of several sub-styles,
each with respective harmonic sub-grammars.

Discussion: what is harmonic grammar/syntax (Riemann/GTTM/Rohrmeier)

Operationalization
------------------

Harmonic grammar --> bigrams (we know that already)

Clustering
----------

General idea 
............

Variance, minimizing *within-cluster sum of squares*, ...

Algorithm
.........

For data :math:`\mathbf{X}=\{x_1, x_2, \ldots, x_n\}`:

#. Choose :math:`k \leq n`.
#. Randomly assign means :math:`\mu_1, \ldots, \mu_k` to points in :math:`\mathbf{X}`.
#. Assign each point in :math:`\mathbf{X}` to cluster :math:`C_i` by determining closest mean :math:`\mu_i`.
#. Given a cluster :math:`C_i`, calculate its `centroid` :math:`m_i`:
   
   .. math:: 
      :nowrap:
      
      \begin{align*}
         m_i =\frac{1}{|C_i|}\sum_{x_j \in C_i} x_j
      \end{align*}

#. Repeat steps 3 and 4 until the means do not change anymore.

Note that, while this is a relatively simple clustering algorithm, it is not guaranteed that it 
finds the global optimal solution. This means that different `initializations` (step 2 of the algorithm)
might lead to different clustering results. More sophisticated clustering methods are, e.g. kNN...