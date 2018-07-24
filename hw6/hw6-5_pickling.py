# Problem 5
# Create an instance of your 'Organism' class from last week. Demonstrate pickling it to a file, and loading it from the file.
# Note: when opening the file you may need to add the 'b' option

import sys
import pickle

sys.path.append('/home/pi/Python/hw5')
from hw5_2_organism import *

Cc = Organism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta_campestris', 'golden_dodder')

Cc.description()

with open('organism.pickle', 'wb') as f:
    pickle.dump(Cc, f)

with open('organism.pickle', 'rb') as n:
    b = pickle.load(n)

b.description()
