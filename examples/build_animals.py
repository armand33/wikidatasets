import pickle
from processFunctions import get_subclasses, query_wikidata_dump, build_dataset


path = '/home/aboschin/datasets/wikidata/animals/'
dump_path = '/home/public/wikidata/latest-all.json.bz2'
n_lines = 56208653

test_entities = get_subclasses('Q16521')  # group of one or more organism(s), which a taxonomist
                                          # adjudges to be a unit

query_wikidata_dump(dump_path, path, n_lines, test_entities=test_entities, collect_labels=False)

labels = pickle.load(open('/home/aboschin/datasets/wikidata/labels.pkl', 'rb'))
build_dataset(path, labels)
