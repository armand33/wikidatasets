import bz2
import pickle
import os
import pandas as pd

from tqdm import tqdm
from utils import get_results, clean
from utils import get_pickle_path, write_to_pickle
from utils import get_id, get_label, to_triplets, intersect, to_json
from utils import concatpkls, write_csv, write_ent_dict, write_rel_dict, write_readme, relabel


def get_subclasses(subject):
    """
    :param subject: String describing the subject (e.g. Q5 for human)
    :return: list of WikiData IDs of entities which are subclasses of the subject.
    """
    endpoint_url = "https://query.wikidata.org/sparql"
    query = """SELECT ?item WHERE {?item wdt:P279* wd:""" + subject + """ .}"""

    results = get_results(endpoint_url, query)

    return [clean(result['item']['value']) for result in results['results']['bindings']]


def query_wikidata_dump(dump_path, path, n_lines, test_entities=None, collect_labels=False):
    """
    :param dump_path: path to the latest-all.json.bz2 file downloaded from
    https://dumps.wikimedia.org/wikidatawiki/entities/
    :param path: path to where pickle files will be written.
    :param n_lines: number of lines of the dump. Fastest way I found was
    `$ bzgrep -c ".*" latest-all.json.bz2`
    :param test_entities: list of entities to check if a line is instance of.
    For each line (entity), we check if it as a fact of the type (id, query_rel, test_entity).
    :param collect_labels:
    """
    pickle_path = get_pickle_path(path)
    collect_facts = (test_entities is not None)
    fails = []

    if collect_labels:
        labels = {}
    if collect_facts:
        facts = []
        n_pickle_dump = 0

    dump = bz2.open(dump_path, 'rt')
    progress_bar = tqdm(total=n_lines)
    counter = 0  # counter of the number of lines read
    line = dump.readline()  # the first line of the file should be "[\n" so we skip it

    while True:
        # while there are lines to read
        line = dump.readline().strip()
        if len(line) == 0:
            break

        counter += 1
        progress_bar.update(1)

        try:
            line = to_json(line)

            if collect_labels:
                id_ = get_id(line)
                labels[id_] = get_label(line)

            if collect_facts:
                triplets, instanceOf = to_triplets(line)
                if len(instanceOf) > 0 and intersect(instanceOf, test_entities):
                    facts.extend(triplets)

        except:
            if type(line) == dict and ('claims' in line.keys()):
                if len(line['claims']) != 0:
                    fails.append(line)
            else:
                fails.append(line)

        if counter % 3000000 == 0:
            # dump in pickle to free memory
            if collect_facts:
                n_pickle_dump += 1
                facts, fails = write_to_pickle(pickle_path, facts, fails, n_pickle_dump)

    if collect_facts:
        _, _ = write_to_pickle(pickle_path, facts, fails, n_pickle_dump + 1)
    if collect_labels:
        pickle.dump(labels, open(path + 'labels.pkl', 'wb'))


def build_dataset(path, labels, return_=False, dump_date='23rd April 2019'):
    """
    Print dataset in path (includes 4 files : edges (kg), attributes, entities, relations.
    :param path: path to the directory where there should already be a pickle/ directory.
    In the latter directory, all the .pkl files will be concatenated into one dataset.
    :param labels: dictionary coming from the function get_labels_dict
    :param return_: bool
    :param dump_date: str
    """
    if path[-1] != '/':
        path = path+'/'
    path_pickle = path + 'pickles/'
    n_files = len([name for name in os.listdir(path_pickle) if name[-4:] == '.pkl'])
    df = concatpkls(n_files, path_pickle)

    ents = list(df['headEntity'].unique())
    feats = list(set(df['tailEntity'].unique()) - set(ents))
    ent2ix = {ent: i for i, ent in enumerate(ents + feats)}
    ix2ent = {i: ent for ent, i in ent2ix.items()}

    tmp = df['relation'].unique()
    rel2ix = {rel: i for i, rel in enumerate(tmp)}
    ix2rel = {i: rel for rel, i in rel2ix.items()}

    df['headEntity'] = df['headEntity'].apply(lambda x: ent2ix[x])
    df['tailEntity'] = df['tailEntity'].apply(lambda x: ent2ix[x])
    df['relation'] = df['relation'].apply(lambda x: rel2ix[x])

    entities = pd.DataFrame([[i, ix2ent[i]] for i in range(len(ix2ent))],
                            columns=['entityID', 'wikidataID'])
    entities['label'] = entities['wikidataID'].apply(relabel, args=(labels,))

    relations = pd.DataFrame([[i, ix2rel[i]] for i in range(len(ix2rel))],
                             columns=['relationID', 'wikidataID'])
    relations['label'] = relations['wikidataID'].apply(relabel, args=(labels,))

    edges_mask = df.tailEntity.isin(df['headEntity'].unique())
    edges = df.loc[edges_mask, ['headEntity', 'tailEntity', 'relation']]
    attributes = df.loc[~edges_mask, ['headEntity', 'tailEntity', 'relation']]

    write_csv(edges, path + 'edges.txt')
    write_csv(attributes, path + 'attributes.txt')
    write_ent_dict(entities, path + 'entities.txt')
    write_rel_dict(relations, path + 'relations.txt')
    write_readme(path+'readme.txt',
                 n_core_ents=attributes['headEntity'].nunique(),
                 n_attrib_ents=attributes['tailEntity'].nunique(),
                 n_core_rels=edges['relation'].nunique(),
                 n_attrib_rels=attributes['relation'].nunique(),
                 n_core_facts=len(edges),
                 n_attrib_facts=len(attributes),
                 dump_date=dump_date)

    if return_:
        return edges, attributes, entities, relations
