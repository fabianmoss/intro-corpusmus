Folk Songs and the Melodic Arc
==============================

.. image:: _static/03/lines.jpg
  :width: 100%
  :align: center
  :alt: Image by `Jerin J <https://unsplash.com/@jn1434?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_ 
        on `Unsplash <https://unsplash.com/s/photos/lines?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_.

.. raw:: latex

    \clearpage

Tones are among the basic elements of music. Most musical styles combine tones in different ways 
to create songs, chants, instrumental pieces, or other elaborate compositions. 
In this chapter, we will analyze some basice aspects of songs by studying distributions of tones and intervals.


Huron... / MusThe Tutorial

Data
----

http://kern.humdrum.org/data?f=zip&l=/essen
or http://kern.humdrum.org/help/data/ 

Open and read `README.txt`

Essen Folksong Collection

- keine Texte!

.. figure:: notebooks/02_Melody_I/img/german_song-1.png 
   :width: 90%
   :align: center

   German song *Die plappernden Junggesellen* from the Essen Folksong Collection.

Analysis:

- AABA' form 
- ascending / descending motives (local level) but also overall
- A' part elaboration of A by insertion of passing notes
- B part movement from ^3 to ^2

.. figure:: notebooks/02_Melody_I/img/chinese_song-1.png 
   :width: 90%
   :align: center

   Chinese song *Shengsi liangxianglian* from the Essen Folksong Collection.

Notes, Pitch Classes
--------------------

https://github.com/DCMLab/DigitalMusicologyExercises/tree/master/tone_profiles
   
means, variance

also multidimensional (for later)

Melodic Arc
-----------

Melodic arc was studied first by :cite:`Huron2006`.

.. figure:: notebooks/02_Melody_I/img/melodic_arc.png
   :align: center

   Melodic arc. The red lines in the background show the melodic profile of each song in the Essen Folksong Corpus;
   the thick black line shows the melodic arc that was obtained by using *Locally Weighted Scatterplot Smoothing* (LOWESS) :cite:`Cleveland1988`.
   The dashed horizontal line marks the mean standardized pitch, and the vertical dashed lines mark the quartiles of the songs,
   showing that most songs also have an arc-like shape at local formal levels.

Intervals
---------

https://github.com/DCMLab/DigitalMusicologyExercises/tree/master/interval_bigrams


maybe extend with Hansen and Pearce (2014) (but data not available?)

.. note:: 

   In this chapter we covered the following musical terms:
  
   - a 
   - b 
   - c