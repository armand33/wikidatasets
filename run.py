import sys
import getopt
from utils import query_wikidata_dump


if __name__ == '__main__':
    # Read command line args
    myopts, args = getopt.getopt(sys.argv[1:], "n:p:r:t:")

    ###############################
    # o == option
    # a == argument passed to the o
    ###############################
    for o, a in myopts:
        if o == '-n':
            n_lines = a
        elif o == '-p':
            path = a
        elif o == '-r':
            query_rel = a
        elif o == '-t':
            query_tail = a
        else:
            print("Usage: %s -n numberOfLines -p path -r rel -t tail" % sys.argv[0])

    query_wikidata_dump(path, n_lines, query_rel=query_rel, query_tail=query_tail)
