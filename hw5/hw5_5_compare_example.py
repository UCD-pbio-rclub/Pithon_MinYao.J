# Problem 5
# Import your class and function from problems 3 and 4. Demonstrate using them together

from hw5_2_organism import Organism

from hw5_3_long_organism import LongOrganism

from hw5_4_compare_function import *

Cc = LongOrganism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta_campestris', 'golden_dodder', 2, 581, 56, 'North_America')
print(Cc.description())
print(Cc.more_description())
#print(Cc.string_description())

Cp = LongOrganism('Eukarya', 'Plantae', 'Anthophyta', 'Eudicotyledonae', 'Solanales', 'Convolvulaceae', 'Cuscuta', 'Cuscuta_pentagona', 'fiveangled_dodder', 2, 'unknown ', 56, 'North_America')
print(Cp.description())
print(Cp.more_description())
#print(Cp.string_description())


compare(Cc.string_description(),Cp.string_description())
compare_D(Cc,Cp)
compare_K(Cc,Cp)
compare_P(Cc,Cp)
compare_C(Cc,Cp)
compare_O(Cc,Cp)
compare_F(Cc,Cp)
compare_G(Cc,Cp)
compare_S(Cc,Cp)
compare_CN(Cc,Cp)
compare_size(Cc,Cp)
compare_chn(Cc,Cp)
compare_plo(Cc,Cp)
compare_reg(Cc,Cp)
