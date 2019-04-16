import pandas as pd
import pickle
from utils import clean
from processFunctions import query_wikidata_dump, build_dataset


path = '/home/aboschin/datasets/wikidata/countries/'
dump_path = '/home/aboschin/datasets/wikidata/latest-all.json.bz2'
n_lines = 70000000
tails = pd.read_csv('/home/aboschin/datasets/wikidata/subclasses/subclasses_countries.tsv',
                    sep='\t')['item'].apply(clean).values

query_wikidata_dump(dump_path, path, n_lines, test_entities=tails, collect_labels=False)

labels = pickle.load(open(path + 'labels.pkl', 'rb'))
build_dataset(path, labels)