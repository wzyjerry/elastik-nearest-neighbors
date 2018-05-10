import json
import re
import sys

assert len(sys.argv) > 1, "Usage: <script.py> path-to-unzipped-glove-vecs.txt"

re_letters_only = re.compile("[^a-zA-Z]")

for line in open(sys.argv[1]):
    tkns = line.split(" ")
    word = tkns[0]
    if len(re_letters_only.sub("", word)) == 0:
        continue
    vector = list(map(lambda x: round(float(x), 5), tkns[1:]))
    doc = {
        "_id": word,
        "_source": {
            "description": "Word vector for: %s" % word,
            "_aknn_vector": vector
        }
    }
    print(json.dumps(doc))