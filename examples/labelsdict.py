from processFunctions import get_subclasses, query_wikidata_dump, build_dataset

path = '/home/aboschin/datasets/wikidata/'
dump_path = '/home/public/wikidata/latest-all.json.bz2'
n_lines = 56208653

query_wikidata_dump(dump_path, path, n_lines, test_entities=None, collect_labels=True)
