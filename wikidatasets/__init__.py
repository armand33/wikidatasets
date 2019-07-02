# -*- coding: utf-8 -*-

"""Top-level package for WikiDataSets."""

__author__ = """Armand Boschin"""
__email__ = 'aboschin@enst.fr'
__version__ = '0.1.2'

from .processFunctions import get_subclasses
from .processFunctions import query_wikidata_dump
from .processFunctions import build_dataset

from .utils import load_data_labels
