import pandas as pd
from utils import query_wikidata_dump, clean

path = '/home/aboschin/datasets/wikidata/'
path_pickle = '/home/aboschin/datasets/wikidata/companies/'
n_lines = 70000000
tails = pd.read_csv('/home/aboschin/datasets/wikidata/subclasses/subclasses_companies.tsv', sep='\t')['item'].apply(clean).values

query_wikidata_dump(path, path_pickle, n_lines, query_tails=tails)