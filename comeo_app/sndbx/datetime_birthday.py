__author__ = 'ipostolaki'

# Weekend birthdate!

from datetime import *

r = range(1990, 2030)

for step_year in r:
    #print(step_year)

    t = date(step_year, 7, 21)

    wd = t.isoweekday()
    if wd==6 or wd==7:
        s = '%d %d' %(step_year, wd)
        print(s)