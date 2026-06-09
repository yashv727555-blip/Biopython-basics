from Bio.Seq import Seq
#Creating a dna sequence
m_dna= Seq("ATGCCGTAATGCCATGCATAGTCA")
print("Dna Sequesnce is : ",m_dna)
print(m_dna.reverse_complement())