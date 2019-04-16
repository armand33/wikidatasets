import pandas as pd
from utils import clean
from processFunctions import query_wikidata_dump


path = '/home/aboschin/datasets/wikidata/humans/'
dump_path = '/home/aboschin/datasets/wikidata/latest-all.json.bz2'
n_lines = 70000000
tails = pd.read_csv('/home/aboschin/datasets/wikidata/subclasses/subclasses_humans.tsv',
                    sep='\t')['item'].apply(clean).values

query_wikidata_dump(dump_path, path, n_lines, test_entities=tails, collect_labels=False)
