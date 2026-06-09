from Bio.Seq import Seq
from Bio.SeqUtils import seq3
dna= Seq("ATGCCGATTGACUUUGCACGATAG")
dna_complement= dna.complement()
reverse_dnacomplement = dna.reverse_complement()
print("The Dna seq is :",dna)
print("The complement of dna is : ",dna_complement)
print("The reverse complement of dna is:  ",reverse_dnacomplement)
rna= dna.transcribe()
print("Rna Seq : ",rna)
protein= rna.translate()
print("Protein Seq : ", protein)
print(seq3(protein))