import pickle
from processFunctions import get_subclasses, query_wikidata_dump, build_dataset


path = '/home/aboschin/datasets/wikidata/humans/'
dump_path = '/home/public/wikidata/latest-all.json.bz2'
n_lines = 70000000

test_entities = get_subclasses('Q5')  # common name of Homo sapiens, unique extant species of the genus Homo

query_wikidata_dump(dump_path, path, n_lines, test_entities=test_entities, collect_labels=True)

labels = pickle.load(open('/home/aboschin/datasets/wikidata/labels.pkl', 'rb'))
build_dataset(path, labels)
