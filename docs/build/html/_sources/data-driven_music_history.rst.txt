Data-Driven Music History
=========================

Traditionally, musicology has been divided into historical and
systematic research agendas, encompassing qualitative-hermeneutic and
quantitative-empirical methodologies, respectively. Innovations in the
emerging and rapidly growing field of musical corpus studies question
this fundamental divide and address, for instance, inherently historical
questions with quantitative methods, fueled by the creation of ever
larger and more appropriate datasets.

This chapter first introduces some methodological and epistemological
issues regarding empirical approaches to music history. It then presents
a hands-on exercise on a case study. Finally, it invites critical
discussion about the implications and relevance of the results for other
subfields such as music psychology. In doing so, the workshop simulates
(nearly) the entire life cycle of a research project, from an initial
idea via selecting appropriate operationalisations and measures up to
choosing suitable visualisations to communicate the results, e.g. in a
research article or a blog post. At each point, participants will be
invited to critically reflect the decisions taken. Along the way, more
general methods for data analysis (e.g. data transformation, clustering,
dimensionality reduction, and plotting) will be introduced. This is
expected to benefit participants in a vast number of future projects.

.. code:: ipython3

    import pandas as pd # for working with tabular data
    pd.set_option('display.max_columns', 500)
    import matplotlib.pyplot as plt # for plotting
    plt.style.use("fivethirtyeight") # select specific plotting style
    import seaborn as sns; sns.set_context("talk")
    import numpy as np

Research Questions
------------------

-  General: How can we study historical changes quantitatively?
-  Specific: What can we say about the history of tonality based on a
   dataset of musical pieces?

A bit of theory
---------------

.. code:: ipython3

    note_names = list("FCGDAEB") # diatonic note names in fifths ordering
    note_names

.. parsed-literal::

    ['F', 'C', 'G', 'D', 'A', 'E', 'B']

.. code:: ipython3

    accidentals = ["bb", "b", "", "#", "##"] # up to two accidentals is suffient here
    accidentals

.. parsed-literal::

    ['bb', 'b', '', '#', '##']

.. code:: ipython3

    lof = [ n + a for a in accidentals for n in note_names ] # lof = "Line of Fifths"
    print(lof)


.. parsed-literal::

    ['Fbb', 'Cbb', 'Gbb', 'Dbb', 'Abb', 'Ebb', 'Bbb', 'Fb', 'Cb', 'Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#', 'E#', 'B#', 'F##', 'C##', 'G##', 'D##', 'A##', 'E##', 'B##']
    

.. code:: ipython3

    len(lof) # how long is this line-of-fifths segment?

.. parsed-literal::

    35

We call the elements on the line of fifths **tonal pitch-classes**

Data
----

A (kind of) large corpus: TP3C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here, we use a dataset that was specifically compiled for this kind of
analysis, the `Tonal pitch-class counts corpus
(TP3C) <https://github.com/DCMLab/TP3C>`__ :cite:`Moss2020b`. 

-  2,012 pieces
-  75 composers
-  approx. spans 600 years of music history
-  does not contain complete pieces but only counts of tonal
   pitch-classes

.. code:: ipython3

    import pandas as pd # to work with tabular data
    
    url = "https://raw.githubusercontent.com/DCMLab/TP3C/master/tp3c.tsv"
    data = pd.read_table(url)
    
    data.sample(10)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>composer</th>
          <th>composer_first</th>
          <th>work_group</th>
          <th>work_catalogue</th>
          <th>opus</th>
          <th>no</th>
          <th>mov</th>
          <th>title</th>
          <th>composition</th>
          <th>publication</th>
          <th>source</th>
          <th>display_year</th>
          <th>Fbb</th>
          <th>Cbb</th>
          <th>Gbb</th>
          <th>Dbb</th>
          <th>Abb</th>
          <th>Ebb</th>
          <th>Bbb</th>
          <th>Fb</th>
          <th>Cb</th>
          <th>Gb</th>
          <th>Db</th>
          <th>Ab</th>
          <th>Eb</th>
          <th>Bb</th>
          <th>F</th>
          <th>C</th>
          <th>G</th>
          <th>D</th>
          <th>A</th>
          <th>E</th>
          <th>B</th>
          <th>F#</th>
          <th>C#</th>
          <th>G#</th>
          <th>D#</th>
          <th>A#</th>
          <th>E#</th>
          <th>B#</th>
          <th>F##</th>
          <th>C##</th>
          <th>G##</th>
          <th>D##</th>
          <th>A##</th>
          <th>E##</th>
          <th>B##</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1311</th>
          <td>Schumann</td>
          <td>Robert</td>
          <td>Dichterliebe</td>
          <td>Op.</td>
          <td>48</td>
          <td>3</td>
          <td>NaN</td>
          <td>Die Rose, die Lilie, die Taube</td>
          <td>1840.0</td>
          <td>NaN</td>
          <td>OSLC</td>
          <td>1840.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>5</td>
          <td>52</td>
          <td>69</td>
          <td>61</td>
          <td>40</td>
          <td>45</td>
          <td>52</td>
          <td>48</td>
          <td>3</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>279</th>
          <td>Alkan</td>
          <td>Charles Valentin</td>
          <td>Esquisses</td>
          <td>Op.</td>
          <td>63</td>
          <td>37</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1861.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1861.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>2</td>
          <td>6</td>
          <td>128</td>
          <td>131</td>
          <td>48</td>
          <td>113</td>
          <td>144</td>
          <td>143</td>
          <td>68</td>
          <td>6</td>
          <td>8</td>
          <td>41</td>
          <td>34</td>
          <td>14</td>
          <td>12</td>
          <td>4</td>
          <td>3</td>
          <td>4</td>
          <td>4</td>
          <td>3</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>61</th>
          <td>Beethoven</td>
          <td>Ludwig van</td>
          <td>Piano Sonatas</td>
          <td>Op.</td>
          <td>22</td>
          <td>NaN</td>
          <td>1.0</td>
          <td>Piano Sonata No. 11</td>
          <td>1800.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1800.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>2</td>
          <td>6</td>
          <td>35</td>
          <td>111</td>
          <td>61</td>
          <td>284</td>
          <td>657</td>
          <td>650</td>
          <td>463</td>
          <td>339</td>
          <td>474</td>
          <td>422</td>
          <td>217</td>
          <td>63</td>
          <td>46</td>
          <td>42</td>
          <td>16</td>
          <td>4</td>
          <td>5</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>208</th>
          <td>Liszt</td>
          <td>Franz</td>
          <td>12 Transcendental Etudes</td>
          <td>S.</td>
          <td>139</td>
          <td>7</td>
          <td>NaN</td>
          <td>Eroica</td>
          <td>1851.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1851.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>4</td>
          <td>15</td>
          <td>129</td>
          <td>148</td>
          <td>225</td>
          <td>297</td>
          <td>376</td>
          <td>393</td>
          <td>296</td>
          <td>225</td>
          <td>163</td>
          <td>156</td>
          <td>130</td>
          <td>137</td>
          <td>113</td>
          <td>88</td>
          <td>56</td>
          <td>42</td>
          <td>45</td>
          <td>15</td>
          <td>32</td>
          <td>6</td>
          <td>5</td>
          <td>7</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1010</th>
          <td>Busnoys</td>
          <td>Antoine</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Mon seul et celé souvenir</td>
          <td>1480.0</td>
          <td>NaN</td>
          <td>ELVIS</td>
          <td>1480.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>12</td>
          <td>58</td>
          <td>55</td>
          <td>29</td>
          <td>84</td>
          <td>59</td>
          <td>55</td>
          <td>13</td>
          <td>1</td>
          <td>6</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>900</th>
          <td>Lang</td>
          <td>Josephine</td>
          <td>Sechs Lieder</td>
          <td>Op.</td>
          <td>25</td>
          <td>3</td>
          <td>NaN</td>
          <td>Barcarole</td>
          <td>NaN</td>
          <td>1860.0</td>
          <td>OSLC</td>
          <td>1860.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>4</td>
          <td>2</td>
          <td>55</td>
          <td>99</td>
          <td>107</td>
          <td>81</td>
          <td>59</td>
          <td>84</td>
          <td>44</td>
          <td>8</td>
          <td>2</td>
          <td>7</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>317</th>
          <td>Beethoven</td>
          <td>Ludwig van</td>
          <td>Piano Sonatas</td>
          <td>Op.</td>
          <td>49</td>
          <td>2</td>
          <td>1.0</td>
          <td>Piano Sonata No. 20</td>
          <td>NaN</td>
          <td>1805.0</td>
          <td>MS</td>
          <td>1805.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>26</td>
          <td>139</td>
          <td>273</td>
          <td>335</td>
          <td>259</td>
          <td>144</td>
          <td>231</td>
          <td>175</td>
          <td>46</td>
          <td>12</td>
          <td>13</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1120</th>
          <td>Reichardt</td>
          <td>Louise</td>
          <td>Zwölf Deutsche und Italiänische Romantische Ge...</td>
          <td>Op.</td>
          <td>NaN</td>
          <td>2</td>
          <td>NaN</td>
          <td>Wenn ich ihn nur habe</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>OSLC</td>
          <td>1802.5</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>1</td>
          <td>0</td>
          <td>10</td>
          <td>40</td>
          <td>39</td>
          <td>21</td>
          <td>18</td>
          <td>22</td>
          <td>16</td>
          <td>9</td>
          <td>1</td>
          <td>5</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1754</th>
          <td>Corelli</td>
          <td>Arcangelo</td>
          <td>12 Trio Sonatas</td>
          <td>Op.</td>
          <td>3</td>
          <td>6</td>
          <td>1.0</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1689.0</td>
          <td>CCARH</td>
          <td>1689.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>65</td>
          <td>117</td>
          <td>104</td>
          <td>68</td>
          <td>77</td>
          <td>81</td>
          <td>59</td>
          <td>13</td>
          <td>0</td>
          <td>8</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1979</th>
          <td>Mozart</td>
          <td>Wolfgang Amadeus</td>
          <td>Sonaten</td>
          <td>KV</td>
          <td>331</td>
          <td>11</td>
          <td>1.0</td>
          <td>Var. 4</td>
          <td>1783.0</td>
          <td>NaN</td>
          <td>CCARH</td>
          <td>1783.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>44</td>
          <td>108</td>
          <td>119</td>
          <td>66</td>
          <td>18</td>
          <td>86</td>
          <td>37</td>
          <td>4</td>
          <td>0</td>
          <td>1</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    data.display_year.plot(kind="hist", bins=50, figsize=(15,6)); # historical overview



.. image:: output_13_0.png


-  it can be seen that there are large gaps and that some historical
   periods are underrepresented
-  however, it is not so obvious how to fix that
-  do we want a uniform distribution over time?
-  do we want a “historically accurate” distribution?
-  do we want to remove geographical/gender/class/instrument/etc.
   biases?
-  on one hand, balanced datasets are likely not to reflect historical
   realities
-  on the other hand, such datasets rather represent the “canon”, that
   is a contemporary selection of “valuable” compositions that may
   differ greatly from what was considered relevant at the time

–> There is no unique objective answer to these questions. It is
important to be aware of these limitations and take them into account
when interpreting the results

For this workshop we ignore all the metadata about the pieces (titles,
composer names etc.) but only focus on their tonal material. Therefore,
we don’t need all the columns of the table.

.. code:: ipython3

    tpc_counts = data.loc[:, lof] # select all rows (":") and the lof columns
    tpc_counts.sample(20)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Fbb</th>
          <th>Cbb</th>
          <th>Gbb</th>
          <th>Dbb</th>
          <th>Abb</th>
          <th>Ebb</th>
          <th>Bbb</th>
          <th>Fb</th>
          <th>Cb</th>
          <th>Gb</th>
          <th>Db</th>
          <th>Ab</th>
          <th>Eb</th>
          <th>Bb</th>
          <th>F</th>
          <th>C</th>
          <th>G</th>
          <th>D</th>
          <th>A</th>
          <th>E</th>
          <th>B</th>
          <th>F#</th>
          <th>C#</th>
          <th>G#</th>
          <th>D#</th>
          <th>A#</th>
          <th>E#</th>
          <th>B#</th>
          <th>F##</th>
          <th>C##</th>
          <th>G##</th>
          <th>D##</th>
          <th>A##</th>
          <th>E##</th>
          <th>B##</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1233</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>14</td>
          <td>79</td>
          <td>101</td>
          <td>30</td>
          <td>13</td>
          <td>53</td>
          <td>34</td>
          <td>2</td>
          <td>0</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1779</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>32</td>
          <td>56</td>
          <td>21</td>
          <td>33</td>
          <td>61</td>
          <td>66</td>
          <td>37</td>
          <td>3</td>
          <td>3</td>
          <td>13</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>254</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>3</td>
          <td>44</td>
          <td>50</td>
          <td>154</td>
          <td>441</td>
          <td>541</td>
          <td>408</td>
          <td>488</td>
          <td>657</td>
          <td>604</td>
          <td>334</td>
          <td>66</td>
          <td>78</td>
          <td>164</td>
          <td>71</td>
          <td>6</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1704</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>54</td>
          <td>67</td>
          <td>76</td>
          <td>64</td>
          <td>55</td>
          <td>65</td>
          <td>42</td>
          <td>4</td>
          <td>0</td>
          <td>6</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1647</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>6</td>
          <td>51</td>
          <td>71</td>
          <td>61</td>
          <td>53</td>
          <td>70</td>
          <td>99</td>
          <td>70</td>
          <td>29</td>
          <td>16</td>
          <td>32</td>
          <td>14</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>715</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>16</td>
          <td>0</td>
          <td>75</td>
          <td>49</td>
          <td>105</td>
          <td>111</td>
          <td>112</td>
          <td>145</td>
          <td>621</td>
          <td>88</td>
          <td>61</td>
          <td>46</td>
          <td>41</td>
          <td>20</td>
          <td>46</td>
          <td>32</td>
          <td>13</td>
          <td>20</td>
          <td>12</td>
          <td>2</td>
          <td>63</td>
          <td>7</td>
          <td>2</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1672</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>1</td>
          <td>0</td>
          <td>45</td>
          <td>57</td>
          <td>36</td>
          <td>57</td>
          <td>64</td>
          <td>73</td>
          <td>49</td>
          <td>10</td>
          <td>0</td>
          <td>15</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>837</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>4</td>
          <td>14</td>
          <td>21</td>
          <td>16</td>
          <td>15</td>
          <td>18</td>
          <td>12</td>
          <td>11</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>741</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>13</td>
          <td>84</td>
          <td>141</td>
          <td>138</td>
          <td>199</td>
          <td>267</td>
          <td>296</td>
          <td>310</td>
          <td>300</td>
          <td>306</td>
          <td>415</td>
          <td>282</td>
          <td>308</td>
          <td>382</td>
          <td>239</td>
          <td>138</td>
          <td>134</td>
          <td>84</td>
          <td>77</td>
          <td>23</td>
          <td>19</td>
          <td>15</td>
          <td>0</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1595</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>4</td>
          <td>4</td>
          <td>14</td>
          <td>8</td>
          <td>51</td>
          <td>209</td>
          <td>252</td>
          <td>244</td>
          <td>144</td>
          <td>163</td>
          <td>158</td>
          <td>80</td>
          <td>22</td>
          <td>11</td>
          <td>8</td>
          <td>13</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>513</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>4</td>
          <td>14</td>
          <td>37</td>
          <td>214</td>
          <td>228</td>
          <td>85</td>
          <td>253</td>
          <td>322</td>
          <td>271</td>
          <td>173</td>
          <td>104</td>
          <td>47</td>
          <td>90</td>
          <td>71</td>
          <td>14</td>
          <td>5</td>
          <td>0</td>
          <td>11</td>
          <td>6</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1502</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>11</td>
          <td>16</td>
          <td>7</td>
          <td>12</td>
          <td>17</td>
          <td>17</td>
          <td>11</td>
          <td>3</td>
          <td>0</td>
          <td>4</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1121</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>16</td>
          <td>27</td>
          <td>0</td>
          <td>20</td>
          <td>44</td>
          <td>34</td>
          <td>27</td>
          <td>3</td>
          <td>0</td>
          <td>18</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1959</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>6</td>
          <td>36</td>
          <td>38</td>
          <td>49</td>
          <td>33</td>
          <td>32</td>
          <td>28</td>
          <td>19</td>
          <td>8</td>
          <td>8</td>
          <td>3</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>169</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>13</td>
          <td>75</td>
          <td>107</td>
          <td>123</td>
          <td>125</td>
          <td>118</td>
          <td>111</td>
          <td>84</td>
          <td>27</td>
          <td>7</td>
          <td>12</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1777</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>1</td>
          <td>75</td>
          <td>135</td>
          <td>81</td>
          <td>110</td>
          <td>126</td>
          <td>181</td>
          <td>108</td>
          <td>27</td>
          <td>8</td>
          <td>26</td>
          <td>7</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>665</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>24</td>
          <td>100</td>
          <td>28</td>
          <td>99</td>
          <td>311</td>
          <td>289</td>
          <td>121</td>
          <td>410</td>
          <td>395</td>
          <td>814</td>
          <td>386</td>
          <td>179</td>
          <td>533</td>
          <td>225</td>
          <td>121</td>
          <td>66</td>
          <td>149</td>
          <td>53</td>
          <td>3</td>
          <td>10</td>
          <td>0</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>436</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>9</td>
          <td>124</td>
          <td>57</td>
          <td>63</td>
          <td>171</td>
          <td>188</td>
          <td>108</td>
          <td>66</td>
          <td>101</td>
          <td>90</td>
          <td>43</td>
          <td>21</td>
          <td>33</td>
          <td>18</td>
          <td>5</td>
          <td>1</td>
          <td>2</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>690</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>20</td>
          <td>25</td>
          <td>7</td>
          <td>25</td>
          <td>47</td>
          <td>45</td>
          <td>27</td>
          <td>0</td>
          <td>0</td>
          <td>14</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>1526</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>16</td>
          <td>14</td>
          <td>11</td>
          <td>98</td>
          <td>236</td>
          <td>496</td>
          <td>106</td>
          <td>127</td>
          <td>182</td>
          <td>101</td>
          <td>37</td>
          <td>8</td>
          <td>20</td>
          <td>11</td>
          <td>20</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    piece = tpc_counts.iloc[10]
    
    fig, axes = plt.subplots(2, 1, figsize=(20,10))
    
    axes[0].bar(piece.sort_values(ascending=False).index, piece.sort_values(ascending=False))
    axes[0].set_title("'without theory'")
    
    axes[1].bar(piece.index, piece)
    axes[1].set_title("'with theory'")
    
    plt.savefig("img/random_piece.png")
    plt.show()



.. image:: output_17_0.png


Let us have an overview of the note counts in these pieces!

If we would just look at the raw counts of the tonal pitch-classe, we
could not learn much from it. Using a theoretical model (the line of
fifths) shows that the notes in pieces are usually come from few
adjacent keys (you don’t say!).

.. figure:: img/random_piece.png
   :alt: Random piece

   Random piece

We probably have very long pieces (sonatas) and very short pieces
(songs) in the dataset. Since we don’t want length (or the absolute
number of notes in a piece) to have an effect, we rather consider tonal
pitch-class distributions instead counts, by normalizing all pieces to
sum to one.

.. code:: ipython3

    tpc_dists = tpc_counts.div(tpc_counts.sum(axis=1), axis=0)
    tpc_dists.sample(20)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Fbb</th>
          <th>Cbb</th>
          <th>Gbb</th>
          <th>Dbb</th>
          <th>Abb</th>
          <th>Ebb</th>
          <th>Bbb</th>
          <th>Fb</th>
          <th>Cb</th>
          <th>Gb</th>
          <th>Db</th>
          <th>Ab</th>
          <th>Eb</th>
          <th>Bb</th>
          <th>F</th>
          <th>C</th>
          <th>G</th>
          <th>D</th>
          <th>A</th>
          <th>E</th>
          <th>B</th>
          <th>F#</th>
          <th>C#</th>
          <th>G#</th>
          <th>D#</th>
          <th>A#</th>
          <th>E#</th>
          <th>B#</th>
          <th>F##</th>
          <th>C##</th>
          <th>G##</th>
          <th>D##</th>
          <th>A##</th>
          <th>E##</th>
          <th>B##</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1658</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.011364</td>
          <td>0.034091</td>
          <td>0.034091</td>
          <td>0.090909</td>
          <td>0.113636</td>
          <td>0.090909</td>
          <td>0.068182</td>
          <td>0.102273</td>
          <td>0.056818</td>
          <td>0.125000</td>
          <td>0.136364</td>
          <td>0.045455</td>
          <td>0.034091</td>
          <td>0.056818</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>109</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000668</td>
          <td>0.016700</td>
          <td>0.086172</td>
          <td>0.113560</td>
          <td>0.111556</td>
          <td>0.125585</td>
          <td>0.157649</td>
          <td>0.156981</td>
          <td>0.120240</td>
          <td>0.047428</td>
          <td>0.022044</td>
          <td>0.021376</td>
          <td>0.018036</td>
          <td>0.002004</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>353</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.023077</td>
          <td>0.117692</td>
          <td>0.150769</td>
          <td>0.136154</td>
          <td>0.137692</td>
          <td>0.144615</td>
          <td>0.136154</td>
          <td>0.104615</td>
          <td>0.026154</td>
          <td>0.010000</td>
          <td>0.013077</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>137</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.003731</td>
          <td>0.016169</td>
          <td>0.085821</td>
          <td>0.134328</td>
          <td>0.125622</td>
          <td>0.139303</td>
          <td>0.130597</td>
          <td>0.141791</td>
          <td>0.125622</td>
          <td>0.055970</td>
          <td>0.019900</td>
          <td>0.012438</td>
          <td>0.008706</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>611</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.065393</td>
          <td>0.046289</td>
          <td>0.072006</td>
          <td>0.089640</td>
          <td>0.160911</td>
          <td>0.231447</td>
          <td>0.122704</td>
          <td>0.058046</td>
          <td>0.071271</td>
          <td>0.047024</td>
          <td>0.025716</td>
          <td>0.005143</td>
          <td>0.001470</td>
          <td>0.000000</td>
          <td>0.002204</td>
          <td>0.000000</td>
          <td>0.000735</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>1741</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.003036</td>
          <td>0.090081</td>
          <td>0.178138</td>
          <td>0.176113</td>
          <td>0.153846</td>
          <td>0.135628</td>
          <td>0.122470</td>
          <td>0.103239</td>
          <td>0.012146</td>
          <td>0.018219</td>
          <td>0.007085</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>495</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.022403</td>
          <td>0.026477</td>
          <td>0.012220</td>
          <td>0.075356</td>
          <td>0.226069</td>
          <td>0.228106</td>
          <td>0.107943</td>
          <td>0.077393</td>
          <td>0.075356</td>
          <td>0.109980</td>
          <td>0.028513</td>
          <td>0.000000</td>
          <td>0.010183</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>248</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.004561</td>
          <td>0.102623</td>
          <td>0.002281</td>
          <td>0.047891</td>
          <td>0.139111</td>
          <td>0.407070</td>
          <td>0.131129</td>
          <td>0.026226</td>
          <td>0.036488</td>
          <td>0.096921</td>
          <td>0.005701</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>1152</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.039175</td>
          <td>0.245361</td>
          <td>0.158763</td>
          <td>0.107216</td>
          <td>0.131959</td>
          <td>0.173196</td>
          <td>0.103093</td>
          <td>0.041237</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>1599</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.016138</td>
          <td>0.008646</td>
          <td>0.054179</td>
          <td>0.134294</td>
          <td>0.170605</td>
          <td>0.122767</td>
          <td>0.088761</td>
          <td>0.154467</td>
          <td>0.112968</td>
          <td>0.064553</td>
          <td>0.021326</td>
          <td>0.011527</td>
          <td>0.014409</td>
          <td>0.023055</td>
          <td>0.002305</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>606</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.059524</td>
          <td>0.059524</td>
          <td>0.061905</td>
          <td>0.235714</td>
          <td>0.161905</td>
          <td>0.147619</td>
          <td>0.104762</td>
          <td>0.057143</td>
          <td>0.054762</td>
          <td>0.045238</td>
          <td>0.007143</td>
          <td>0.004762</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>731</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.022831</td>
          <td>0.091324</td>
          <td>0.063927</td>
          <td>0.105023</td>
          <td>0.082192</td>
          <td>0.125571</td>
          <td>0.148402</td>
          <td>0.136986</td>
          <td>0.086758</td>
          <td>0.063927</td>
          <td>0.027397</td>
          <td>0.031963</td>
          <td>0.013699</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>82</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.004723</td>
          <td>0.069658</td>
          <td>0.269185</td>
          <td>0.165289</td>
          <td>0.108619</td>
          <td>0.077922</td>
          <td>0.107438</td>
          <td>0.118064</td>
          <td>0.036600</td>
          <td>0.015348</td>
          <td>0.008264</td>
          <td>0.017710</td>
          <td>0.000000</td>
          <td>0.001181</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>935</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.088496</td>
          <td>0.143363</td>
          <td>0.176991</td>
          <td>0.141593</td>
          <td>0.139823</td>
          <td>0.162832</td>
          <td>0.120354</td>
          <td>0.023009</td>
          <td>0.000000</td>
          <td>0.001770</td>
          <td>0.001770</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>670</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.001664</td>
          <td>0.003177</td>
          <td>0.004993</td>
          <td>0.010743</td>
          <td>0.009684</td>
          <td>0.032531</td>
          <td>0.097140</td>
          <td>0.106219</td>
          <td>0.079437</td>
          <td>0.131185</td>
          <td>0.113330</td>
          <td>0.165229</td>
          <td>0.100620</td>
          <td>0.034196</td>
          <td>0.041610</td>
          <td>0.041459</td>
          <td>0.014223</td>
          <td>0.007263</td>
          <td>0.004388</td>
          <td>0.000605</td>
          <td>0.000000</td>
          <td>0.000303</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>564</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.038182</td>
          <td>0.098182</td>
          <td>0.076364</td>
          <td>0.109091</td>
          <td>0.121818</td>
          <td>0.132727</td>
          <td>0.250909</td>
          <td>0.083636</td>
          <td>0.007273</td>
          <td>0.014545</td>
          <td>0.052727</td>
          <td>0.012727</td>
          <td>0.001818</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>404</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000507</td>
          <td>0.001013</td>
          <td>0.006079</td>
          <td>0.021783</td>
          <td>0.069402</td>
          <td>0.107396</td>
          <td>0.100304</td>
          <td>0.110942</td>
          <td>0.155015</td>
          <td>0.152482</td>
          <td>0.112969</td>
          <td>0.059777</td>
          <td>0.030395</td>
          <td>0.039007</td>
          <td>0.026342</td>
          <td>0.006079</td>
          <td>0.000507</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>341</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.006089</td>
          <td>0.012855</td>
          <td>0.019621</td>
          <td>0.016915</td>
          <td>0.092693</td>
          <td>0.179296</td>
          <td>0.209743</td>
          <td>0.098782</td>
          <td>0.076455</td>
          <td>0.113667</td>
          <td>0.098106</td>
          <td>0.058187</td>
          <td>0.008119</td>
          <td>0.004736</td>
          <td>0.004736</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>371</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.028169</td>
          <td>0.089924</td>
          <td>0.195016</td>
          <td>0.173348</td>
          <td>0.136511</td>
          <td>0.109426</td>
          <td>0.140845</td>
          <td>0.081257</td>
          <td>0.023835</td>
          <td>0.014085</td>
          <td>0.005417</td>
          <td>0.002167</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
        <tr>
          <th>53</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000898</td>
          <td>0.007181</td>
          <td>0.026032</td>
          <td>0.073609</td>
          <td>0.101436</td>
          <td>0.095153</td>
          <td>0.147217</td>
          <td>0.164273</td>
          <td>0.151706</td>
          <td>0.114004</td>
          <td>0.033214</td>
          <td>0.033214</td>
          <td>0.038600</td>
          <td>0.012567</td>
          <td>0.000898</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
        </tr>
      </tbody>
    </table>
    </div>



For further numerical analysis, we extract the data from this table and
assign it to a variable ``X``.

.. code:: ipython3

    # extract values of table to matrix
    X = tpc_dists.values
    
    X.shape # shows (#rows, #columns) of X




.. parsed-literal::

    (2012, 35)



Now, ``X`` is a 2012 :math:`\times` 35 matrix where the rows represent
the pieces and the columns (also called “features” or “dimensions”)
represent the relative frequency of tonal pitch-classes.

Thinking in 35 dimensions is quite difficult for most people. Without
trying to imagine what this would look like, what can we already say
about this data?

Since each piece is a point in this 35-D space and pieces are
represented as vectors, pieces that have similar tonal pitch-class
distributions must be close in this space (whatever this looks like).

What groups of pieces that cluster together? Maybe pieces of the same
composer are similar to each other? Maybe pieces from a similar time?
Maybe pieces for the same instruments?

If we find clusters, these would still be in 35-D and thus difficult to
interpret. Luckily, there are a range of so-called *dimensionality
reduction* methods that transform the data into lower-dimensional spaces
so that we actually can look at them.

A very common dimensionality reduction method is **Principal Components
Analysis (PCA)**.

The basic idea of PCA is:

-  find dimensions in the data that maximize the variance in this
   direction
-  these dimensions have to be orthogonal to each other (mutually
   independent)
-  these dimensions are called the *principal components*
-  each principal component is associated with how much of the data
   variance it explains

.. code:: ipython3

    import numpy as np # for numerical computations
    import sklearn
    from sklearn.decomposition import PCA # for dimensionality reduction
    
    pca = sklearn.decomposition.PCA(n_components=35) # initialize PCA with 35 dimensions
    pca.fit(X) # apply it to the data
    variance = pca.explained_variance_ratio_ # assign explained variance to variable

.. code:: ipython3

    fig, ax = plt.subplots(figsize=(14,5))
    x = np.arange(35)
    ax.plot(x, variance, label="relative", marker="o")
    ax.plot(x, variance.cumsum(), label="cumulative", marker="o")
    ax.set_xlim(-0.5, 35)
    ax.set_ylim(-0.1, 1.1)
    ax.set_xlabel("Principal Components")
    ax.set_ylabel("Explained variance")
    plt.xticks(np.arange(len(lof)), np.arange(len(lof)) + 1) # because Pyhon starts counting at 0
    
    plt.legend(loc="center right")
    plt.tight_layout()
    plt.savefig("img/explained_variance.png")
    plt.show()



.. image:: output_30_0.png


.. figure:: img/explained_variance.png
   :alt: explained variance

   explained variance

.. code:: ipython3

    variance[:5]




.. parsed-literal::

    array([0.41144591, 0.23410347, 0.09063507, 0.07574242, 0.04436989])



The first principal component explains 41.1% of the variance of the
data, the second explains 23.4% and the third 9%. Together, this amounts
to 73.6%.

Almost three quarters of the variance in the dataset is retained by
reducing the dimensionality from 35 to 3 dimensions (8.6%)! If we reduce
the data to two dimensions, we still can explain :math:`\approx` 65% of
the variance.

This is great because it means that we can look at the data in 2 or 3
dimensions without loosing too much information.

Recovering the line of fifths from data
---------------------------------------

.. code:: ipython3

    pca3d = PCA(n_components=3)
    pca3d.fit(X)
    
    X_ = pca3d.transform(X)
    X_.shape




.. parsed-literal::

    (2012, 3)



.. code:: ipython3

    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure(figsize=(6,6))
    
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X_[:,0], X_[:,1], X_[:,2], s=50, alpha=.25) # c=cs,
    ax.set_xlabel("PC 1", labelpad=30)
    ax.set_ylabel("PC 2", labelpad=30)
    ax.set_zlabel("PC 3", labelpad=30)
    
    plt.tight_layout()
    plt.savefig("img/3d_scatter.png")
    plt.show()



.. image:: output_38_0.png


.. figure:: img/3d_scatter.png
   :alt: 3D Scatterplot

   3D Scatterplot

Each piece in this plot is represented by a point in 3-D space. But
remember that this location represents ~75% of the information contained
in the full tonal pitch-class distribution. In 35-D space each dimension
corresponded to the relative frequency of a tonal pitch-class in a
piece.

-  What do these three dimensions signify?
-  How can we interpret them?

Fortunately, we can inspect them individually and try to interpret what
we see.

.. code:: ipython3

    from itertools import combinations
    
    fig, axes = plt.subplots(1,3, sharey=True, figsize=(24,8))
    
    for k, (i, j) in enumerate(combinations(range(3), 2)):
    
        axes[k].scatter(X_[:,i], X_[:,j], s=50, alpha=.25, edgecolor=None)
        axes[k].set_xlabel(f"PC {i+1}")
        axes[k].set_ylabel(f"PC {j+1}")
        axes[k].set_aspect("equal")
    
    plt.tight_layout()
    plt.savefig("img/3d_dimension_pairs.png")
    plt.show()



.. image:: output_41_0.png


.. figure:: img/3d_dimension_pairs.png
   :alt: Principal Components

   Principal Components

Clearly, looking at two principal components at a time shows that there
is some latent structure in the data. How can we understand it better?

One way to see whether the pieces are clustered together systematically
be coloring them according to some criterion.

As always, many different options are available. For the present purpose
we will use the most simple summary of the piece: its most frequent note
(which is the *mode* of its pitch-class distribution in statistical
terms) and call this note its **tonal center**.

This will also allow to map the tonal pitch-classes on the line of
fifths to colors.

.. figure:: img/lof.png
   :alt: Line of fifths coloring

   Line of fifths coloring

.. code:: ipython3

    tpc_dists["tonal_center"] = tpc_dists.apply(lambda piece: np.argmax(piece[lof].values) - 15, axis=1)
    tpc_dists.sample(10)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>Fbb</th>
          <th>Cbb</th>
          <th>Gbb</th>
          <th>Dbb</th>
          <th>Abb</th>
          <th>Ebb</th>
          <th>Bbb</th>
          <th>Fb</th>
          <th>Cb</th>
          <th>Gb</th>
          <th>Db</th>
          <th>Ab</th>
          <th>Eb</th>
          <th>Bb</th>
          <th>F</th>
          <th>C</th>
          <th>G</th>
          <th>D</th>
          <th>A</th>
          <th>E</th>
          <th>B</th>
          <th>F#</th>
          <th>C#</th>
          <th>G#</th>
          <th>D#</th>
          <th>A#</th>
          <th>E#</th>
          <th>B#</th>
          <th>F##</th>
          <th>C##</th>
          <th>G##</th>
          <th>D##</th>
          <th>A##</th>
          <th>E##</th>
          <th>B##</th>
          <th>tonal_center</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>319</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.049020</td>
          <td>0.105392</td>
          <td>0.193627</td>
          <td>0.088235</td>
          <td>0.128676</td>
          <td>0.155637</td>
          <td>0.172794</td>
          <td>0.067402</td>
          <td>0.000000</td>
          <td>0.006127</td>
          <td>0.029412</td>
          <td>0.003676</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>-2</td>
        </tr>
        <tr>
          <th>959</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.029730</td>
          <td>0.113514</td>
          <td>0.129730</td>
          <td>0.118919</td>
          <td>0.189189</td>
          <td>0.205405</td>
          <td>0.140541</td>
          <td>0.062162</td>
          <td>0.000000</td>
          <td>0.008108</td>
          <td>0.002703</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>3</td>
        </tr>
        <tr>
          <th>213</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000536</td>
          <td>0.014464</td>
          <td>0.002321</td>
          <td>0.010536</td>
          <td>0.087321</td>
          <td>0.116250</td>
          <td>0.044643</td>
          <td>0.088750</td>
          <td>0.110714</td>
          <td>0.115536</td>
          <td>0.097857</td>
          <td>0.031429</td>
          <td>0.023929</td>
          <td>0.072500</td>
          <td>0.067143</td>
          <td>0.036786</td>
          <td>0.014464</td>
          <td>0.006250</td>
          <td>0.023929</td>
          <td>0.009643</td>
          <td>0.010357</td>
          <td>0.005536</td>
          <td>0.001964</td>
          <td>0.005000</td>
          <td>0.000000</td>
          <td>0.002143</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>-5</td>
        </tr>
        <tr>
          <th>914</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.004326</td>
          <td>0.004851</td>
          <td>0.018747</td>
          <td>0.012192</td>
          <td>0.021893</td>
          <td>0.044442</td>
          <td>0.029759</td>
          <td>0.039984</td>
          <td>0.064761</td>
          <td>0.072889</td>
          <td>0.070661</td>
          <td>0.072496</td>
          <td>0.093078</td>
          <td>0.114709</td>
          <td>0.103828</td>
          <td>0.062533</td>
          <td>0.057682</td>
          <td>0.054536</td>
          <td>0.031463</td>
          <td>0.012585</td>
          <td>0.005768</td>
          <td>0.004457</td>
          <td>0.002360</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>6</td>
        </tr>
        <tr>
          <th>127</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.004911</td>
          <td>0.012500</td>
          <td>0.039732</td>
          <td>0.095089</td>
          <td>0.156250</td>
          <td>0.115625</td>
          <td>0.119196</td>
          <td>0.145536</td>
          <td>0.153125</td>
          <td>0.076339</td>
          <td>0.022768</td>
          <td>0.011607</td>
          <td>0.036607</td>
          <td>0.009821</td>
          <td>0.000446</td>
          <td>0.000446</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>1</td>
        </tr>
        <tr>
          <th>711</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.005298</td>
          <td>0.066225</td>
          <td>0.127152</td>
          <td>0.152318</td>
          <td>0.050331</td>
          <td>0.107285</td>
          <td>0.182781</td>
          <td>0.147020</td>
          <td>0.068874</td>
          <td>0.014570</td>
          <td>0.014570</td>
          <td>0.049007</td>
          <td>0.010596</td>
          <td>0.000000</td>
          <td>0.001325</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.002649</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>-1</td>
        </tr>
        <tr>
          <th>879</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.135371</td>
          <td>0.139738</td>
          <td>0.135371</td>
          <td>0.165939</td>
          <td>0.170306</td>
          <td>0.135371</td>
          <td>0.117904</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>3</td>
        </tr>
        <tr>
          <th>1020</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.016349</td>
          <td>0.138965</td>
          <td>0.070845</td>
          <td>0.076294</td>
          <td>0.237057</td>
          <td>0.209809</td>
          <td>0.147139</td>
          <td>0.057221</td>
          <td>0.002725</td>
          <td>0.035422</td>
          <td>0.008174</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>858</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.008929</td>
          <td>0.125000</td>
          <td>0.178571</td>
          <td>0.133929</td>
          <td>0.125000</td>
          <td>0.178571</td>
          <td>0.125000</td>
          <td>0.125000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00000</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>755</th>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000000</td>
          <td>0.000960</td>
          <td>0.000960</td>
          <td>0.001440</td>
          <td>0.006721</td>
          <td>0.002880</td>
          <td>0.006721</td>
          <td>0.016323</td>
          <td>0.033125</td>
          <td>0.033125</td>
          <td>0.033605</td>
          <td>0.053289</td>
          <td>0.088814</td>
          <td>0.149784</td>
          <td>0.071051</td>
          <td>0.097456</td>
          <td>0.157945</td>
          <td>0.063370</td>
          <td>0.087854</td>
          <td>0.018243</td>
          <td>0.019203</td>
          <td>0.047048</td>
          <td>0.009602</td>
          <td>0.000000</td>
          <td>0.0</td>
          <td>0.00048</td>
          <td>0.0</td>
          <td>0.0</td>
          <td>8</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    from matplotlib import cm
    from matplotlib.colors import Normalize
    
    #normalize item number values to colormap
    norm = Normalize(vmin=-15, vmax=20)
    
    # cs = [ cm.seismic(norm(c)) for c in data["tonal_center"]]
    cs = [ cm.seismic(norm(c)) for c in tpc_dists["tonal_center"]]

.. figure:: img/3d_dimension_pairs.png
   :alt: Dimension pairs

   Dimension pairs

.. code:: ipython3

    from itertools import combinations
    
    fig, axes = plt.subplots(1,3, sharey=True, figsize=(24,8))
    
    for k, (i, j) in enumerate(combinations(range(3), 2)):
    
        axes[k].scatter(X_[:,i], X_[:,j], s=50, c=[ np.abs(c) for c in cs], edgecolor=None)
        axes[k].set_xlabel(f"PC {i}")
        axes[k].set_ylabel(f"PC {j}")
        axes[k].set_aspect("equal")
    
    plt.tight_layout()
    plt.savefig("img/3d_dimension_pairs_colored.png")
    plt.show()



.. image:: output_49_0.png


|Dimension pairs colored| |Line of Fifths|

.. |Dimension pairs colored| image:: img/3d_dimension_pairs_colored.png
.. |Line of Fifths| image:: img/lof.png

Historical development of tonality
----------------------------------

The line of fifths is an important underlying structure for pitch-class
distributions in tonal compositions

But we have treated all pieces in our dataset as synchronic and have not
yet taken their historical location into account.

Remember the tonal pitch-class distribution of an example piece above?

.. figure:: img/random_piece.png
   :alt: Random piece

   Random piece

Let’s assume the pitch-class content of a piece spreads on the line of
fifths from F to A\ :math:`\sharp`.

.. figure:: img/lof.png
   :alt: Line of fifths

   Line of fifths

This means, its range on the line of fifths is :math:`10 - (-1) = 11`.
The piece covers eleven consecutive fifths on the lof.

We can generalize this calculation and write a function that calculates
the range for each piece in the dataset.

.. code:: ipython3

    def lof_range(piece):
        l = [i for i, v in enumerate(piece) if v!=0]
        return max(l) - min(l)

.. code:: ipython3

    data["lof_range"] = data.loc[:, lof].apply(lof_range, axis=1) # create a new column
    data.sample(20)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>composer</th>
          <th>composer_first</th>
          <th>work_group</th>
          <th>work_catalogue</th>
          <th>opus</th>
          <th>no</th>
          <th>mov</th>
          <th>title</th>
          <th>composition</th>
          <th>publication</th>
          <th>source</th>
          <th>display_year</th>
          <th>Fbb</th>
          <th>Cbb</th>
          <th>Gbb</th>
          <th>Dbb</th>
          <th>Abb</th>
          <th>Ebb</th>
          <th>Bbb</th>
          <th>Fb</th>
          <th>Cb</th>
          <th>Gb</th>
          <th>Db</th>
          <th>Ab</th>
          <th>Eb</th>
          <th>Bb</th>
          <th>F</th>
          <th>C</th>
          <th>G</th>
          <th>D</th>
          <th>A</th>
          <th>E</th>
          <th>B</th>
          <th>F#</th>
          <th>C#</th>
          <th>G#</th>
          <th>D#</th>
          <th>A#</th>
          <th>E#</th>
          <th>B#</th>
          <th>F##</th>
          <th>C##</th>
          <th>G##</th>
          <th>D##</th>
          <th>A##</th>
          <th>E##</th>
          <th>B##</th>
          <th>lof_range</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>1022</th>
          <td>Victoria</td>
          <td>TomasLuisde</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>O vos omnes</td>
          <td>NaN</td>
          <td>1585.0</td>
          <td>ELVIS</td>
          <td>1585.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>9</td>
          <td>1</td>
          <td>0</td>
          <td>8</td>
          <td>25</td>
          <td>19</td>
          <td>25</td>
          <td>51</td>
          <td>67</td>
          <td>35</td>
          <td>9</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>11</td>
        </tr>
        <tr>
          <th>51</th>
          <td>Bach</td>
          <td>Johann Sebastian</td>
          <td>Wohltemperiertes Klavier II</td>
          <td>BWV</td>
          <td>877</td>
          <td>1</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1740.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1740.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>1</td>
          <td>18</td>
          <td>78</td>
          <td>120</td>
          <td>96</td>
          <td>122</td>
          <td>132</td>
          <td>156</td>
          <td>119</td>
          <td>47</td>
          <td>24</td>
          <td>40</td>
          <td>26</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>13</td>
        </tr>
        <tr>
          <th>941</th>
          <td>Mahler</td>
          <td>Gustav</td>
          <td>Kindertotenlieder</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>4</td>
          <td>NaN</td>
          <td>Oft denk' ich sie sind nur ausgegangen</td>
          <td>NaN</td>
          <td>1904.0</td>
          <td>OSLC</td>
          <td>1904.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>12</td>
          <td>0</td>
          <td>5</td>
          <td>53</td>
          <td>75</td>
          <td>66</td>
          <td>96</td>
          <td>106</td>
          <td>245</td>
          <td>65</td>
          <td>54</td>
          <td>51</td>
          <td>54</td>
          <td>30</td>
          <td>12</td>
          <td>4</td>
          <td>22</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>17</td>
        </tr>
        <tr>
          <th>261</th>
          <td>Koželuh</td>
          <td>Leopold</td>
          <td>Piano Sonata</td>
          <td>Op.</td>
          <td>38</td>
          <td>3</td>
          <td>2</td>
          <td>Allegretto</td>
          <td>1793.0</td>
          <td>NaN</td>
          <td>DB</td>
          <td>1793.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>4</td>
          <td>88</td>
          <td>192</td>
          <td>69</td>
          <td>178</td>
          <td>389</td>
          <td>392</td>
          <td>232</td>
          <td>123</td>
          <td>103</td>
          <td>114</td>
          <td>42</td>
          <td>14</td>
          <td>8</td>
          <td>3</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>15</td>
        </tr>
        <tr>
          <th>1335</th>
          <td>Schumann</td>
          <td>Robert</td>
          <td>Liederkreis</td>
          <td>Op.</td>
          <td>39</td>
          <td>7</td>
          <td>NaN</td>
          <td>Auf einer Burg</td>
          <td>1840.0</td>
          <td>1842.0</td>
          <td>OSLC</td>
          <td>1840.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>26</td>
          <td>82</td>
          <td>51</td>
          <td>29</td>
          <td>52</td>
          <td>102</td>
          <td>54</td>
          <td>16</td>
          <td>0</td>
          <td>13</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>10</td>
        </tr>
        <tr>
          <th>1286</th>
          <td>Schubert</td>
          <td>Franz</td>
          <td>Winterreise</td>
          <td>D. 911</td>
          <td>89</td>
          <td>7</td>
          <td>NaN</td>
          <td>Auf dem Flusse</td>
          <td>NaN</td>
          <td>1827.0</td>
          <td>OSLC</td>
          <td>1827.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>1</td>
          <td>5</td>
          <td>0</td>
          <td>40</td>
          <td>88</td>
          <td>44</td>
          <td>111</td>
          <td>173</td>
          <td>287</td>
          <td>178</td>
          <td>70</td>
          <td>84</td>
          <td>142</td>
          <td>91</td>
          <td>15</td>
          <td>0</td>
          <td>7</td>
          <td>3</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>17</td>
        </tr>
        <tr>
          <th>1714</th>
          <td>Grieg</td>
          <td>Edvard</td>
          <td>Lyrical Pieces</td>
          <td>Op.</td>
          <td>12</td>
          <td>8</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1866.0</td>
          <td>1867.0</td>
          <td>DCML</td>
          <td>1866.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>4</td>
          <td>0</td>
          <td>10</td>
          <td>27</td>
          <td>66</td>
          <td>65</td>
          <td>41</td>
          <td>26</td>
          <td>63</td>
          <td>29</td>
          <td>7</td>
          <td>6</td>
          <td>4</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>13</td>
        </tr>
        <tr>
          <th>401</th>
          <td>Bach</td>
          <td>Johann Sebastian</td>
          <td>Wohltemperiertes Klavier I</td>
          <td>BWV</td>
          <td>868</td>
          <td>2</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1722.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1722.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>1</td>
          <td>21</td>
          <td>99</td>
          <td>136</td>
          <td>135</td>
          <td>143</td>
          <td>115</td>
          <td>135</td>
          <td>90</td>
          <td>23</td>
          <td>8</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>11</td>
        </tr>
        <tr>
          <th>857</th>
          <td>Rue</td>
          <td>Pierre de la</td>
          <td>Ave Sanctissima Maria</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Cruxifixus</td>
          <td>1485.0</td>
          <td>NaN</td>
          <td>ELVIS</td>
          <td>1485.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>21</td>
          <td>19</td>
          <td>29</td>
          <td>22</td>
          <td>19</td>
          <td>23</td>
          <td>17</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>6</td>
        </tr>
        <tr>
          <th>2009</th>
          <td>Joplin</td>
          <td>Scott</td>
          <td>Ragtimes</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Wall Street Rag</td>
          <td>NaN</td>
          <td>1909.0</td>
          <td>CCARH</td>
          <td>1909.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>6</td>
          <td>9</td>
          <td>20</td>
          <td>72</td>
          <td>188</td>
          <td>303</td>
          <td>151</td>
          <td>154</td>
          <td>232</td>
          <td>173</td>
          <td>42</td>
          <td>73</td>
          <td>16</td>
          <td>19</td>
          <td>37</td>
          <td>0</td>
          <td>2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>16</td>
        </tr>
        <tr>
          <th>1869</th>
          <td>Corelli</td>
          <td>Arcangelo</td>
          <td>12 concerti grossi</td>
          <td>Op.</td>
          <td>6</td>
          <td>10</td>
          <td>4.0</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1714.0</td>
          <td>CCARH</td>
          <td>1714.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>79</td>
          <td>174</td>
          <td>206</td>
          <td>167</td>
          <td>147</td>
          <td>151</td>
          <td>141</td>
          <td>34</td>
          <td>0</td>
          <td>12</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>9</td>
        </tr>
        <tr>
          <th>1520</th>
          <td>Alkan</td>
          <td>Charles Valentin</td>
          <td>Un Morceau Caractéristique</td>
          <td>Op.</td>
          <td>74</td>
          <td>2</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1840.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1840.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>154</td>
          <td>140</td>
          <td>38</td>
          <td>90</td>
          <td>285</td>
          <td>474</td>
          <td>274</td>
          <td>62</td>
          <td>78</td>
          <td>226</td>
          <td>88</td>
          <td>1</td>
          <td>8</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>12</td>
        </tr>
        <tr>
          <th>741</th>
          <td>Granados</td>
          <td>Enrique</td>
          <td>Goyescas</td>
          <td>Op.</td>
          <td>11</td>
          <td>5</td>
          <td>NaN</td>
          <td>El Amor y la muerte (balada)</td>
          <td>1909.0</td>
          <td>1912.0</td>
          <td>MS</td>
          <td>1909.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>13</td>
          <td>84</td>
          <td>141</td>
          <td>138</td>
          <td>199</td>
          <td>267</td>
          <td>296</td>
          <td>310</td>
          <td>300</td>
          <td>306</td>
          <td>415</td>
          <td>282</td>
          <td>308</td>
          <td>382</td>
          <td>239</td>
          <td>138</td>
          <td>134</td>
          <td>84</td>
          <td>77</td>
          <td>23</td>
          <td>19</td>
          <td>15</td>
          <td>0</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>23</td>
        </tr>
        <tr>
          <th>462</th>
          <td>Bach</td>
          <td>Johann Sebastian</td>
          <td>Inventions and Sinfonias</td>
          <td>BWV</td>
          <td>773</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1723.0</td>
          <td>MS</td>
          <td>1723.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>41</td>
          <td>93</td>
          <td>80</td>
          <td>90</td>
          <td>102</td>
          <td>92</td>
          <td>106</td>
          <td>47</td>
          <td>2</td>
          <td>14</td>
          <td>9</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>10</td>
        </tr>
        <tr>
          <th>1304</th>
          <td>Schumann</td>
          <td>Robert</td>
          <td>Dichterliebe</td>
          <td>Op.</td>
          <td>48</td>
          <td>12</td>
          <td>NaN</td>
          <td>Am leuchtenden Sommermorgen</td>
          <td>1840.0</td>
          <td>NaN</td>
          <td>OSLC</td>
          <td>1840.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>2</td>
          <td>12</td>
          <td>6</td>
          <td>3</td>
          <td>27</td>
          <td>113</td>
          <td>96</td>
          <td>49</td>
          <td>42</td>
          <td>58</td>
          <td>37</td>
          <td>13</td>
          <td>23</td>
          <td>11</td>
          <td>10</td>
          <td>0</td>
          <td>1</td>
          <td>3</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>17</td>
        </tr>
        <tr>
          <th>1689</th>
          <td>Corelli</td>
          <td>Arcangelo</td>
          <td>12 Trio Sonatas</td>
          <td>Op.</td>
          <td>1</td>
          <td>8</td>
          <td>3.0</td>
          <td>Largo</td>
          <td>NaN</td>
          <td>1681.0</td>
          <td>CCARH</td>
          <td>1681.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>39</td>
          <td>55</td>
          <td>44</td>
          <td>39</td>
          <td>88</td>
          <td>90</td>
          <td>66</td>
          <td>7</td>
          <td>0</td>
          <td>13</td>
          <td>3</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>10</td>
        </tr>
        <tr>
          <th>1320</th>
          <td>Schumann</td>
          <td>Robert</td>
          <td>Frauenliebe und Leben</td>
          <td>Op.</td>
          <td>42</td>
          <td>3</td>
          <td>NaN</td>
          <td>Ich kann's nicht fassen, nicht glauben</td>
          <td>1840.0</td>
          <td>NaN</td>
          <td>OSLC</td>
          <td>1840.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>3</td>
          <td>2</td>
          <td>5</td>
          <td>49</td>
          <td>74</td>
          <td>54</td>
          <td>62</td>
          <td>129</td>
          <td>108</td>
          <td>57</td>
          <td>26</td>
          <td>10</td>
          <td>16</td>
          <td>17</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>14</td>
        </tr>
        <tr>
          <th>983</th>
          <td>Dufay</td>
          <td>Guillaume</td>
          <td>Missa l'homme armé</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Kyrie</td>
          <td>1474.0</td>
          <td>NaN</td>
          <td>ELVIS</td>
          <td>1474.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>29</td>
          <td>35</td>
          <td>26</td>
          <td>65</td>
          <td>54</td>
          <td>41</td>
          <td>18</td>
          <td>8</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>8</td>
        </tr>
        <tr>
          <th>1525</th>
          <td>Alkan</td>
          <td>Charles Valentin</td>
          <td>Un Morceau Caractéristique</td>
          <td>Op.</td>
          <td>74</td>
          <td>7</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>1840.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1840.0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>5</td>
          <td>3</td>
          <td>22</td>
          <td>66</td>
          <td>210</td>
          <td>221</td>
          <td>76</td>
          <td>81</td>
          <td>226</td>
          <td>144</td>
          <td>20</td>
          <td>21</td>
          <td>46</td>
          <td>18</td>
          <td>4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>14</td>
        </tr>
        <tr>
          <th>1427</th>
          <td>Scriabin</td>
          <td>Alexander</td>
          <td>NaN</td>
          <td>Op.</td>
          <td>9</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>Nocturne for the left hand</td>
          <td>1894.0</td>
          <td>NaN</td>
          <td>MS</td>
          <td>1894.0</td>
          <td>0</td>
          <td>1</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>61</td>
          <td>17</td>
          <td>33</td>
          <td>117</td>
          <td>215</td>
          <td>248</td>
          <td>110</td>
          <td>99</td>
          <td>151</td>
          <td>94</td>
          <td>49</td>
          <td>83</td>
          <td>127</td>
          <td>79</td>
          <td>48</td>
          <td>99</td>
          <td>95</td>
          <td>99</td>
          <td>38</td>
          <td>5</td>
          <td>11</td>
          <td>36</td>
          <td>10</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>27</td>
        </tr>
      </tbody>
    </table>
    </div>



This allows us now to take the ``display_year`` (composition or
publication) and ``lof_range`` (range on the line of fifths) features to
observe historical changes.

.. code:: ipython3

    fig, ax = plt.subplots(figsize=(18,9))
    ax.scatter(data["display_year"].values, data["lof_range"].values, alpha=.5, s=50)
    ax.set_ylim(0,35)
    ax.set_xlabel("year")
    ax.set_ylabel("line-of-fifths range")
    plt.savefig("img/hist_scatter.png");



.. image:: output_59_0.png


.. figure:: img/hist_scatter.png
   :alt: Historical scatterplot

   Historical scatterplot

We could try to fit a line to this data to see whether there is a trend
(kinda obvious here).

.. code:: ipython3

    g = sns.lmplot(
        data=data, 
        x="display_year", 
        y="lof_range", 
        line_kws={"color":"k"},
        scatter_kws={"alpha":.5},
    #     lowess=True,
        height=8,
        aspect=2
    )
    g.savefig("img/hist_scatter_line.png");



.. image:: output_62_0.png


.. figure:: img/hist_scatter_line.png
   :alt: Line Scatter

   Line Scatter

But actually, this is not the best idea. Why should any historical
process be linear? More complex models might make more sense.

A more versatile technique is *Locally Weighted Scatterplot Smoothing*
(LOWESS) that locally fits a polynomial. Using this method, we see that
a non-linear process is displayed.

.. code:: ipython3

    from statsmodels.nonparametric.smoothers_lowess import lowess
    
    x = data.display_year
    y = data.lof_range
    l = lowess(y,x)
    
    fig, ax = plt.subplots(figsize=(15,10))
    
    ax.scatter(x,y, s=50)
    ax.plot(l[:,0], l[:,1], c="k")
    ax.set_ylabel("line-of-fifths range")
    plt.savefig("img/hist_scatter_lowess.png")
    plt.show()



.. image:: output_66_0.png


.. figure:: img/hist_scatter_lowess.png
   :alt: Scatter Lowess

   Scatter Lowess

If there is time: some more advanced stuff
------------------------------------------

.. code:: ipython3

    B = 200
    delta = 1/10 
    
    fig, ax = plt.subplots(figsize=(16,9))
    
    x = data.display_year
    y = data.lof_range
    l = lowess(y,x, frac=delta)
    
    ax.scatter(x,y, s=50, alpha=.25)
    
    for _ in range(B):
        resampled = data.sample(data.shape[0], replace=True)
        
        xx = resampled.display_year
        yy = resampled.lof_range
        ll = lowess(yy,xx, frac=delta)
        
        ax.plot(ll[:,0], ll[:,1], c="k", alpha=.05)
        
    ax.plot(l[:,0], l[:,1], c="yellow")
    
    ## REGIONS
    from matplotlib.patches import Rectangle
    
    text_kws = {
        "rotation" : 90,
        "fontsize" : 16,
        "bbox" : dict(
            facecolor="white", 
            boxstyle="round"
        ),
        "horizontalalignment" : "center",
        "verticalalignment" : "center"
    }
    
    rect_props = {
        "width" : 40,
        "zorder" : -1,
        "alpha" : 1.
    }
    
    stylecolors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
    
    ax.text(1980, 3, "diatonic", **text_kws)
    ax.axhline(6.5, c="gray", linestyle="--", lw=2) # dia / chrom.
    ax.add_patch(Rectangle((1960,0), height=6.5, facecolor=stylecolors[0], **rect_props))
    
    ax.text(1980, 9.5, "chromatic", **text_kws)
    ax.axhline(12.5, c="gray", linestyle="--", lw=2) # chr. / enh.
    ax.add_patch(Rectangle((1960,6.5), height=6, facecolor=stylecolors[1], **rect_props))
    
    ax.text(1980, 23.5, "enharmonic", **text_kws)
    ax.add_patch(Rectangle((1960,12.5), height=28, facecolor=stylecolors[2], **rect_props))
    
    ax.set_ylim(0,35)
    ax.set_xlim(1300,2000)
    
    ax.set_ylabel("line-of-fifths range")
    plt.savefig("img/final.png", dpi=300)
    plt.show()



.. image:: output_69_0.png


Usung bootstrap sampling we achieve an estimation of the local varience
of the data and thus of the diversity in the note usage of the musical
pieces.

.. figure:: img/final.png
   :alt: Final Result

   Final Result

We also can distinguish three regions in terms of line-of-fifth range:
diatonic, chromatic, and enharmonic.

Grouping the data together in these three regions, we see a clear change
from diatonic and chromatic to chromatic and enharmonic pieces over the
course of history.

.. code:: ipython3

    epochs = {
        "Renaissance" : [1300, 1549],
        "Baroque" : [1550, 1649],
        "Classical" : [1650, 1749],
        "Early\nRomantic" : [1750, 1819],
        "Late Romantic/\nModern" : [1820, 2000]
    }   
    
    strata = [
        "diatonic",
        "chromatic",
        "enharmonic"
    ]
    
    widths = data[["display_year", "lof_range"]].sort_values(by="display_year").reset_index(drop=True)
    
    df = pd.concat(
        [
            widths[ 
                (widths.display_year >= epochs[e][0]) & (widths.display_year <= epochs[e][1]) 
            ]["lof_range"].value_counts(normalize=True).sort_index().groupby( 
                lambda x: strata[0] if x <= 6 else strata[1] if x <= 12 else strata[2]
            ).sum() for e in epochs
        ], axis=1, sort=True
    )
    
    df.columns = epochs.keys()
    df = df.reindex(strata)
    df.T.plot(kind="bar", stacked=True, figsize=(12,5))
    # plt.title("Epochs")
    plt.legend(bbox_to_anchor=(1.3,0.75))
    plt.gca().set_xticklabels(epochs.keys(), rotation="horizontal")
    plt.tight_layout()
    plt.savefig("img/epochs_regions.png")
    plt.show()



.. image:: output_72_0.png


.. figure:: img/epochs_regions.png
   :alt: Epochs

   Epochs

-  Renaissance: largest diatonic proportion overall but mostly chromatic
-  Baroque: alost completely chromatic
-  Classical: enharmonic proportion increases -> more distant
   modulations
-  This trend continues through the Romantic eras

Summary
-------

.. raw:: html

   <p>

1. We have analyzed a very specific aspect of Western classical music.

   .. raw:: html

      </p>

   .. raw:: html

      <p class="fragment fade-in">

   2. We have used a large(-ish) corpus to answer our research question.

      .. raw:: html

         </p>

      .. raw:: html

         <p class="fragment fade-in">

      3. We have operationalized musical pieces as vectors that
         represent distributions of tonal pitch-classes.

         .. raw:: html

            </p>

         .. raw:: html

            <p class="fragment fade-in">

         4. We have used the dimensionality-reduction technique
            Principal Component Analysis (PCA) in order to visually
            inspect the distribution of the data in 2 and 3 dimensions.

            .. raw:: html

               </p>

            .. raw:: html

               <p class="fragment fade-in">

            5. We have used music-theoretical domain knowledge to find
               meaningful structure in this space.

               .. raw:: html

                  </p>

               .. raw:: html

                  <p class="fragment fade-in">

               6. We have seen that pieces are largely distributed along
                  the line of fifths.

                  .. raw:: html

                     </p>

                  .. raw:: html

                     <p class="fragment fade-in">

                  7. We have used Locally Weighted Scatterplot Smoothing
                     (LOWESS) to estimate the variance in this
                     historical process.

                     .. raw:: html

                        </p>

                     .. raw:: html

                        <p class="fragment fade-in">

                     8. We have seen that, historically, composers
                        explore ever larger regions on this line and
                        that the variance also increases.

                        .. raw:: html

                           </p>

Conclusion
----------

1. Data-driven approaches to music analysis offer new ways of studying
   music history.
2. One of the largest obstacles is the lack of appropriate data (maybe
   you could help improve the situation?)
3. It is difficult to operationalize/formalize musical concepts.
4. Good news: there is a lot to be done for Master/PhD students!

The end
-------

-  Thank you very much for participating in this workhop
-  I would appreciate it if you would send me some feedback (mail:
   fabian.moss@epfl.ch; Twitter:
   [@fabianmoss](https://twitter.com/fabianmoss))
-  Please get in touch if you are interested in working on a small
   project
-  Special thanks to Diana Kayser for organization and making everyhing
   possible!!!
-  My funding: École Polytechnique Fédérale de Lausane (EPFL) and Swiss
   National Science Foundation (SNSF)
