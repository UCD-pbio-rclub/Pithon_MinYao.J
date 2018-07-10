# Problem 2
# Write a class called "Organism".
# Have the class initialize with the organism's complete taxonomic lineage (KPCOFGS) and common name.
# Write methods which allow a user to see these values in informative ways.


class Organism:
	
	def __init__(self,
                     Domain,
                     Kingdom,
                     Phylum,
                     Class,
                     Order,
                     Family,
                     Genus,
                     Species,
                     common_name):
		self.Domain = Domain
		self.Kingdom = Kingdom
		self.Phylum = Phylum
		self.Class = Class
		self.Order = Order
		self.Family = Family
		self.Genus = Genus
		self.Species = Species
		self.common_name = common_name
	
	def description(self):
		print( 'Domain:', self.Domain, "\n",
                       'Kingdom:', self.Kingdom, "\n",
                       'Phylum:', self.Phylum, "\n",
                       'Class:', self.Class, "\n",
                       'Order:',self.Order, "\n",
                       'Family:',self.Family, "\n",
                       'Genus:',self.Genus, "\n",
                       'Species:',self.Species, "\n",
                       'Common_name:',self.common_name, sep = "")

Cc = Organism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta campestris', 'golden dodder')
print(Cc.description())

