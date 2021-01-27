class DNA:
    def __init__(self,dna):
        self.dna=dna
    def count_nucleotides(self):
        dictionary_dna={"A":0,"T":0,"G":0,"C":0}
        for i in self.dna:
            dictionary_dna[i]+=1
        return dictionary_dna
    def calculate_complement(self):
        complement=""
        for i in self.dna:
            if i=="A":
                complement+="T"
            elif i=="T":
                complement+="A"
            elif i=="G":
                complement+="C"
            elif i=="C":
                complement+="G"
        return complement
    def count_point_mutations(self,dna_to_control):
        counter=0
        for i in range(len(dna_to_control)):
            if dna_to_control[i]!=self.dna[i]:
                counter+=1
        return counter
    def find_motif(self,dna_motif):
        index_list=[]
        for i in range(0,(len(self.dna)-len(dna_motif)+1)):
            if self.dna[i:len(dna_motif)+i]==dna_motif:
                index_list.append(i)
        return index_list

dna=DNA("GATATATGCATATACTT")
print(dna.find_motif("ATAT"))

