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