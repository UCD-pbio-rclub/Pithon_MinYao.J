# Problem 4
# Write a function which allows a user to compare and/or contrast two instances of your class "LongOrganism"

def compare(string1, string2):
    if string1 == string2:
        print ("Same organism!")
    
    else:
        print ("Different organism!")

def compare_D(sp1,sp2):
    if sp1.Domain == sp2.Domain:
        print ("Same Domain!")

    else:
        print ("Different Domain!")

def compare_K(sp1,sp2):
    if sp1.Kingdom == sp2.Kingdom:
        print ("Same Kingdom!")

    else:
        print ("Different Kingdom!")

def compare_P(sp1,sp2):
    if sp1.Phylum == sp2.Phylum:
        print ("Same Phylum!")

    else:
        print ("Different Phylum!")

def compare_C(sp1,sp2):
    if sp1.Class == sp2.Class:
        print ("Same Class!")

    else:
        print ("Different Class!")


def compare_O(sp1,sp2):
    if sp1.Order == sp2.Order:
        print ("Same Order!")

    else:
        print ("Different Order!")

def compare_F(sp1,sp2):
    if sp1.Family == sp2.Family:
        print ("Same Family!")

    else:
        print ("Different Family!")

        
def compare_G(sp1,sp2):
    if sp1.Genus == sp2.Genus:
        print ("Same Genus!")

    else:
        print ("Different Genus!")


def compare_S(sp1,sp2):
    if sp1.Species == sp2.Species:
        print ("Same Species!")

    else:
        print ("Different Species!")
        


def compare_CN(sp1,sp2):
    if sp1.common_name == sp2.common_name:
        print ("Same common name!")

    else:
        print ("Different common name!")




def compare_plo(sp1,sp2):
    if sp1.ploidy == sp2.ploidy:
        print ("Same ploidy!")

    else:
        print ("Different ploidy!")

def compare_size(sp1,sp2):
    if sp1.size == sp2.size:
        print ("Same genome size!")

    else:
        print ("Different genome size!")

def compare_chn(sp1,sp2):
    if sp1.number == sp2.number:
        print ("Same chromosome number!")

    else:
        print ("Different chromosome number!")

def compare_reg(sp1,sp2):
    if sp1.region == sp2.region:
        print ("Same native region!")

    else:
        print ("Different native region!")



        

        
