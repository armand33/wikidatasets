=====
Usage
=====

This is an example of how to build the subgraph of all human entities from WikiData::

    import pickle
    from wikidatasets.processFunctions import get_subclasses, query_wikidata_dump, build_dataset

    path = 'humans/'  # this will contain the files output through the process
    dump_path = 'latest-all.json.bz2'  # path to the bz2 dump file
    n_lines = 56208653  # this can be an upper bound
    # common name of Homo sapiens, unique extant species of the genus Homo
    test_entities = get_subclasses('Q5')

    query_wikidata_dump(dump_path, path, n_lines,
                        test_entities=test_entities, collect_labels=True)

    labels = pickle.load(open(path + 'labels.pkl', 'rb'))
    build_dataset(path, labels)
