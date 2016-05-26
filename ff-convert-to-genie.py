import json
import sys, os
import string
from ast import literal_eval

iris = open(os.path.expanduser('~/Desktop/iris.data'))

## Convert to Genie data format:
i = 0
for row in iris.readlines():
    i += 1
    d = string.split(string.strip(row), ',')
    name = d.pop(-1)[5:]  ## indexing to remove the 'Iris-' part of the string.
    data = {"strings": [name], "vectors": [[literal_eval(n) for n in d]], "scalars": []}
    data = json.dumps(data)

    output = open(os.path.expanduser('~/Desktop/Iris-gdf/%s-%s' %(i, name)), 'w')
    output.write(data + '\n')
    output.close()

iris.close()
