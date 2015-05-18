from __future__ import print_function

import random
with open('oceny.csv', 'w+') as f:
    print('student,zadanie,ocena', file=f)
    for student in xrange(20):
        for x in xrange(5):
            ocena = random.randint(2,5)
            print('student%d,zadanie%d,%d' % (student, x, ocena), file=f)

 
