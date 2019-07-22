.. _processFunctions:


Process Functions
*****************

.. currentmodule:: wikidatasets.processFunctions


Get subclasses
--------------
Get a list of WikiData IDs of entities which are subclasses of the subject.

.. autofunction:: wikidatasets.processFunctions.get_subclasses

Query wikidata dump
-------------------
Go through a Wikidata dump. It can either collect entities that are instances of test entities or collect the dictionary of labels. It can also do both.

.. autofunction:: wikidatasets.processFunctions.query_wikidata_dump

Build dataset
-------------
Builds datasets from the pickle files produced by ``query_wikidata_dump``.

.. autofunction:: wikidatasets.processFunctions.build_dataset
