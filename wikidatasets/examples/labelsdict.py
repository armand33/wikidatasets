from wikidatasets.processFunctions import query_wikidata_dump

# change the 3 following values to match your installation
path = '../'  # this will contain the files output through the process
dump_path = 'latest-all.json.bz2'  # path to the bz2 dump file
n_lines = 81933324  # this can be an upper bound

query_wikidata_dump(dump_path, path, n_lines, test_entities=None, collect_labels=True)
