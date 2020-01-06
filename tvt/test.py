# test program 

import collections
PolicyOutputs = collections.namedtuple(
    'PolicyOutputs', ['policy', 'action', 'baseline'])

P = PolicyOutputs(1,2,3)
print(P.policy)