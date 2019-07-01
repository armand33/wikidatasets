============
WikiDataSets
============


.. image:: https://img.shields.io/pypi/v/wikidatasets.svg
        :target: https://pypi.python.org/pypi/wikidatasets

.. image:: https://img.shields.io/travis/armand33/wikidatasets.svg
        :target: https://travis-ci.org/armand33/wikidatasets

.. image:: https://readthedocs.org/projects/wikidatasets/badge/?version=latest
        :target: https://wikidatasets.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/armand33/wikidatasets/shield.svg
     :target: https://pyup.io/repos/github/armand33/wikidatasets/
     :alt: Updates



Code to parse WikiData dumps into smaller knowledge graphs (e.g. graph of human entities).


* Free software: BSD license
* Documentation: https://wikidatasets.readthedocs.io.

Data Sets
---------
Data sets are available on this `page <https://graphs.telecom-paristech.fr/Home_page.html#wikidatasets-section)>`_.

Features
--------
The `example/` folder contains examples of scripts to create datasets (e.g. `build_humans.py <https://github.com/armand33/WikiDataSets/blob/master/examples/build_humans.py>`_).
Such scripts should be placed in the main directory (along with `utils.py`, `processFunctions.py`) and hard-coded paths should be tuned to match your installation.

Citations
---------

If you find this code useful in your research, please consider citing our `paper <https://arxiv.org/abs/1906.04536>`_:

| @misc{arm2019wikidatasets,
    |title={WikiDataSets : Standardized sub-graphs from WikiData},
    |author={Armand Boschin},
    |year={2019},
    |eprint={1906.04536},
    |archivePrefix={arXiv},
    |primaryClass={cs.LG}
}

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
