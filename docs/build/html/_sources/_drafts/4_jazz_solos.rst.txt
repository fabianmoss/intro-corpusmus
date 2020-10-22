Solos in the *Weimar Jazz Database*
-----------------------------------

.. figure:: _static/jazz.jpg
   :width: 100%
   :align: center
   :alt: Jazz.

   Photo by `Janine Robinson <https://unsplash.com/@janinekrob?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_
   on `Unsplash <https://unsplash.com/s/photos/jazz?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText>`_

The first project we will have a look at is the `Jazzomat <https://jazzomat.hfm-weimar.de/>`_ project.
Transcriptions of Jazz solos :cite:`Pfleiderer2017`. The *Weimar Jazz Database* (WJD) consists of 
456 transcriptions of Jazz solos from diverse substyles.
As all the corpora that we deal with here, it is freely available on the internet. [#fn1]_

The WJD contains a number of tables:

.. list-table:: Tables in the *Weimar Jazz Database*
   :header-rows: 1
   :widths: 30 70 

   * - Table name
     - Description
   * - ``beats``
     - Table for beat annotation of WJD melodies, referenced by ``melody(melid)``
   * - ``composition_info``
     - Infos regarding the underlying composition of a WJD solo, referenced by ``melody(melid)``
   * - ``db_info``
     - Information regarding the distributed database file like version information, license, etc
   * - ``esac_info``
     - EsAC infos for EsAC melodies, referenced by ``melody(melid)``
   * - ``melody``
     - Main table for all melody events
   * - ``melody_type``
     - Indicated type of melody: WJD solos or EsAC (Folk songs using Essen Associative Code), referenced by ``melody(melid)``
   * - ``popsong_info``
     - Pop song infos, referenced by ``melody(melid)``
   * - ``record_info``
     - Infos regarding the specific audio recording of a WJD solo was taken from, referenced by ``melody(melid)``
   * - ``sections``
     - All sections (phrase, chorus, form, chords, etc.), referenced by ``melody(melid)``
   * - ``solo_info``
     - Solo infos for WJD solos, referenced by ``melody(melid)``
   * - ``track_info``
     - Information specific to a track on a record (or CD)
   * - ``transcription_info``
     - Transcription infos for WJD solos, referenced by ``melody(melid)``

Here, we focus on the main table ``melody``. First, we download the entire database from `<https://jazzomat.hfm-weimar.de/download/download.html>`_ 
(under "Weimar Jazz Database") and save it as the file ``wjazz.db``. 

.. code-block:: python

   import sqlite3 # for working with databases
   import pandas as pd # for working with tabular data

   # create connection to database
   conn = sqlite3.connect("wjazzd.db")

   # read all entries of the `melody` table into a pandas DataFrame
   df = pd.read_sql("SELECT * FROM melody", con=conn)

   df.head()

>>> df.head()
output

The part of the code ``SELECT * FROM melody`` reads "Select all entries from the table 'melody'".

.. [#fn1] https://jazzomat.hfm-weimar.de/dbformat/dboverview.html