# Problem 4.
# Write a function which allows a user to compare and/or contrast two instances of your class "LongOrganism"

from hw5_2_organism import Organism

class LongOrganism(Organism):
	def __init__(self,Domain,Kingdom,Phylum,Class,Order,Family,Genus,Species,common_name,ploidy,size,number,region):
			Organism.__init__(self,Domain,Kingdom,Phylum,Class,Order,Family,Genus,Species,common_name)
			self.ploidy = ploidy
			self.size = size
			self.number = number
			self.region = region


	def description(self):
			Organism.description(self)
			print('Ploidy:', self.ploidy, "\n",
				  'Genome size:', self.size, 'Mbp',"\n",
				  'Chromosome number (2n):', self.number, "\n",
				  'Native region:', self.region, "\n", sep = "")
			


Cc = LongOrganism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta campestris', 'golden dodder', 2, 581, 56, 'North America')
print(Cc.description())

Cp = LongOrganism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta pentagona', 'fiveangled dodder', 2, 'unknown ', 56, 'North America')
print(Cp.description())

import difflib

diff = difflib.context_diff(Cc.description(), Cp.description())
print (diff)



