# Problem 3
# Demonstrate inheritance by importing your class "Organism" from problem 2.
# Use it to create a new class called "LongOrganism" which inherits "Organism" and modifies it by adding any other attributes that may be significant about an organism (ie ploidy, genome size, region).
# Write new methods which allow a user to see these values in informative ways.

from hw5_2_organism import Organism

class LongOrganism(Organism):
	def __init__(self,Domain,Kingdom,Phylum,Class,Order,Family,Genus,Species,common_name,ploidy,size,number,region):
			Organism.__init__(self,Domain,Kingdom,Phylum,Class,Order,Family,Genus,Species,common_name)
			self.ploidy = ploidy
			self.size = size
			self.number = number
			self.region = region


	def more_description(self):
			print('Ploidy:', self.ploidy, "\n",
				  'Genome size:', self.size, 'Mbp',"\n",
				  'Chromosome number (2n):', self.number, "\n",
				  'Native region:', self.region, "\n", sep = "")
			


#Cc = LongOrganism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta_campestris', 'golden_dodder', 2, 581, 56, 'North_America')
#print(Cc.description())
#print(Cc.more_description())
#print(Cc.string_description())

#Cp = LongOrganism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta_pentagona', 'fiveangled_dodder', 2, 'unknown ', 56, 'North_America')
#print(Cp.description())
#print(Cp.more_description())
#print(Cp.string_description())



