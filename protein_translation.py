from Bio.Seq import Seq
m_dna= Seq("ATGCCGTAATGCCATGCATAGTCA")
m_rna= Seq("AUGCCGUAAUGCCAUGCAUAGUCA")
protein = m_rna.translate()
print(protein)
jay_z="Hello World"
print(jay_z[0:5:1])
print(jay_z[-1:-6:-1])