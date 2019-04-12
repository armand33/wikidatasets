import pickle
import bz2
import json

from tqdm import tqdm


def concat_claims(claims):
    """
    :param claims: dict
    :return: iterator through the claims
    """
    for rel_id, rel_claims in claims.items():
        for claim in rel_claims:
            yield claim


def to_triplets(ent):
    """
    :param ent: dict coming from the parsing of a json line of the dump
    :return: list of triplets of this entity (head, rel, tail)
    """
    if len(ent['claims']) == 0:
        return []
    claims = concat_claims(ent['claims'])
    triplets = []
    e1 = ent['id']
    for claim in claims:
        mainsnak = claim['mainsnak']
        if mainsnak['snaktype'] != "value":
            continue
        if mainsnak['datatype'] == 'wikibase-item':
            rel = mainsnak['property']
            e2 = 'Q{}'.format(mainsnak['datavalue']['value']['numeric-id'])
            triplets.append((e1, rel, e2))
    return triplets


def get_type(ent):
    return ent['type']


def get_id(ent):
    return ent['id']


def get_label(ent):
    """
    :param ent: dict coming from the parsing of a json line of the dump
    :return: string label of ent in english if available of any other language else
    """
    labels = ent['labels']
    if len(labels) == 0:
        return 'No label {}'.format(ent['id'])
    if 'en' in labels.keys():
        return labels['en']['value']
    else:
        return labels[list(labels.keys())[0]]['value']


def relabel(x, labels):
    try:
        return labels[x]
    except KeyError:
        return x


def dump_pickle(path, triplet, n_dump):
    with open(path+'dump{}.pkl'.format(n_dump), 'wb') as f:
        pickle.dump(triplet, f)
    print('Just made pickle dump number {}'.format(n_dump))


def query_wikidata_dump(path, n_lines, query_rel='P31', query_tail='Q5'):
    """
    :param path: path to the latest-all.json.bz2 file downloaded from
    https://dumps.wikimedia.org/wikidatawiki/entities/
    :param n_lines: number of lines of the dump. Fastest way I found was
    `$ bzgrep -c ".*" latest-all.json.bz2`
    :param query_rel: For each line (entity), we check if it as a fact of the type
    (id, query_rel, query_tail). Default is 'P31' which is the Wikidata code for 'is instance of'.
    :param query_tail: For each line (entity), we check if it as a fact of the type
    (id, query_rel, query_tail). Default is 'Q5' which is the Wikidata code for 'human'.
    :return:
    """
    labels = {}
    human_facts = []
    fails = []

    dump = bz2.open(path+'latest-all.json.bz2', 'rt')
    progress_bar = tqdm(total=n_lines)

    line = dump.readline()  # the first line of the file should be "[\n" so we skip it
    counter = 0  # counter of the number of lines read
    n_pickle_dump = 0

    while len(line) > 0:  # while there are lines to read
        counter += 1
        line = dump.readline().strip()
        progress_bar.update(1)
        if line[-1] == ',':
            line = line[:-1]  # all lines should end with a ','
        try:
            # turn string to json
            if line[0] != '{' or line[-1] != '}':
                # then this line is not a proper json file we should deal with it later
                fails.append(line)
                continue
            line = json.loads(line)

            # extract data from json
            id_ = get_id(line)
            labels[id_] = get_label(line)
            triplets = to_triplets(line)

            if len(triplets) > 0 and (id_, query_rel, query_tail) in triplets:
                human_facts.extend(triplets)

        except:
            fails.append(line)

        if counter % 3000000 == 0:
            # dump in pickle to free memory
            n_pickle_dump += 1
            dump_pickle(path, (labels, human_facts, fails), n_pickle_dump)

            # empty variables
            del labels, human_facts, fails
            labels = {}
            human_facts = []
            fails = []

    n_pickle_dump += 1
    dump_pickle(path, (labels, human_facts, fails), n_pickle_dump)
