from processFunctions import query_wikidata_dump

path = '/home/aboschin/datasets/wikidata/'
dump_path = '/home/aboschin/datasets/wikidata/latest-all.json.bz2'
n_lines = 70000000
query_wikidata_dump(path, dump_path, n_lines, test_entities=None, collect_labels=True)
